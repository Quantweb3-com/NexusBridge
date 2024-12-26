from typing import Dict, Any, Literal
import orjson
import hmac
import base64
import asyncio
import aiohttp
from urllib.parse import urljoin, urlencode
from nexus.base import ApiClient
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
            okx_response = orjson.loads(raw)
            if okx_response["code"] == "0":
                return raw
            else:
                okx_error_response = orjson.loads(raw)
                for data in okx_error_response["data"]:
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

    async def post_api_v5_trade_order(
            self,
            inst_id: str,
            td_mode: str,
            side: str,
            ord_type: str,
            sz: str,
            **kwargs,
    ):
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
        return orjson.loads(raw)

    async def post_api_v5_trade_cancel_order(
            self, inst_id: str, ord_id: str | None = None, cl_ord_id: str | None = None
    ):
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
        return orjson.loads(raw)

    async def post_api_v5_trade_batch_orders(
            self,
            inst_id: str,
            td_mode: str,
            side: Literal["sell", "buy"],
            ord_type: Literal[
                "market", "limit", "post_only", "fok", "ioc", "optimal_limit_ioc", "mmp", "mmp_and_post_only"
            ],
            sz: str,
            **kwargs,
    ):
        """
                Place orders in batches. Maximum 20 orders can be placed per request.
                Request parameters should be passed in the form of an array. Orders will be placed in turn
                https://www.okx.com/docs-v5/en/?python#order-book-trading-trade-post-place-multiple-orders

                {'arg': {'channel': 'orders', 'instType': 'ANY', 'uid': '611800569950521616'}, 'data': [{'instType': 'SWAP', 'instId': 'BTC-USDT-SWAP', 'tgtCcy': '', 'ccy': '', 'ordId': '1993784914940116992', 'clOrdId': '', 'algoClOrdId': '', 'algoId': '', 'tag': '', 'px': '80000', 'sz': '0.1', 'notionalUsd': '80.0128', 'ordType': 'limit', 'side': 'buy', 'posSide': 'long', 'tdMode': 'cross', 'accFillSz': '0', 'fillNotionalUsd': '', 'avgPx': '0', 'state': 'canceled', 'lever': '3', 'pnl': '0', 'feeCcy': 'USDT', 'fee': '0', 'rebateCcy': 'USDT', 'rebate': '0', 'category': 'normal', 'uTime': '1731921825881', 'cTime': '1731921820806', 'source': '', 'reduceOnly': 'false', 'cancelSource': '1', 'quickMgnType': '', 'stpId': '', 'stpMode': 'cancel_maker', 'attachAlgoClOrdId': '', 'lastPx': '91880', 'isTpLimit': 'false', 'slTriggerPx': '', 'slTriggerPxType': '', 'tpOrdPx': '', 'tpTriggerPx': '', 'tpTriggerPxType': '', 'slOrdPx': '', 'fillPx': '', 'tradeId': '', 'fillSz': '0', 'fillTime': '', 'fillPnl': '0', 'fillFee': '0', 'fillFeeCcy': '', 'execType': '', 'fillPxVol': '', 'fillPxUsd': '', 'fillMarkVol': '', 'fillFwdPx': '', 'fillMarkPx': '', 'amendSource': '', 'reqId': '', 'amendResult': '', 'code': '0', 'msg': '', 'pxType': '', 'pxUsd': '', 'pxVol': '', 'linkedAlgoOrd': {'algoId': ''}, 'attachAlgoOrds': []}]}
                """
        endpoint = "/api/v5/trade/batch-orders"
        payload = {
            "instId": inst_id,
            "tdMode": td_mode,
            "side": side,
            "ordType": ord_type,
            "sz": sz,
            **kwargs,
        }
        raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def post_api_v5_trade_cancel_batch_orders(
            self,
            body: list[dict[str, str]],
    ):
        """
        Cancel multiple orders in batches
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-post-cancel-multiple-orders
        """
        endpoint = "/api/v5/trade/cancel-batch-orders"

        raw = await self._fetch("POST", endpoint, payload=body, signed=True)
        return orjson.loads(raw)

    async def post_api_v5_trade_amend_order(
            self,
            inst_id: str,
            **kwargs,
    ):
        """
        Modify an existing order
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-post-amend-order
        """
        endpoint = "/api/v5/trade/amend-order"
        payload = {
            "instId": inst_id,
            **kwargs,
        }
        raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def post_api_v5_trade_amend_batch_orders(
            self,
            body: list[dict[str, str]],
    ):
        """
        Modify multiple orders in batches
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-post-amend-multiple-orders
        """
        endpoint = "/api/v5/trade/amend-batch-orders"

        raw = await self._fetch("POST", endpoint, payload=body, signed=True)
        return orjson.loads(raw)

    async def post_api_v5_trade_close_position(
            self,
            inst_id: str,
            mgn_mode: Literal["cross", "isolated"],
            **kwargs,
    ):
        """
        Close the position of an instrument via a market order
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-post-close-positions
        """
        endpoint = "/api/v5/trade/close-position"
        payload = {
            "instId": inst_id,
            "mgnMode": mgn_mode,
            **kwargs,
        }
        raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def get_api_v5_trade_order(
            self,
            inst_id: str,
            ord_id: str | None = None,
            cl_ord_id: str | None = None,
    ):
        """
        Retrieve order details.
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-get-order-details
        """
        endpoint = "/api/v5/trade/order"
        payload = {"instId": inst_id}
        if ord_id:
            payload["ordId"] = ord_id
        if cl_ord_id:
            payload["clOrdId"] = cl_ord_id

        raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def get_api_v5_trade_orders_pending(
            self,
            **kwargs,
    ):
        """
        Retrieve all incomplete orders under the current account.
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-get-order-list
        """
        endpoint = "/api/v5/trade/orders-pending"
        payload = {
            **kwargs,
        }

        raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def get_api_v5_trade_orders_history(
            self,
            inst_type: Literal["SPOT", "MARGIN", "SWAP", "FUTURES", "OPTION"],
            **kwargs,
    ):
        """
        Get completed orders which are placed in the last 7 days, including those placed 7 days ago but completed in the last 7 days.
        The incomplete orders that have been canceled are only reserved for 2 hours.
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-get-order-history-last-7-days
        """
        endpoint = "/api/v5/trade/orders-history"
        payload = {
            "instType": inst_type,
            **kwargs,
        }

        raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def get_api_v5_trade_orders_history_archive(
            self,
            inst_type: Literal["SPOT", "MARGIN", "SWAP", "FUTURES", "OPTION"],
            **kwargs,
    ):
        """
        Get completed orders which are placed 7 days ago or earlier.
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-get-order-history-last-3-months
        """
        endpoint = "/api/v5/trade/orders-history-archive"
        payload = {
            "instType": inst_type,
            **kwargs,
        }

        raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def get_api_v5_trade_fills(
            self,
            **kwargs,
    ):
        """
        Retrieve recently-filled transaction details in the last 3 day.
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-get-transaction-details-last-3-days
        """
        endpoint = "/api/v5/trade/fills"
        payload = {
            **kwargs,
        }

        raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def get_api_v5_trade_fills_history(
            self,
            inst_type: Literal["SPOT", "MARGIN", "SWAP", "FUTURES", "OPTION"],
            **kwargs,
    ):
        """
        Retrieve recently-filled transaction details in the last 3 months.
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-get-transaction-details-last-3-months
        """
        endpoint = "/api/v5/trade/fills-history"
        payload = {
            "instType": inst_type,
            **kwargs,
        }

        raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def get_api_v5_trade_easy_convert_currency_list(
            self,
            **kwargs,
    ):
        """
        Get list of small convertibles and mainstream currencies. Only applicable to the crypto balance less than $10.
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-get-easy-convert-currency-list
        """
        endpoint = "/api/v5/trade/easy-convert-currency-list"
        payload = {
            **kwargs,
        }

        raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def post_api_v5_trade_easy_convert(
            self,
            from_ccy: list[str],
            to_ccy: str,
            source: str = "1",
    ):
        """
        Convert small currencies to mainstream currencies.
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-post-place-easy-convert
        """
        endpoint = "/api/v5/trade/easy-convert"
        payload = {
            "fromCcy": from_ccy,
            "toCcy": to_ccy,
            "source": source,
        }
        raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def get_api_v5_trade_easy_convert_history(
            self,
            **kwargs,
    ):
        """
        Get the history and status of easy convert trades in the past 7 days.
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-get-easy-convert-history
        """
        endpoint = "/api/v5/trade/easy-convert-history"
        payload = {
            **kwargs,
        }

        raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def get_api_v5_trade_one_click_repay_currency_list(
            self,
            **kwargs,
    ):
        """
        Get list of debt currency data and repay currencies. Debt currencies include both cross and isolated debts.
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-get-one-click-repay-currency-list
        """
        endpoint = "/api/v5/trade/one-click-repay-currency-list"
        payload = {
            **kwargs,
        }

        raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def post_api_v5_trade_one_click_repay(
            self,
            debt_ccy: list[str],
            repay_ccy: str,
    ):
        """
        Trade one-click repay to repay cross debts. Isolated debts are not applicable. The maximum repayment amount is based on the remaining available balance of funding and trading accounts.
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-post-trade-one-click-repay
        """
        endpoint = "/api/v5/trade/one-click-repay"
        payload = {
            "debtCcy": debt_ccy,
            "repayCcy": repay_ccy,
        }
        raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def get_api_v5_trade_one_click_repay_history(
            self,
            **kwargs,
    ):
        """
        Get the history and status of one-click repay trades in the past 7 days.
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-get-one-click-repay-history
        """
        endpoint = "/api/v5/trade/one-click-repay-history"
        payload = {
            **kwargs,
        }

        raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def post_api_v5_trade_mass_cancel(
            self,
            inst_type: str,
            inst_family: str,
            **kwargs,
    ):
        """
        Cancel all the MMP pending orders of an instrument family.
        Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-post-mass-cancel-order
        """
        endpoint = "/api/v5/trade/mass-cancel"
        payload = {
            "instType": inst_type,
            "instFamily": inst_family,
            **kwargs,
        }
        raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def post_api_v5_trade_cancel_all_after(
            self,
            time_out: str,
            **kwargs,
    ):
        """
        Cancel all pending orders after the countdown timeout. Applicable to all trading symbols through order book (except Spread trading)
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-post-cancel-all-after
        """
        endpoint = "/api/v5/trade/cancel-all-after"
        payload = {
            "timeOut": time_out,
            **kwargs,
        }
        raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)

    async def get_api_v5_trade_account_rate_limit(self):
        """
        Get account rate limit related information.
        Only new order requests and amendment order requests will be counted towards this limit. For batch order requests consisting of multiple orders, each order will be counted individually.
        For details, please refer to Fill ratio based sub-account rate limit
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-get-account-rate-limit
        """
        endpoint = "/api/v5/trade/account-rate-limit"
        raw = await self._fetch("GET", endpoint, signed=True)
        return orjson.loads(raw)

    # POST /api/v5/trade/order-precheck
    async def post_api_v5_trade_order_precheck(
            self,
            inst_id: str,
            td_mode: str,
            side: str,
            ord_type: str,
            sz: str,
            **kwargs,
    ):
        """
        This endpoint is used to precheck the account information before and after placing the order.
        Only applicable to Multi-currency margin mode, and Portfolio margin mode.
        https://www.okx.com/docs-v5/en/?shell#order-book-trading-trade-post-order-precheck
        """
        endpoint = "/api/v5/trade/order-precheck"
        payload = {
            "instId": inst_id,
            "tdMode": td_mode,
            "side": side,
            "ordType": ord_type,
            "sz": sz,
            **kwargs,
        }
        raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
        return orjson.loads(raw)
