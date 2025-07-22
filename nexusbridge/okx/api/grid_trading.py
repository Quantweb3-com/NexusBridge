# Grid Trading
# Grid trading works by the simple strategy of buy low and sell high. After you set the parameters, the system automatically places orders at incrementally increasing or decreasing prices. Overall, the grid bot seeks to capitalize on normal price volatility by placing buy and sell orders at certain regular intervals above and below a predefined base price.
# The API endpoints of Grid Trading require authentication.
from typing import Literal

import orjson


async def post_api_v5_trading_bot_grid_order_algo(
    self,
    inst_id: str,
    algo_ord_type: Literal["grid", "contract_grid"],
    max_px: str,
    min_px: str,
    grid_num: str,
    trigger_param: list[dict[str, str]] | None = None,
    base_sz: str | None = None,
    quote_sz: str | None = None,
    **kwargs,
):
    """
    Create a grid strategy order
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-post-place-grid-algo-order
    """
    endpoint = "/api/v5/tradingBot/grid/order-algo"
    payload = {
        "instId": inst_id,
        "algoOrdType": algo_ord_type,
        "maxPx": max_px,
        "minPx": min_px,
        "gridNum": grid_num,
        **kwargs,
    }
    if base_sz:
        payload["baseSz"] = base_sz
    if quote_sz:
        payload["quoteSz"] = quote_sz
    if trigger_param:
        payload["triggerParams"] = trigger_param
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_grid_amend_order_algo(
    self,
    inst_id: str,
    algo_id: str,
    trigger_param: list[dict[str, str]] | None = None,
    **kwargs,
):
    """
    Amend a grid strategy order
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-post-amend-grid-algo-order
    """
    endpoint = "/api/v5/tradingBot/grid/amend-order-algo"
    payload = {
        "instId": inst_id,
        "algoId": algo_id,
        **kwargs,
    }
    if trigger_param:
        payload["triggerParams"] = trigger_param
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_grid_stop_order_algo(
    self,
    payload: list[dict[str, str]],
):
    """
    A maximum of 10 orders can be stopped per request.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-post-stop-grid-algo-order
    """
    endpoint = "/api/v5/tradingBot/grid/stop-order-algo"
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_grid_close_position(
    self, algo_id: str, mkt_close: Literal[True, False], **kwargs
):
    """
    Close position when the contract grid stop type is 'keep position'.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-post-close-position-for-contract-grid
    """
    endpoint = "/api/v5/tradingBot/grid/close-position"
    payload = {
        "algoId": algo_id,
        "mktClose": mkt_close,
        "tag": "f50cdd72d3b6BCDE",
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_grid_cancel_close_order(
    self, algo_id: str, ord_id: str
):
    """
    Cancel close position order for contract grid
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-post-cancel-close-position-order-for-contract-grid
    """
    endpoint = "/api/v5/tradingBot/grid/cancel-close-order"
    payload = {
        "algoId": algo_id,
        "ordId": ord_id,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_grid_order_instant_trigger(
    self,
    algo_id: str,
):
    """
    Place an instant trigger order
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-post-instant-trigger-order
    """
    endpoint = "/api/v5/tradingBot/grid/order-instant-trigger"
    payload = {
        "algoId": algo_id,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_grid_orders_algo_pending(
    self, algo_ord_type: Literal["grid", "contract_grid"], **kwargs
):
    """
    Grid algo order list
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-get-grid-algo-order-list
    """
    endpoint = "/api/v5/tradingBot/grid/orders-algo-pending"
    payload = {
        "algoOrdType": algo_ord_type,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_grid_orders_algo_history(
    self, algo_ord_type: Literal["grid", "contract_grid"], **kwargs
):
    """
    Grid algo order history
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-get-grid-algo-order-history
    """
    endpoint = "/api/v5/tradingBot/grid/orders-algo-history"
    payload = {
        "algoOrdType": algo_ord_type,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_grid_orders_algo_details(
    self,
    algo_id: str,
    algo_ord_type: Literal["grid", "contract_grid"],
):
    """
    Grid algo order details
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-get-grid-algo-order-details
    """
    endpoint = "/api/v5/tradingBot/grid/orders-algo-details"
    payload = {
        "algoId": algo_id,
        "algoOrdType": algo_ord_type,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_grid_sub_orders(
    self,
    algo_id: str,
    algo_ord_type: Literal["grid", "contract_grid"],
    _type: Literal["live", "filled"],
    **kwargs,
):
    """
    Grid algo sub orders
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-get-grid-algo-sub-orders
    """
    endpoint = "/api/v5/tradingBot/grid/sub-orders"
    payload = {
        "algoId": algo_id,
        "algoOrdType": algo_ord_type,
        "type": _type,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_grid_positions(
    self,
    algo_id: str,
    algo_ord_type: Literal["grid", "contract_grid"],
):
    """
    Grid algo order positions
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-get-grid-algo-order-positions
    """
    endpoint = "/api/v5/tradingBot/grid/positions"
    payload = {
        "algoId": algo_id,
        "algoOrdType": algo_ord_type,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_grid_withdraw_income(
    self,
    algo_id: str,
):
    """
    Spot grid withdraw income
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-post-spot-grid-withdraw-income
    """
    endpoint = "/api/v5/tradingBot/grid/withdraw-income"
    payload = {
        "algoId": algo_id,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_grid_compute_margin_balance(
    self,
    algo_id: str,
    _type: Literal["add", "reduce"],
    amt: str | None = None,
):
    """
    Compute margin balance
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-post-compute-margin-balance
    """
    endpoint = "/api/v5/tradingBot/grid/compute-margin-balance"
    payload = {
        "algoId": algo_id,
        "type": _type,
    }
    if amt:
        payload["amt"] = amt

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_grid_margin_balance(
    self,
    algo_id: str,
    _type: Literal["add", "reduce"],
    amt: str | None = None,
    percent: str | None = None,
):
    """
    Adjust margin balance
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-post-adjust-margin-balance
    """
    endpoint = "/api/v5/tradingBot/grid/margin-balance"
    payload = {
        "algoId": algo_id,
        "type": _type,
    }
    if amt:
        payload["amt"] = amt
    if percent:
        payload["percent"] = percent
    if not amt and not percent:
        raise ValueError("amt or percent must be provided")
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_grid_adjust_investment(
    self,
    algo_id: str,
    amt: str,
):
    """
    It is used to add investment and only applicable to contract gird.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-post-add-investment
    """
    endpoint = "/api/v5/tradingBot/grid/adjust-investment"
    payload = {
        "algoId": algo_id,
        "amt": amt,
    }

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_grid_ai_param(
    self, algo_ord_type: Literal["grid", "contract_grid"], inst_id: str, **kwargs
):
    """
    Get grid AI parameters
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-get-grid-ai-parameter-public
    """
    endpoint = "/api/v5/tradingBot/grid/ai-param"
    payload = {
        "algoOrdType": algo_ord_type,
        "instId": inst_id,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_grid_min_investment(
    self,
    inst_id: str,
    algo_ord_type: Literal["grid", "contract_grid"],
    max_px: str,
    min_px: str,
    grid_num: str,
    run_type: Literal["1", "2"],
    investment_data: list[dict[str, str]] | None = None,
    **kwargs,
):
    """
    Compute the minimum investment
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-post-compute-min-investment-public
    """
    endpoint = "/api/v5/tradingBot/grid/min-investment"
    payload = {
        "instId": inst_id,
        "algoOrdType": algo_ord_type,
        "maxPx": max_px,
        "minPx": min_px,
        "gridNum": grid_num,
        "runType": run_type,
        **kwargs,
    }
    if investment_data:
        payload["investmentData"] = investment_data
    raw = await self._fetch("POST", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_rsi_back_testing(
    self, inst_id: str, timeframe: str, thold: str, time_period: str, **kwargs
):
    """
    RSI back testing (public)
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-get-rsi-back-testing-public
    """
    endpoint = "/api/v5/tradingBot/public/rsi-back-testing"
    payload = {
        "instId": inst_id,
        "timeframe": timeframe,
        "thold": thold,
        "timePeriod": time_period,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_grid_quantity(
    self,
    inst_id: str,
    run_type: Literal["1", "2"],
    algo_ord_type: Literal["grid", "contract_grid"],
    max_px: str,
    min_px: str,
    lever: str | None = None,
):
    """
    Get grid quantity
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-grid-trading-get-max-grid-quantity-public
    """
    endpoint = "/api/v5/tradingBot/grid/grid-quantity"
    payload = {
        "instId": inst_id,
        "runType": run_type,
        "algoOrdType": algo_ord_type,
        "maxPx": max_px,
        "minPx": min_px,
    }

    if algo_ord_type == "contract_grid":
        if not lever:
            raise ValueError("lever must be provided")
        payload["lever"] = lever
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)
