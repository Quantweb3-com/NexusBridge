import asyncio
import aiohttp

from typing import Any, Dict
from urllib.parse import urljoin, urlencode, unquote

import orjson

from nexus.base import ApiClient
from nexus.binance.authentication import rsa_signature, hmac_hashing


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

    async def _fetch(
            self,
            method: str,
            endpoint: str,
            payload: Dict[str, Any] = None,
            signed: bool = False,
            timestamp: bool = False
    ):
        self._init_session()

        url = urljoin(self.base_url, endpoint)
        payload = payload or {}
        if timestamp:
            payload["timestamp"] = self._clock.timestamp_ms()
        if signed:
            payload = urlencode(payload)
            signature = self._get_sign(payload)
            payload += f"&signature={signature}"
        payload_str = (
            unquote(urlencode(payload))
            if method == "GET"
            else orjson.dumps(payload).decode("utf-8")
        )

        if method == "GET":
            url += f"?{payload_str}"
            payload_str = None
        self._log.debug(f"Request: {url}")
        try:
            response = await self._session.request(
                method=method,
                url=url,
                headers=self._headers,
                data=payload_str
            )
            return orjson.loads(await response.read())
        except aiohttp.ClientError as e:
            self._log.error(f"Client Error {method} Url: {url} {e}")
            raise
        except asyncio.TimeoutError:
            self._log.error(f"Timeout {method} Url: {url}")
            raise
        except Exception as e:
            self._log.error(f"Error {method} Url: {url} {e}")
            raise
        finally:
            await self.close_session()
