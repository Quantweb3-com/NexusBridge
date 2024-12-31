import hmac
import hashlib
import aiohttp
import asyncio
import orjson
from typing import Any, Dict, List
from urllib.parse import urljoin, urlencode, unquote

from nexus.base import ApiClient
from nexus.bybit.constants import BybitUrl
from nexus.bybit.error import BybitError

from nexus.bybit.api import AccountApi, PositionApi, TradeApi, MarketApi, AssetApi


class BybitApiClient(ApiClient):
    def __init__(
            self,
            api_key: str = None,
            secret: str = None,
            url: BybitUrl = BybitUrl.TESTNET,
            timeout: int = 10,
    ):
        """
        ### Testnet:
        `https://api-testnet.bybit.com`

        ### Mainnet:
        (both endpoints are available):
        `https://api.bybit.com`
        `https://api.bytick.com`

        ### Important:
        Netherland users: use `https://api.bybit.nl` for mainnet
        Hong Kong users: use `https://api.byhkbit.com` for mainnet
        Turkey users: use `https://api.bybit-tr.com` for mainnet
        Kazakhstan users: use `https://api.bybit.kz` for mainnet
        """

        super().__init__(
            api_key=api_key,
            secret=secret,
            timeout=timeout,
        )
        self._recv_window = 5000

        self._base_url = url.base_url

        self._headers = {
            "Content-Type": "application/json",
            "User-Agent": "TradingBot/1.0",
        }

        if api_key:
            self._headers["X-BAPI-API-KEY"] = api_key

        self.trade_api = TradeApi(self._fetch)
        self.account_api = AccountApi(self._fetch)
        self.position_api = PositionApi(self._fetch)
        self.market_api = MarketApi(self._fetch)
        self.asset_api = AssetApi(self._fetch)

    def _generate_signature(self, payload: str) -> List[str]:
        timestamp = str(self._clock.timestamp_ms())

        param = str(timestamp) + self._api_key + str(self._recv_window) + payload
        hash = hmac.new(
            bytes(self._secret, "utf-8"), param.encode("utf-8"), hashlib.sha256
        )
        signature = hash.hexdigest()
        return [signature, timestamp]

    async def _fetch(
            self,
            method: str,
            endpoint: str,
            payload: Dict[str, Any] = None,
            signed: bool = False,
    ):
        self._init_session()

        url = urljoin(self._base_url, endpoint)
        payload = payload or {}

        payload_str = (
            unquote(urlencode(payload))
            if method == "GET"
            else orjson.dumps(payload).decode("utf-8")
        )

        headers = self._headers
        if signed:
            signature, timestamp = self._generate_signature(payload_str)
            headers = {
                **headers,
                "X-BAPI-TIMESTAMP": timestamp,
                "X-BAPI-SIGN": signature,
                "X-BAPI-RECV-WINDOW": str(self._recv_window),
            }

        if method == "GET":
            url += f"?{payload_str}"
            payload_str = None

        try:
            self._log.debug(f"Request: {url} {payload_str}")
            response = await self._session.request(
                method=method,
                url=url,
                headers=headers,
                data=payload_str,
            )
            raw = await response.read()
            if response.status >= 400:
                raise BybitError(
                    code=response.status,
                    message=orjson.loads(raw) if raw else None,
                )
            bybit_response = orjson.loads(raw)
            if bybit_response["retCode"] == 0:
                return raw
            else:
                raise BybitError(
                    code=bybit_response["retCode"],
                    message=bybit_response["retMsg"],
                )
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

    def __getattr__(self, name):
        if hasattr(self.trade_api, name):
            return getattr(self.trade_api, name)
        elif hasattr(self.position_api, name):
            return getattr(self.position_api, name)
        elif hasattr(self.account_api, name):
            return getattr(self.account_api, name)
        elif hasattr(self.market_api, name):
            return getattr(self.market_api, name)
        elif hasattr(self.asset_api, name):
            return getattr(self.asset_api, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
