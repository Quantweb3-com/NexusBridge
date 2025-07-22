from typing import Literal

import orjson


async def post_api_v5_trading_bot_signal_create_signal(
    self,
    signal_chan_name: str,
    signal_chan_desc: str | None = None,
):
    """
    Create a signal.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading
    """
    endpoint = "/api/v5/tradingBot/signal/create-signal"
    payload = {
        "signalChanName": signal_chan_name,
    }
    if signal_chan_desc:
        payload["signalChanDesc"] = signal_chan_desc
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


# POST /api/v5/tradingBot/recurring/order-algo
async def post_api_v5_trading_bot_recurring_order_algo(
    self,
    stgy_name: str,
    recurring_list: list[dict[str, str]],
    period: Literal["monthly", "weekly", "daily", "hourly"],
    recurring_time: str,
    time_zone: str,
    amt: str,
    investment_ccy: str,
    td_mode: Literal["cross", "cash"],
    **kwargs,
):
    """
    Create a recurring order algo.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-recurring-buy-post-place-recurring-buy-order
    """
    endpoint = "/api/v5/tradingBot/recurring/order-algo"
    payload = {
        "stgyName": stgy_name,
        "recurringList": recurring_list,
        "period": period,
        "recurringTime": recurring_time,
        "timeZone": time_zone,
        "amt": amt,
        "investmentCcy": investment_ccy,
        "tdMode": td_mode,
        **kwargs,
    }

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_recurring_amend_order_algo(
    self,
    algo_id: str,
    stgy_name: str,
):
    """
    Amend recurring buy order
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-recurring-buy-post-amend-recurring-buy-order
    """
    endpoint = "/api/v5/tradingBot/recurring/amend-order-algo"
    payload = {
        "algoId": algo_id,
        "stgyName": stgy_name,
    }

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_recurring_stop_order_algo(
    self,
    algo_id: list[str],
):
    """
    Stop recurring buy order
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-recurring-buy-post-stop-recurring-buy-order
    """
    endpoint = "/api/v5/tradingBot/recurring/stop-order-algo"
    payload = []
    for algo in algo_id:
        payload.append({"algoId": algo})

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_recurring_orders_algo_pending(self, **kwargs):
    """
    Get pending recurring orders
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-recurring-buy-get-recurring-buy-order-list
    """
    endpoint = "/api/v5/tradingBot/recurring/orders-algo-pending"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_recurring_orders_algo_history(self, **kwargs):
    """
    Get historical recurring orders
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-recurring-buy-get-recurring-buy-order-history
    """
    endpoint = "/api/v5/tradingBot/recurring/orders-algo-history"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_recurring_orders_algo_details(self, algo_id: str):
    """
    Get recurring order details
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-recurring-buy-get-recurring-buy-order-details
    """
    endpoint = "/api/v5/tradingBot/recurring/orders-algo-details"
    payload = {"algoId": algo_id}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_recurring_sub_orders(self, algo_id: str, **kwargs):
    """
    Get recurring sub orders
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-recurring-buy-get-recurring-buy-sub-orders
    """
    endpoint = "/api/v5/tradingBot/recurring/sub-orders"
    payload = {"algoId": algo_id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)
