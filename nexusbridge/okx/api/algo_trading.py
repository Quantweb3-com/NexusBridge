import orjson


async def post_api_v5_trade_order_algo(
    self,
    inst_id: str,
    td_mode: str,
    side: str,
    ord_type: str,
    **kwargs,
):
    """
    The algo order includes trigger order, oco order, chase order, conditional order, twap order and trailing order.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-algo-trading-post-place-algo-order
    """
    endpoint = "/api/v5/trade/order-algo"
    payload = {
        "instId": inst_id,
        "tdMode": td_mode,
        "side": side,
        "ordType": ord_type,
        "tag": "f50cdd72d3b6BCDE",
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trade_cancel_algos(self, payload: list[dict[str, str]]):
    """
    Cancel unfilled algo orders. A maximum of 10 orders can be canceled per request. Request parameters should be passed in the form of an array.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-algo-trading-post-cancel-algo-order
    """
    endpoint = "/api/v5/trade/cancel-algos"
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trade_amend_algos(
    self,
    algo_id: str | None = None,
    cl_algo_id: str | None = None,
    **kwargs,
):
    """
    Amend unfilled algo orders (Support Stop order and Trigger order only, not including Move_order_stop order, Iceberg order, TWAP order, Trailing Stop order).
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-algo-trading-post-amend-algo-order
    """
    endpoint = "/api/v5/trade/amend-algos"
    payload = {
        **kwargs,
    }
    if algo_id:
        payload["algoId"] = algo_id
    if cl_algo_id:
        payload["algoClOrdId"] = cl_algo_id
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trade_cancel_advance_algos(self, payload: list[dict[str, str]]):
    """
    This endpoint will be offline soon, please use Cancel algo order
    Cancel unfilled algo orders (including Iceberg order, TWAP order, Trailing Stop order). A maximum of 10 orders can be canceled per request. Request parameters should be passed in the form of an array.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-algo-trading-post-cancel-advance-algo-order
    """
    endpoint = "/api/v5/trade/cancel-advance-algos"
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trade_order_algo(
    self,
    algo_id: str | None = None,
    algo_cl_ord_id: str | None = None,
):
    """
    Retrieve the details of an algo order.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-algo-trading-post-cancel-advance-algo-order
    """
    endpoint = "/api/v5/trade/order-algo"
    payload = {}
    if algo_id:
        payload["algoId"] = algo_id
    if algo_cl_ord_id:
        payload["algoClOrdId"] = algo_cl_ord_id

    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trade_orders_algo_pending(self, ord_type: str, **kwargs):
    """
    Retrieve all incomplete algo orders under the current account.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-algo-trading-get-algo-order-list
    """
    endpoint = "/api/v5/trade/orders-algo-pending"
    payload = {
        "ordType": ord_type,
        **kwargs,
    }

    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trade_orders_algo_history(
    self,
    ord_type: str,
    state: str | None = None,
    algo_id: str | None = None,
    **kwargs,
):
    """
    Retrieve a list of all algo orders under the current account in the last 3 months.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-algo-trading-get-algo-order-history
    """
    endpoint = "/api/v5/trade/orders-algo-history"
    payload = {
        "ordType": ord_type,
        **kwargs,
    }
    if state:
        payload["state"] = state
    if algo_id:
        payload["algoId"] = algo_id

    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_grid_order_algo(
    self,
    inst_id: str,
    td_mode: str,
    side: str,
    ord_type: str,
    sz: str,
    **kwargs,
):
    """
    Place a new grid order
    https://www.okx.com/docs-v5/en/?shell#trading-bot-grid-trading-post-place-grid-order
    """
    endpoint = "/api/v5/tradingBot/grid/order-algo"
    payload = {
        "instId": inst_id,
        "tdMode": td_mode,
        "side": side,
        "ordType": ord_type,
        "sz": sz,
        "tag": "f50cdd72d3b6BCDE",
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)
