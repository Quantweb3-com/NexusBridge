import asyncio

import aiohttp

from typing import Any, Dict, Callable
from urllib.parse import urljoin, urlencode

import orjson
from aiolimiter import AsyncLimiter

from nexusbridge.base import ApiClient, WSClient
from nexusbridge.binance.authentication import rsa_signature, hmac_hashing, ed_25519
from nexusbridge.binance.constants import KeyType
from nexusbridge.binance.error import BinanceClientError, BinanceServerError


class BinanceApiClient(ApiClient):
    def __init__(
        self,
        base_url: str,
        private_key=None,
        private_key_passphrase=None,
        secret: str = None,
        key: str = None,
        timeout: int = 10,
        max_rate: int | None = None,
    ):
        super().__init__(
            secret=secret,
            timeout=timeout,
            max_rate=max_rate,
        )
        self._headers = {
            "Content-Type": "application/json",
            "User-Agent": "TradingBot/1.0",
        }

        if key:
            self._headers["X-MBX-APIKEY"] = key

        self.private_key = private_key
        self.private_key_pass = private_key_passphrase
        self.secret = secret
        self.base_url = base_url

    def _get_sign(self, payload):
        if self.private_key:
            return rsa_signature(self.private_key, payload, self.private_key_pass)
        return hmac_hashing(self.secret, payload)

    def _prepare_payload(self, payload: Dict[str, Any], signed: bool) -> str:
        """Prepare payload by encoding and optionally signing."""
        # payload = {k: str(v).lower() if isinstance(v, bool) else v for k, v in payload.items()}
        if signed:
            payload["timestamp"] = self._clock.timestamp_ms()
            encoded_payload = urlencode(payload)
            signature = self._get_sign(encoded_payload)
            return f"{encoded_payload}&signature={signature}"
        return urlencode(payload)

    async def _fetch(
        self,
        method: str,
        endpoint: str,
        payload: Dict[str, Any] = None,
        signed: bool = False,
    ):
        """Make an asynchronous HTTP request."""
        if self._limiter:
            await self._limiter.wait()

        self._init_session()

        url = urljoin(self.base_url, endpoint)
        payload = payload or {}
        encoded_payload = self._prepare_payload(payload, signed)

        if method.upper() == "GET":
            url = f"{url}?{encoded_payload}"
            data = None
        else:
            data = encoded_payload

        self._log.debug(f"Request: {method} {url}")

        try:
            response = await self._session.request(
                method=method,
                url=url,
                headers=self._headers,
                data=data,
            )
            status = response.status
            raw = await response.read()
            self._log.debug(f"Response: {raw}")
            if 400 <= status < 500:
                text = await response.text()
                raise BinanceClientError(status, text, self._headers)
            elif status >= 500:
                text = await response.text()
                raise BinanceServerError(status, text, self._headers)
            return orjson.loads(raw)

        except aiohttp.ClientError as e:
            self._log.error(f"Client Error {method} Url: {url} {e}")
            raise
        except asyncio.TimeoutError:
            self._log.error(f"Timeout {method} Url: {url}")
            raise
        except Exception as e:
            self._log.error(f"Error {method} Url: {url} {e}")
            raise


class BinanceWSClient(WSClient):
    def __init__(
        self,
        url: str,
        handler: Callable[..., Any],
        key=None,
        secret=None,
        listen_key=None,
        private_key=None,
        key_type: KeyType = None,
        private_key_passphrase=None,
        **kwargs,
    ):
        self.key_type = key_type
        self.key = key
        self.secret = secret
        self.private_key = private_key
        self.private_key_passphrase = private_key_passphrase
        self.key_type = (key_type,)
        listen_key = listen_key
        super().__init__(
            url,
            limiter=AsyncLimiter(max_rate=3, time_period=1),
            handler=handler,
            **kwargs,
        )

    def _get_sign(self, payload):
        pairs = payload.split("&")
        pairs.sort()
        payload = "&".join(pairs)
        if self.key_type[0] == KeyType.RSA:
            return rsa_signature(self.private_key, payload, self.private_key_passphrase)
        elif self.key_type[0] == KeyType.Ed:
            return ed_25519(self.private_key, payload, self.private_key_passphrase)
        else:
            return hmac_hashing(self.secret, payload)

    async def _subscribe(
        self, params: str | list[str], subscription_id: str | None = None
    ):
        if isinstance(params, str):
            params = [params]

        new_params = [param for param in params if param not in self._subscriptions]
        if not new_params:
            return

        subscription_id = subscription_id or self._clock.timestamp_ms()
        await self._connect()
        payload = {
            "method": "SUBSCRIBE",
            "params": new_params,
            "id": subscription_id,
        }
        await self._send(payload)
        self._subscriptions.update({param: payload for param in new_params})
        self._log.info(f"Subscribed to {subscription_id} with payload: {payload}")

    async def _unsubscribe(self, params: str | list[str], subscription_id: int):
        if isinstance(params, str):
            params = [params]

        valid_params = [param for param in params if param in self._subscriptions]
        if not valid_params:
            return

        await self._connect()
        payload = {
            "method": "UNSUBSCRIBE",
            "params": valid_params,
            "id": subscription_id,
        }
        await self._send(payload)
        for param in valid_params:
            self._subscriptions.pop(param, None)
        self._log.info(f"Unsubscribed from {subscription_id} with payload: {payload}")

    async def send(
        self, method: str, params: list[Any] | None = None, _id: str | None = None
    ):
        await self._connect()
        payload = {
            "method": method,
            "id": _id or self._clock.timestamp_ms(),
        }
        if params:
            payload["params"] = params

        await self._send(payload)

    async def _resubscribe(self):
        for _, payload in self._subscriptions.items():
            await self._send(payload)
