from typing import Literal

from nexusbridge.binance.constants import Side, OrderType


async def post_api_v3_order(self, symbol: str, side: Side, _type: OrderType, **kwargs):
    """
    Send in a new order.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints
    """
    endpoint = "/api/v3/order"
    payload = {"symbol": symbol, "side": side.value, "type": _type.value, **kwargs}

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_api_v3_order_test(
    self,
    symbol: str,
    side: Side,
    _type: OrderType,
    compute_commission_rates: bool = False,
    **kwargs,
):
    """
    Test new order creation and signature/recvWindow long. Creates and validates a new order but does not send it into the matching engine.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#test-new-order-trade
    """
    endpoint = "/api/v3/order/test"
    payload = {
        "computeCommissionRates": compute_commission_rates,
        "symbol": symbol,
        "side": side.value,
        "type": _type.value,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def get_api_v3_order(self, symbol: str, **kwargs):
    """
    Check an order's status.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#query-order-user_data
    """
    endpoint = "/api/v3/order"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def delete_api_v3_order(self, symbol: str, **kwargs):
    """
    Cancel an active order.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#cancel-order-trade
    """
    endpoint = "/api/v3/order"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_api_v3_open_orders(self, symbol: str, **kwargs):
    """
    Cancels all active orders on a symbol. This includes orders that are part of an order list.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#cancel-all-open-orders-on-a-symbol-trade
    """
    endpoint = "/api/v3/openOrders"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def post_api_v3_order_cancel_replace(
    self,
    symbol: str,
    side: Side,
    _type: OrderType,
    cancel_replace_mode: Literal["STOP_ON_FAILURE", "ALLOW_FAILURE"],
    **kwargs,
):
    """
    Cancels an existing order and places a new order on the same symbol.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#cancel-an-existing-order-and-send-a-new-order-trade
    """
    endpoint = "/api/v3/order/cancelReplace"
    payload = {
        "symbol": symbol,
        "side": side.value,
        "type": _type.value,
        "cancelReplaceMode": cancel_replace_mode,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def get_api_v3_open_orders(self, symbol: str, **kwargs):
    """
    Get all open orders on a symbol. Careful when accessing this with no symbol.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#current-open-orders-user_data
    """
    endpoint = "/api/v3/openOrders"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_api_v3_all_orders(self, symbol: str, **kwargs):
    """
    Get all account orders; active, canceled, or filled.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#all-orders-user_data
    """
    endpoint = "/api/v3/allOrders"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def post_api_v3_order_oco(
    self,
    symbol: str,
    side: Side,
    quantity: float,
    price: float,
    stop_price: float,
    **kwargs,
):
    """
    Post an OCO order
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#order-lists
    """
    endpoint = "/api/v3/order/oco"
    payload = {
        "symbol": symbol,
        "side": side.value,
        "quantity": quantity,
        "price": price,
        "stopPrice": stop_price,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_api_v3_sor_order(
    self, symbol: str, side: Side, _type: OrderType, quantity: float, **kwargs
):
    """
    Places an order using smart order routing (SOR).
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#sor
    """
    endpoint = "/api/v3/sor/order"
    payload = {
        "symbol": symbol,
        "side": side.value,
        "type": _type.value,
        "quantity": quantity,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw
