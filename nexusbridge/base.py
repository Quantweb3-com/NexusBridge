from abc import ABC, abstractmethod

import aiohttp
import certifi
import orjson
import ssl
import asynciolimiter

import asyncio
from typing import Any
from typing import Callable, Literal, Optional

from aiolimiter import AsyncLimiter
from picows import (
    ws_connect,
    WSFrame,
    WSTransport,
    WSListener,
    WSMsgType,
    WSAutoPingStrategy,
)
from nexusbridge.utils import Log, LiveClock


class ApiClient(ABC):
    def __init__(
        self,
        api_key: str = None,
        secret: str = None,
        timeout: int = 10,
        max_rate: int | None = None,
    ):
        self._api_key = api_key
        self._secret = secret
        self._timeout = timeout
        self._log = Log.get_logger(type(self).__name__)
        self._ssl_context = ssl.create_default_context(cafile=certifi.where())
        self._session: Optional[aiohttp.ClientSession] = None
        self._clock = LiveClock()

        if max_rate:
            self._limiter = asynciolimiter.Limiter(rate=max_rate)
        else:
            self._limiter = None

    def _init_session(self):
        if self._session is None:
            timeout = aiohttp.ClientTimeout(total=self._timeout)
            tcp_connector = aiohttp.TCPConnector(
                ssl=self._ssl_context, enable_cleanup_closed=True
            )
            self._session = aiohttp.ClientSession(
                connector=tcp_connector, json_serialize=orjson.dumps, timeout=timeout
            )

    async def close_session(self):
        if self._session:
            await self._session.close()
            self._session = None


class Listener(WSListener):
    def __init__(
        self,
        logger,
        handler: Callable[..., Any],
        specific_ping_msg=None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._log = logger
        self._specific_ping_msg = specific_ping_msg
        self._callback = handler
        self._clock = LiveClock()

    def send_user_specific_ping(self, transport: WSTransport):
        if self._specific_ping_msg:
            transport.send(WSMsgType.TEXT, self._specific_ping_msg)
            self._log.debug(f"Sent user specific ping {self._specific_ping_msg}")
        else:
            transport.send_ping()
            self._log.debug("Sent default ping.")

    def on_ws_connected(self, transport: WSTransport):
        self._log.debug("Connected to Websocket...")

    def on_ws_disconnected(self, transport: WSTransport):
        self._log.debug("Disconnected from Websocket.")

    def on_ws_frame(self, transport: WSTransport, frame: WSFrame):
        try:
            match frame.msg_type:
                case WSMsgType.PING:
                    # Only send pong if auto_pong is disabled
                    transport.send_pong(frame.get_payload_as_bytes())
                    return
                case WSMsgType.TEXT:
                    # Queue raw bytes for handler to decode
                    self._callback(frame.get_payload_as_bytes())
                    return
                case WSMsgType.CLOSE:
                    close_code = frame.get_close_code()
                    close_msg = frame.get_close_message()
                    self._log.warning(
                        f"Received close frame. Close code: {close_code}, Close message: {close_msg}"
                    )
                    return
        except Exception as e:
            self._log.error(f"Error processing message: {str(e)}")


class WSClient(ABC):
    def __init__(
        self,
        url: str,
        limiter: AsyncLimiter,
        handler: Callable[..., Any],
        specific_ping_msg: bytes = None,
        reconnect_interval: int = 1,
        ping_idle_timeout: int = 2,
        ping_reply_timeout: int = 1,
        auto_ping_strategy: Literal[
            "ping_when_idle", "ping_periodically"
        ] = "ping_when_idle",
        enable_auto_ping: bool = True,
        enable_auto_pong: bool = False,
    ):
        self._clock = LiveClock()
        self._url = url
        self._specific_ping_msg = specific_ping_msg
        self._reconnect_interval = reconnect_interval
        self._ping_idle_timeout = ping_idle_timeout
        self._ping_reply_timeout = ping_reply_timeout
        self._enable_auto_pong = enable_auto_pong
        self._enable_auto_ping = enable_auto_ping
        self._listener: Listener = None
        self._transport = None
        self._subscriptions = {}
        self._limiter = limiter
        self._handler = handler
        if auto_ping_strategy == "ping_when_idle":
            self._auto_ping_strategy = WSAutoPingStrategy.PING_WHEN_IDLE
        elif auto_ping_strategy == "ping_periodically":
            self._auto_ping_strategy = WSAutoPingStrategy.PING_PERIODICALLY
        self._log = Log.get_logger(type(self).__name__)

    @property
    def connected(self):
        return self._transport and self._listener

    async def _connect(self):
        if not self.connected:
            WSListenerFactory = lambda: Listener(
                self._log,
                handler=self._handler,
                specific_ping_msg=self._specific_ping_msg,
            )  # noqa: E731
            self._transport, self._listener = await ws_connect(
                WSListenerFactory,
                self._url,
                enable_auto_ping=self._enable_auto_ping,
                auto_ping_idle_timeout=self._ping_idle_timeout,
                auto_ping_reply_timeout=self._ping_reply_timeout,
                auto_ping_strategy=self._auto_ping_strategy,
                enable_auto_pong=self._enable_auto_pong,
            )

    async def connect(self):
        await self._connect()
        await self._connection_handler()

    async def _connection_handler(self):
        while True:
            try:
                if not self.connected:
                    await self._connect()
                    await self._resubscribe()
                await self._transport.wait_disconnected()
            except asyncio.CancelledError:
                self.disconnect()
                await asyncio.sleep(0.5)
                break
            except Exception as e:
                self._log.error(f"Connection error: {e}")
                self._log.debug("Websocket reconnecting...")
                self._transport, self._listener = None, None
                await asyncio.sleep(self._reconnect_interval)

    async def _send(self, payload: dict):
        await self._limiter.acquire()
        self._transport.send(WSMsgType.TEXT, orjson.dumps(payload))

    def disconnect(self):
        if self.connected:
            self._transport.disconnect()

    @abstractmethod
    async def _resubscribe(self):
        pass
