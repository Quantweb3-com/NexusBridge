import asyncio
import json

import aiohttp

from typing import Any, Dict
from urllib.parse import urljoin, urlencode, unquote

import orjson

from nexus.base import ApiClient
from nexus.binance.authentication import rsa_signature, hmac_hashing
from nexus.binance.error import BinanceClientError, BinanceServerError

class BinanceApiClient(ApiClient):
    def __init__(
            self,
            base_url: str,
            private_key=None,
            private_key_passphrase=None,
            secret: str = None,
            key: str = None,
            timeout: int = 10,
    ):
        super().__init__(
            secret=secret,
            timeout=timeout,
        )
        self._headers = {
            "Content-Type": "application/json",
            "User-Agent": "TradingBot/1.0",
            "X-MBX-APIKEY": key,
        }
        self.private_key = private_key
        self.private_key_pass = private_key_passphrase
        self.secret = secret
        self.base_url = base_url

    def _get_sign(self, payload):
        if self.private_key:
            return rsa_signature(self.secret, payload, self.private_key_pass)
        return hmac_hashing(self.secret, payload)

    def _prepare_payload(self, payload: Dict[str, Any], signed: bool) -> str:
        """Prepare payload by encoding and optionally signing."""
        payload = {k: str(v).lower() if isinstance(v, bool) else v for k, v in payload.items()}
        if signed:
            payload["timestamp"] = self._clock.timestamp_ms()
            encoded_payload = urlencode(payload)
            signature = self._get_sign(encoded_payload)
            return f"{encoded_payload}&signature={signature}"
        return urlencode(payload)

    async def _fetch(self, method: str, endpoint: str, payload: Dict[str, Any] = None, signed: bool = False):
        """Make an asynchronous HTTP request."""
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
                raise BinanceClientError(status, response.text(), self._headers)
            elif status >= 500:
                raise BinanceServerError(status, response.text(), self._headers)
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
