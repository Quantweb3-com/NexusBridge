from typing import Dict, Any
import orjson
import hmac
import base64
import asyncio
import aiohttp
from urllib.parse import urljoin, urlencode, unquote

from nexus.base import ApiClient
from nexus.okx.api import TradeApi, AlgoTradingApi, GridTradingApi, SignalBotTradingApi, RecurringBuyApi, \
    CopyTradingApi, MarketDataApi, PublicDataApi
from nexus.okx.api.trading_account import TradingAccountApi
from nexus.okx.constants import OkxUrl
from nexus.okx.error import OkxHttpError, OkxRequestError


class OkxApiClient(ApiClient):
    def __init__(
            self,
            api_key: str = None,
            secret: str = None,
            passphrase: str = None,
            url: OkxUrl = OkxUrl.DEMO,
            timeout: int = 10,
    ):
        super().__init__(
            api_key=api_key,
            secret=secret,
            timeout=timeout,
        )

        self._base_url = url.base_url
        self._passphrase = passphrase
        self._testnet = url.is_testnet
        self.trade_api = TradeApi(self._fetch)
        self.algo_trading_api = AlgoTradingApi(self._fetch)
        self.grid_trading_api = GridTradingApi(self._fetch)
        self.signal_bot_trading_api = SignalBotTradingApi(self._fetch)
        self.recurring_buy_api = RecurringBuyApi(self._fetch)
        self.copy_trading_api = CopyTradingApi(self._fetch)
        self.market_data_api = MarketDataApi(self._fetch)
        self.trading_account_api = TradingAccountApi(self._fetch)
        self.public_data_api = PublicDataApi(self._fetch)
        self._headers = {
            "Content-Type": "application/json",
            "User-Agent": "TradingBot/1.0",
        }

    def _generate_signature(self, message: str) -> str:
        mac = hmac.new(
            bytes(self._secret, encoding="utf8"),
            bytes(message, encoding="utf-8"),
            digestmod="sha256",
        )
        return base64.b64encode(mac.digest()).decode()

    async def _get_signature(
            self, ts: str, method: str, request_path: str, payload: Dict[str, Any] = None
    ) -> str:
        body = ""
        if method == "POST":
            body = {}
        if payload:
            body = orjson.dumps(payload).decode()

        sign_str = f"{ts}{method}{request_path}{body}"
        signature = self._generate_signature(sign_str)
        return signature

    def _get_timestamp(self) -> str:
        return (
            self._clock.utc_now()
            .isoformat(timespec="milliseconds")
            .replace("+00:00", "Z")
        )

    async def _get_headers(
            self, ts: str, method: str, request_path: str, payload: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        headers = self._headers
        signature = await self._get_signature(ts, method, request_path, payload)
        headers.update(
            {
                "OK-ACCESS-KEY": self._api_key,
                "OK-ACCESS-SIGN": signature,
                "OK-ACCESS-TIMESTAMP": ts,
                "OK-ACCESS-PASSPHRASE": self._passphrase,
            }
        )
        if self._testnet:
            headers["x-simulated-trading"] = "1"
        return headers

    async def _fetch(
            self,
            method: str,
            endpoint: str,
            payload: list[Dict[str, Any]] | Dict[str, Any] = None,
            signed: bool = False,
    ) -> bytes:
        self._init_session()
        url = urljoin(self._base_url, endpoint)
        request_path = endpoint
        headers = self._headers
        timestamp = self._get_timestamp()

        payload = payload or {}

        payload_json = unquote(urlencode(payload)) if method == "GET" else orjson.dumps(payload)

        if method == "GET":
            url += f"?{payload_json}"
            request_path = f"{request_path}?{payload_json}" if payload_json != '' else request_path
            payload_json = None
            # when method is GET, payload should be empty
            payload = {}

        if signed and self._api_key:
            headers = await self._get_headers(timestamp, method, request_path, payload)

        try:
            self._log.debug(
                f"Request {method} Url: {url} Headers: {headers} Payload: {payload_json}"
            )

            response = await self._session.request(
                method=method,
                url=url,
                headers=headers,
                data=payload_json,
            )
            raw = await response.read()
            if response.status >= 400:
                raise OkxHttpError(
                    status_code=response.status,
                    message=orjson.loads(raw),
                    headers=response.headers,
                )
            okx_response = orjson.loads(raw)
            if okx_response["code"] == "0":
                return raw
            else:
                if len(okx_response["data"]) == 0:
                    raise OkxRequestError(
                        error_code=okx_response["code"],
                        status_code=okx_response["code"],
                        message=okx_response["msg"],
                    )
                else:
                    for data in okx_response["data"]:
                        raise OkxRequestError(
                            error_code=data["sCode"],
                            status_code=response.status,
                            message=data["sMsg"],
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
        elif hasattr(self.algo_trading_api, name):
            return getattr(self.algo_trading_api, name)
        elif hasattr(self.grid_trading_api, name):
            return getattr(self.grid_trading_api, name)
        elif hasattr(self.signal_bot_trading_api, name):
            return getattr(self.signal_bot_trading_api, name)
        elif hasattr(self.recurring_buy_api, name):
            return getattr(self.recurring_buy_api, name)
        elif hasattr(self.copy_trading_api, name):
            return getattr(self.copy_trading_api, name)
        elif hasattr(self.market_data_api, name):
            return getattr(self.market_data_api, name)
        elif hasattr(self.trading_account_api, name):
            return getattr(self.trading_account_api, name)
        elif hasattr(self.public_data_api, name):
            return getattr(self.public_data_api, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
