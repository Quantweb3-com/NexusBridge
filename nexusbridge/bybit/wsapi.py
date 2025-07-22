import hmac
import orjson
import asyncio

from typing import Any, Callable, Literal
from aiolimiter import AsyncLimiter

from nexusbridge.base import WSClient
from nexusbridge.bybit.constants import BybitAccountType


def generate_topic(
    base: str, symbol: str, depth: int = None, interval: str = None
) -> str:
    if base == "orderbook" and depth:
        return f"orderbook.{depth}.{symbol}"
    elif (
        base == "publicTrade"
        or base == "tickers"
        or base == "liquidation"
        or base == "tickers_lt"
        or base == "lt"
    ):
        return f"{base}.{symbol}"
    elif base == "kline" or base == "kline_lt":
        return f"{base}.{interval}.{symbol}"
    else:
        raise ValueError(f"Invalid base topic {base} or missing parameters")


class BybitWSClient(WSClient):
    def __init__(
        self,
        account_type: BybitAccountType,
        handler: Callable[..., Any],
        api_key: str = None,
        secret: str = None,
    ):
        self._account_type = account_type
        self._api_key = api_key
        self._secret = secret
        self._authed = False
        if self.is_private:
            url = account_type.ws_private_url
        else:
            url = account_type.ws_public_url
        # Bybit: do not exceed 500 requests per 5 minutes
        super().__init__(
            url,
            limiter=AsyncLimiter(max_rate=500, time_period=5 * 60),
            handler=handler,
            ping_idle_timeout=5,
            ping_reply_timeout=2,
            specific_ping_msg=orjson.dumps({"op": "ping"}),
            auto_ping_strategy="ping_when_idle",
        )

    @property
    def is_private(self):
        return self._api_key is not None or self._secret is not None

    def _generate_signature(self):
        expires = self._clock.timestamp_ms() + 1_000
        signature = str(
            hmac.new(
                bytes(self._secret, "utf-8"),
                bytes(f"GET/realtime{expires}", "utf-8"),
                digestmod="sha256",
            ).hexdigest()
        )
        return signature, expires

    def _get_auth_payload(self):
        signature, expires = self._generate_signature()
        return {"op": "auth", "args": [self._api_key, expires, signature]}

    async def _auth(self):
        if not self._authed:
            await self._send(self._get_auth_payload())
            self._authed = True
            await asyncio.sleep(5)

    async def _subscribe(self, topic: str | list[str], auth: bool = False):
        if isinstance(topic, list):
            for t in topic:
                if t in self._subscriptions:
                    self._log.debug(f"Already subscribed to {t}")
                    topic.remove(t)
                    return
        else:
            if topic in self._subscriptions:
                self._log.debug(f"Already subscribed to {topic}")
                return
        await self._connect()
        payload = {
            "op": "subscribe",
            "args": [topic] if isinstance(topic, str) else topic,
        }
        if auth:
            await self._auth()
        if isinstance(topic, list):
            for t in topic:
                self._subscriptions[t] = payload
        else:
            self._subscriptions[topic] = payload
        await self._send(payload)
        self._log.debug(f"Subscribing to {topic}.{self._account_type.value}...")

    async def subscribe_multiple(self, topics: list[str], auth: bool = False):
        await self._subscribe(topics, auth)

    async def subscribe_order_book(self, symbol: str, depth: int):
        """
        ### Linear & inverse:
        - Level 1 data, push frequency: 10ms
        - Level 50 data, push frequency: 20ms
        - Level 200 data, push frequency: 100ms
        - Level 500 data, push frequency: 100ms

        ### Spot:
        - Level 1 data, push frequency: 10ms
        - Level 50 data, push frequency: 20ms
        - Level 200 data, push frequency: 200ms

        ### Option:
        - Level 25 data, push frequency: 20ms
        - Level 100 data, push frequency: 100ms
        """
        topic = generate_topic("orderbook", symbol, depth)
        await self._subscribe(topic)

    async def subscribe_trade(self, symbol: str):
        topic = generate_topic("publicTrade", symbol)
        await self._subscribe(topic)

    async def subscribe_ticker(self, symbol: str):
        topic = generate_topic("tickers", symbol)
        await self._subscribe(topic)

    async def subscribe_kline(self, symbol: str, interval: str):
        """
        ### Available intervals:
        - 1 3 5 15 30 (min)
        - 60 120 240 360 720 (min)
        """
        topic = generate_topic("kline", symbol, interval=interval)
        await self._subscribe(topic)

    async def subscribe_liquidation(self, symbol: str):
        """
        Subscribe to the liquidation stream. Pushes at most one order per second per symbol. As such, this feed does not push all liquidations that occur on Bybit.
        """
        topic = generate_topic("liquidation", symbol)
        await self._subscribe(topic)

    async def subscribe_lt_kline(self, symbol: str, interval: str):
        """
        Available intervals:
        1 3 5 15 30 (min)
        60 120 240 360 720 (min)
        D (day)
        W (week)
        M (month)
        """
        topic = generate_topic("kline_lt", symbol, interval=interval)
        await self._subscribe(topic)

    async def subscribe_lt_ticker(self, symbol: str):
        topic = generate_topic("tickers_lt", symbol)
        await self._subscribe(topic)

    async def subscribe_lt_nav(self, symbol: str):
        topic = generate_topic("lt", symbol)
        await self._subscribe(topic)

    async def _resubscribe(self):
        if self.is_private:
            self._authed = False
            await self._auth()
        for _, payload in self._subscriptions.items():
            await self._send(payload)

    async def subscribe_order(
        self,
        topic: Literal[
            "order", "order.spot", "order.linear", "order.inverse", "order.option"
        ] = "order",
    ):
        """
        ### Topics:

        #### All in one:
        - order

        Categorical topics:
        - order.spot
        - order.linear
        - order.inverse
        - order.option
        """
        await self._subscribe(topic, auth=True)

    async def subscribe_position(
        self,
        topic: Literal[
            "position", "position.linear", "position.inverse", "position.option"
        ] = "position",
    ):
        """
        ### Topics:

        #### All in one:
        - position

        Categorical topics:
        - position.linear
        - position.inverse
        - position.option
        """
        await self._subscribe(topic, auth=True)

    async def subscribe_wallet(self, topic: str = "wallet"):
        """
        ### Topics:
        - wallet
        """
        await self._subscribe(topic, auth=True)

    async def subscribe_execution(
        self,
        topic: Literal[
            "execution",
            "execution.spot",
            "execution.linear",
            "execution.inverse",
            "execution.option",
        ] = "execution",
    ):
        """
        ### Topics:
        - execution
        """
        await self._subscribe(topic, auth=True)

    async def subscribe_fast_execution(
        self,
        topic: Literal[
            "execution.fast.linear",
            "execution.fast.inverse",
            "execution.fast.spot",
            "execution.fast",
        ] = "execution.fast",
    ):
        await self._subscribe(topic, auth=True)

    async def subscribe_greek(self, topic: str = "greeks"):
        """
        ### Topics:
        - greeks
        """
        await self._subscribe(topic, auth=True)

    async def subscribe_dcp(
        self, topic: Literal["dcp.future", "dcp.spot", "dcp.option"]
    ):
        """
        ### Topics:
        Subscribe to the dcp stream to trigger DCP function.
        For example, connection A subscribes "dcp.xxx", connection B does not and connection C subscribes "dcp.xxx".
            If A is alive, B is dead, C is alive, then this case will not trigger DCP.
            If A is alive, B is dead, C is dead, then this case will not trigger DCP.
            If A is dead, B is alive, C is dead, then DCP is triggered when reach the timeWindow threshold
            To sum up, for those private connections subscribing "dcp" topic are all dead, then DCP will be triggered.
        """
        await self._subscribe(topic, auth=True)
