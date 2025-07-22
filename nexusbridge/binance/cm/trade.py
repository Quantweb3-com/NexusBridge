import json
from typing import Literal

from nexusbridge.binance.constants import Side, OrderType


async def post_dapi_v1_order(self, symbol: str, side: Side, _type: OrderType, **kwargs):
    """

    Send in a new order.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade
    """
    endpoint = "/dapi/v1/order"
    payload = {"symbol": symbol, "side": side.value, "type": _type.value, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_dapi_v1_batch_order(self, batch_orders: list[dict], **kwargs):
    """
    Place Multiple Orders
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Place-Multiple-Orders
    """
    endpoint = "/dapi/v1/batchOrders"
    payload = {"batchOrders": json.dumps(batch_orders), **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def put_dapi_v1_order(self, symbol: str, side: Side, **kwargs):
    """
    Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Modify-Order
    """
    endpoint = "/dapi/v1/order"
    payload = {"symbol": symbol, "side": side.value, **kwargs}
    raw = await self._fetch("PUT", endpoint, payload=payload, signed=True)
    return raw


async def put_dapi_v1_batch_order(self, batch_orders: list[dict], **kwargs):
    """
    Modify Multiple Orders
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Modify-Multiple-Orders
    """
    endpoint = "/dapi/v1/batchOrders"
    payload = {"batchOrders": json.dumps(batch_orders), **kwargs}
    raw = await self._fetch("PUT", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_order_amendment(self, symbol: str, **kwargs):
    """
    Get order modification history
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Get-Order-Modify-History
    """
    endpoint = "/dapi/v1/orderAmendment"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def delete_dapi_v1_order(self, symbol: str, **kwargs):
    """
    Cancel an active order.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Order
    """
    endpoint = "/dapi/v1/order"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_dapi_v1_batch_order(
    self,
    symbol: str,
    order_id_list: list[int] | None = None,
    orig_client_order_id_list: list[int] | None = None,
    **kwargs,
):
    """
    Cancel Multiple Orders
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Cancel-Multiple-Orders
    """
    endpoint = "/dapi/v1/batchOrders"
    payload = {"symbol": symbol, **kwargs}
    if order_id_list:
        payload["orderIdList"] = json.dumps(order_id_list)
    if orig_client_order_id_list:
        payload["origClientOrderIdList"] = json.dumps(orig_client_order_id_list)
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_dapi_v1_all_open_orders(self, symbol: str, **kwargs):
    """
    Cancel All Open Orders
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Cancel-All-Open-Orders
    """
    endpoint = "/dapi/v1/allOpenOrders"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def post_dapi_v1_countdown_cancel_all(
    self, symbol: str, countdown_time: int, **kwargs
):
    """
    Cancel all open orders of the specified symbol at the end of the specified countdown. This rest endpoint means to ensure your open orders are canceled in case of an outage. The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and repalced by a new one. The system will check all countdowns approximately every 10 milliseconds, so please note that sufficient redundancy should be considered when using this function. We do not recommend setting the countdown time to be too precise or too small.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Auto-Cancel-All-Open-Orders
    """
    endpoint = "/dapi/v1/countdownCancelAll"
    payload = {"symbol": symbol, "countdownTime": countdown_time, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_order(self, symbol: str, **kwargs):
    """
    Check an order's status.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Query-Order
    """
    endpoint = "/dapi/v1/order"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_all_orders(self, symbol: str, **kwargs):
    """
    Get all account orders; active, canceled, or filled.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/All-Orders
    """
    endpoint = "/dapi/v1/allOrders"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_open_orders(self, **kwargs):
    """
    Get all open orders on a symbol.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Current-All-Open-Orders
    """
    endpoint = "/dapi/v1/openOrders"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_open_order(self, symbol: str, **kwargs):
    """
    Query open order
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Query-Current-Open-Order
    """
    endpoint = "/dapi/v1/openOrder"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_force_orders(self, **kwargs):
    """
    Query user's Force Orders
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Users-Force-Orders
    """
    endpoint = "/dapi/v1/forceOrders"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_user_trades(self, symbol: str, **kwargs):
    """
    Get trades for a specific account and symbol.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Account-Trade-List
    """
    endpoint = "/dapi/v1/userTrades"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_position_risk(self, **kwargs):
    """
    Get current account information.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Position-Information
    """
    endpoint = "/dapi/v1/positionRisk"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def post_dapi_v1_position_side_dual(
    self, dual_side_position: Literal["true", "false"], **kwargs
):
    """
    Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Change-Position-Mode#request-weight
    """
    endpoint = "/dapi/v1/positionSide/dual"
    payload = {"dualSidePosition": dual_side_position, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_dapi_v1_margin_type(
    self, symbol: str, margin_type: Literal["ISOLATED", "CROSSED"], **kwargs
):
    """
    Change user's margin type in the specific symbol market.For Hedge Mode, LONG and SHORT positions of one symbol use the same margin type.
    With ISOLATED margin type, margins of the LONG and SHORT positions are isolated from each other.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Change-Margin-Type
    """
    endpoint = "/dapi/v1/marginType"
    payload = {"symbol": symbol, "marginType": margin_type, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_dapi_v1_leverage(self, symbol: str, leverage: int, **kwargs):
    """
    Change user's initial leverage in the specific symbol market.
    For Hedge Mode, LONG and SHORT positions of one symbol use the same initial leverage and share a total notional value.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Change-Initial-Leverage
    """
    endpoint = "/dapi/v1/leverage"
    payload = {"symbol": symbol, "leverage": leverage, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_adl_quantile(self, **kwargs):
    """
    Query position ADL quantile estimation
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Position-ADL-Quantile-Estimation
    """
    endpoint = "/dapi/v1/adlQuantile"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def post_dapi_v1_position_margin(
    self, symbol: str, amount: float, _type: Literal[1, 2], **kwargs
):
    """
    Modify Isolated Position Margin
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Modify-Isolated-Position-Margin
    """
    endpoint = "/dapi/v1/positionMargin"
    payload = {"symbol": symbol, "amount": amount, "type": _type, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_position_margin_history(self, symbol: str, **kwargs):
    """
    Get position margin change history
    https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/Get-Position-Margin-Change-History
    """
    endpoint = "/dapi/v1/positionMargin/history"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw
