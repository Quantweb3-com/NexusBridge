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


async def get_api_v5_trading_bot_signal_signals(
    self, signal_source_type: Literal["1", "2", "3"], **kwargs
):
    """
    Get signals.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-get-signals
    """
    endpoint = "/api/v5/tradingBot/signal/signals"
    payload = {"signalSourceType": signal_source_type, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_signal_order_algo(
    self,
    signal_chan_id: str,
    lever: str,
    invest_amt: str,
    sub_ord_type: Literal["1", "2", "9"],
    **kwargs,
):
    """
    Create signal bot
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-post-create-signal-bot
    """
    endpoint = "/api/v5/tradingBot/signal/order-algo"
    payload = {
        "signalChanId": signal_chan_id,
        "lever": lever,
        "investAmt": invest_amt,
        "subOrdType": sub_ord_type,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_signal_stop_order_algo(
    self,
    algo_ids: list[str],
):
    """
    Stop signal bot
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-post-cancel-signal-bots
    """
    endpoint = "/api/v5/tradingBot/signal/stop-order-algo"
    payload = []
    for i, algo_id in enumerate(algo_ids):
        payload.append(
            {
                "algoId": algo_id,
            }
        )
    if len(payload) == 0:
        raise ValueError("algo_ids is empty")
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_signal_margin_balance(
    self,
    algo_id: str,
    _type: Literal["add", "reduce"],
    amt: str,
    allow_reinvest: bool = False,
):
    """
    Get signal bot margin balance
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-post-adjust-margin-balance
    """
    endpoint = "/api/v5/tradingBot/signal/margin-balance"
    payload = {
        "algoId": algo_id,
        "type": _type,
        "amt": amt,
        "allowReinvest": allow_reinvest,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_signal_amend_tp_sl(
    self,
    algo_id: str,
    exit_setting_param: dict[str, str],
):
    """
    Amend signal bot take profit and stop loss
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-post-amend-tpsl
    """
    endpoint = "/api/v5/tradingBot/signal/amendTPSL"
    payload = {
        "algoId": algo_id,
        "exitSettingParam": exit_setting_param,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_signal_set_instruments(
    self,
    algo_id: str,
    inst_ids: list[str],
    include_all: bool = False,
):
    """
    Set signal bot instruments
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-post-set-instruments
    """
    endpoint = "/api/v5/tradingBot/signal/set-instruments"
    payload = {
        "algoId": algo_id,
        "instIds": inst_ids,
        "includeAll": include_all,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_signal_orders_algo_details(
    self,
    algo_id: str,
    algo_ord_type: str = "contract",
):
    """
    Get signal bot orders algo details
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-get-signal-bot-order-details
    """
    endpoint = "/api/v5/tradingBot/signal/orders-algo-details"
    payload = {
        "algoId": algo_id,
        "algoOrdType": algo_ord_type,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_signal_orders_algo_pending(
    self, algo_ord_type: str = "contract", **kwargs
):
    """
    Get signal bot orders algo pending
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-get-active-signal-bot
    """
    endpoint = "/api/v5/tradingBot/signal/orders-algo-pending"
    payload = {"algoOrdType": algo_ord_type, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_signal_orders_algo_history(
    self, algo_id: str, algo_ord_type: str = "contract", **kwargs
):
    """
    Get signal bot orders algo history
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-get-signal-bot-history
    """
    endpoint = "/api/v5/tradingBot/signal/orders-algo-history"
    payload = {"algoOrdType": algo_ord_type, "algoId": algo_id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_signal_positions(
    self,
    algo_id: str,
    algo_ord_type: str = "contract",
):
    """
    Get signal bot positions
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-get-signal-bot-order-positions
    """
    endpoint = "/api/v5/tradingBot/signal/positions"
    payload = {
        "algoId": algo_id,
        "algoOrdType": algo_ord_type,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_signal_positions_history(self, algo_id: str, **kwargs):
    """
    Get signal bot positions history
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-get-position-history
    """
    endpoint = "/api/v5/tradingBot/signal/positions-history"
    payload = {"algoId": algo_id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_signal_close_position(
    self,
    algo_id: str,
    inst_id: str,
):
    """
    Close signal bot position
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-post-close-position
    """
    endpoint = "/api/v5/tradingBot/signal/close-position"
    payload = {
        "algoId": algo_id,
        "instId": inst_id,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_signal_sub_order(
    self,
    algo_id: str,
    inst_id: str,
    side: Literal["buy", "sell"],
    ord_type: Literal["market", "limit"],
    sz: str,
    **kwargs,
):
    """
    You can place an order only if you have sufficient funds.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-post-place-sub-order
    """
    endpoint = "/api/v5/tradingBot/signal/sub-order"
    payload = {
        "algoId": algo_id,
        "instId": inst_id,
        "side": side,
        "ordType": ord_type,
        "sz": sz,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_trading_bot_signal_cancel_sub_order(
    self,
    algo_id: str,
    inst_id: str,
    signal_ord_id: str,
):
    """
    Cancel signal bot sub order
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-post-cancel-sub-order
    """
    endpoint = "/api/v5/tradingBot/signal/cancel-sub-order"
    payload = {
        "algoId": algo_id,
        "instId": inst_id,
        "signalOrdId": signal_ord_id,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_signal_sub_orders(
    self, algo_id: str, algo_ord_type: str = "contract", **kwargs
):
    """
    Get signal bot sub orders
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-get-signal-bot-sub-orders
    """
    endpoint = "/api/v5/tradingBot/signal/sub-orders"
    payload = {"algoId": algo_id, "algoOrdType": algo_ord_type, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_trading_bot_signal_event_history(self, algo_id: str, **kwargs):
    """
    Get signal bot event history
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-signal-bot-trading-get-signal-bot-event-history
    """
    endpoint = "/api/v5/tradingBot/signal/event-history"
    payload = {"algoId": algo_id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)
