import json
from typing import Literal

from nexusbridge.binance.constants import OrderType, Side


async def post_fapi_v1_order(self, symbol: str, side: Side, _type: OrderType, **kwargs):
    """
    Send in a new order.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api
    """
    endpoint = "/fapi/v1/order"
    payload = {"symbol": symbol, "side": side.value, "type": _type.value, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_fapi_v1_batch_order(self, batch_orders: list[dict], **kwargs):
    """
    Place Multiple Orders
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Place-Multiple-Orders
    """
    endpoint = "/fapi/v1/batchOrders"
    payload = {"batchOrders": json.dumps(batch_orders), **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def put_fapi_v1_order(
    self, symbol: str, side: Side, quantity: float, price: float, **kwargs
):
    """
    Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Order
    """
    endpoint = "/fapi/v1/order"
    payload = {
        "symbol": symbol,
        "side": side.value,
        "quantity": quantity,
        "price": price,
        **kwargs,
    }
    raw = await self._fetch("PUT", endpoint, payload=payload, signed=True)
    return raw


async def put_fapi_v1_batch_order(self, batch_orders: list[dict], **kwargs):
    """
    Modify Multiple Orders (TRADE)
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Multiple-Orders
    """
    endpoint = "/fapi/v1/batchOrders"
    payload = {"batchOrders": json.dumps(batch_orders), **kwargs}
    raw = await self._fetch("PUT", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_order_amendment(self, symbol: str, **kwargs):
    """
    Get order modification history
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Order-Modify-History
    """
    endpoint = "/fapi/v1/orderAmendment"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def delete_fapi_v1_order(self, symbol: str, **kwargs):
    """
    Cancel an active order.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Order
    """
    endpoint = "/fapi/v1/order"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_fapi_v1_batch_order(
    self,
    symbol: str,
    order_id_list: list[int] | None = None,
    orig_client_order_id_list: list[int] | None = None,
    **kwargs,
):
    """
    Cancel Multiple Orders
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders#request-parameters
    """
    endpoint = "/fapi/v1/batchOrders"
    payload = {"symbol": symbol, **kwargs}
    if order_id_list:
        payload["orderIdList"] = json.dumps(order_id_list)
    if orig_client_order_id_list:
        payload["origClientOrderIdList"] = json.dumps(orig_client_order_id_list)
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_fapi_v1_all_open_orders(self, symbol: str, **kwargs):
    """
    Cancel All Open Orders
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders
    """
    endpoint = "/fapi/v1/allOpenOrders"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def post_fapi_v1_countdown_cancel_all(
    self, symbol: str, countdown_time: int, **kwargs
):
    """
    Cancel all open orders of the specified symbol at the end of the specified countdown. The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and replaced by a new one.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Auto-Cancel-All-Open-Orders
    """
    endpoint = "/fapi/v1/countdownCancelAll"
    payload = {"symbol": symbol, "countdownTime": countdown_time, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_order(self, symbol: str, **kwargs):
    """
    Check an order's status.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Order
    """
    endpoint = "/fapi/v1/order"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_all_orders(self, symbol: str, **kwargs):
    """
    Get all account orders; active, canceled, or filled.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/All-Orders
    """
    endpoint = "/fapi/v1/allOrders"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_open_orders(self, **kwargs):
    """
    Get all open orders on a symbol.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Current-All-Open-Orders
    """
    endpoint = "/fapi/v1/openOrders"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_open_order(self, symbol: str, **kwargs):
    """
    Query open order
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Current-Open-Order
    """
    endpoint = "/fapi/v1/openOrder"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_force_orders(self, **kwargs):
    """
    Query user's Force Orders
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders
    """
    endpoint = "/fapi/v1/forceOrders"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_user_trades(self, symbol: str, **kwargs):
    """
    Get trades for a specific account and symbol.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List
    """
    endpoint = "/fapi/v1/userTrades"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def post_fapi_v1_margin_type(
    self, symbol: str, margin_type: Literal["ISOLATED", "CROSSED"], **kwargs
):
    """
    Change symbol level margin type
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type
    """
    endpoint = "/fapi/v1/marginType"
    payload = {"symbol": symbol, "marginType": margin_type, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_fapi_v1_position_side_dual(
    self, dual_side_position: Literal["BOTH", "LONG", "SHORT"], **kwargs
):
    """
    Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Position-Mode
    """
    endpoint = "/fapi/v1/positionSide/dual"
    payload = {"dualSidePosition": dual_side_position, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_fapi_v1_leverage(self, symbol: str, leverage: int, **kwargs):
    """
    Change user's initial leverage of specific symbol market.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage
    """
    endpoint = "/fapi/v1/leverage"
    payload = {"symbol": symbol, "leverage": leverage, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_fapi_v1_multi_assets_margin(self, multi_assets_margin: str, **kwargs):
    """
    Change user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode
    """
    endpoint = "/fapi/v1/multiAssetsMargin"
    payload = {"multiAssetsMargin": multi_assets_margin, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_fapi_v1_position_margin(
    self, symbol: str, amount: float, _type: Literal[1, 2], **kwargs
):
    """
    Modify Isolated Position Margin
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin
    """
    endpoint = "/fapi/v1/positionMargin"
    payload = {"symbol": symbol, "amount": amount, "type": _type, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v2_position_risk(self, **kwargs):
    """
    Get current position information.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V2
    """
    endpoint = "/fapi/v2/positionRisk"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v3_position_risk(self, **kwargs):
    """
    Get current position information(only symbol that has position or open orders will be returned).
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V3
    """
    endpoint = "/fapi/v3/positionRisk"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_adl_quantile(self, **kwargs):
    """
    Position ADL Quantile Estimation
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation
    """
    endpoint = "/fapi/v1/adlQuantile"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_position_margin_history(self, symbol: str, **kwargs):
    """
    Get position margin change history
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History
    """
    endpoint = "/fapi/v1/positionMargin/history"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def post_fapi_v1_order_test(
    self, symbol: str, side: Side, _type: OrderType, **kwargs
):
    """
    Testing order request, this order will not be submitted to matching engine
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/New-Order-Test
    """
    endpoint = "/fapi/v1/order/test"
    payload = {"symbol": symbol, "side": side.value, "type": _type.value, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw
