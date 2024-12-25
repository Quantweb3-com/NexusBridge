import msgspec
from typing import Dict, Any
import orjson
import hmac
import base64
import asyncio
import aiohttp
from urllib.parse import urljoin, urlencode
from nexus.base import ApiClient
from nexus.okx.constants import OkxUrl
from nexus.okx.error import OkxHttpError, OkxRequestError
from nexus.okx.schema import (
    OkxPlaceOrderResponse,
    OkxCancelOrderResponse,
    OkxGeneralResponse,
)


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
        self._place_order_decoder = msgspec.json.Decoder(OkxPlaceOrderResponse)
        self._cancel_order_decoder = msgspec.json.Decoder(OkxCancelOrderResponse)
        self._general_response_decoder = msgspec.json.Decoder(OkxGeneralResponse)
        self._headers = {
            "Content-Type": "application/json",
            "User-Agent": "TradingBot/1.0",
        }

    async def post_api_v5_trade_order(
        self,
        inst_id: str,
        td_mode: str,
        side: str,
        ord_type: str,
        sz: str,
        **kwargs,
    ) -> OkxPlaceOrderResponse:
        """
        Place a new order
        https://www.okx.com/docs-v5/en/#order-book-trading-trade-post-place-order

        {'arg': {'channel': 'orders', 'instType': 'ANY', 'uid': '611800569950521616'}, 'data': [{'instType': 'SWAP', 'instId': 'BTC-USDT-SWAP', 'tgtCcy': '', 'ccy': '', 'ordId': '1993784914940116992', 'clOrdId': '', 'algoClOrdId': '', 'algoId': '', 'tag': '', 'px': '80000', 'sz': '0.1', 'notionalUsd': '80.0128', 'ordType': 'limit', 'side': 'buy', 'posSide': 'long', 'tdMode': 'cross', 'accFillSz': '0', 'fillNotionalUsd': '', 'avgPx': '0', 'state': 'canceled', 'lever': '3', 'pnl': '0', 'feeCcy': 'USDT', 'fee': '0', 'rebateCcy': 'USDT', 'rebate': '0', 'category': 'normal', 'uTime': '1731921825881', 'cTime': '1731921820806', 'source': '', 'reduceOnly': 'false', 'cancelSource': '1', 'quickMgnType': '', 'stpId': '', 'stpMode': 'cancel_maker', 'attachAlgoClOrdId': '', 'lastPx': '91880', 'isTpLimit': 'false', 'slTriggerPx': '', 'slTriggerPxType': '', 'tpOrdPx': '', 'tpTriggerPx': '', 'tpTriggerPxType': '', 'slOrdPx': '', 'fillPx': '', 'tradeId': '', 'fillSz': '0', 'fillTime': '', 'fillPnl': '0', 'fillFee': '0', 'fillFeeCcy': '', 'execType': '', 'fillPxVol': '', 'fillPxUsd': '', 'fillMarkVol': '', 'fillFwdPx': '', 'fillMarkPx': '', 'amendSource': '', 'reqId': '', 'amendResult': '', 'code': '0', 'msg': '', 'pxType': '', 'pxUsd': '', 'pxVol': '', 'linkedAlgoOrd': {'algoId': ''}, 'attachAlgoOrds': []}]}
        """
        endpoint = "/api/v5/trade/order"
        payload = {
            "instId": inst_id,
            "tdMode": td_mode,
            "side": side,
            "ordType": ord_type,
            "sz": sz,
            **kwargs,
        }
        raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
        return self._place_order_decoder.decode(raw)

    async def post_api_v5_trade_cancel_order(
        self, inst_id: str, ord_id: str | None = None, cl_ord_id: str | None = None
    ) -> OkxCancelOrderResponse:
        """
        Cancel an existing order
        https://www.okx.com/docs-v5/en/#order-book-trading-trade-post-cancel-order
        """
        endpoint = "/api/v5/trade/cancel-order"
        payload = {"instId": inst_id}
        if ord_id:
            payload["ordId"] = ord_id
        if cl_ord_id:
            payload["clOrdId"] = cl_ord_id

        raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
        return self._cancel_order_decoder.decode(raw)

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
        payload: Dict[str, Any] = None,
        signed: bool = False,
    ) -> bytes:
        await self._init_session()
        url = urljoin(self._base_url, endpoint)
        request_path = endpoint
        headers = self._headers
        timestamp = self._get_timestamp()

        payload = payload or {}

        payload_json = urlencode(payload) if method == "GET" else orjson.dumps(payload)

        if method == "GET":
            url += f"?{payload_json}"
            payload_json = None

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
            okx_response = self._general_response_decoder.decode(raw)
            if okx_response.code == "0":
                return raw
            else:
                raise OkxRequestError(
                    error_code=okx_response.code,
                    status_code=response.status,
                    message=okx_response.msg,
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
