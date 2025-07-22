import orjson
from typing import Any, Dict, Callable, Literal


async def post_v5_order_create(
    self,
    category: Literal["linear", "inverse", "spot", "option"],
    symbol: str,
    side: Literal["Buy", "Sell"],
    order_type: Literal["Market", "Limit"],
    qty: str,
    **kwargs,
):
    """
    This endpoint supports to create the order for Spot, Margin trading, USDT perpetual, USDC perpetual, USDC futures, Inverse Futures and Options.
    https://bybit-exchange.github.io/docs/v5/order/create-order
    """
    endpoint = "/v5/order/create"
    payload = {
        "category": category,
        "symbol": symbol,
        "side": side,
        "orderType": order_type,
        "qty": qty,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_order_amend(
    self,
    category: Literal["linear", "inverse", "spot", "option"],
    symbol: str,
    **kwargs,
):
    """
    Amend Order
    https://bybit-exchange.github.io/docs/v5/order/amend-order
    """
    endpoint = "/v5/order/amend"
    payload = {
        "category": category,
        "symbol": symbol,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_order_cancel(
    self,
    category: Literal["linear", "inverse", "spot", "option"],
    symbol: str,
    **kwargs,
):
    """
    Cancel Order
    https://bybit-exchange.github.io/docs/v5/order/cancel-order
    """
    endpoint = "/v5/order/cancel"
    payload = {
        "category": category,
        "symbol": symbol,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def get_v5_order_realtime(
    self, category: Literal["linear", "inverse", "spot", "option"], **kwargs
):
    """
    Get Open & Closed Orders
    https://bybit-exchange.github.io/docs/v5/order/open-order
    """
    endpoint = "/v5/order/realtime"
    payload = {
        "category": category,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_order_cancel_all(
    self, category: Literal["linear", "inverse", "spot", "option"], **kwargs
):
    """
    Cancel All Orders
    https://bybit-exchange.github.io/docs/v5/order/cancel-all
    """
    endpoint = "/v5/order/cancel-all"
    payload = {
        "category": category,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def get_v5_order_history(
    self, category: Literal["linear", "inverse", "spot", "option"], **kwargs
):
    """
    Get Order History
    https://bybit-exchange.github.io/docs/v5/order/order-list
    """
    endpoint = "/v5/order/history"
    payload = {
        "category": category,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def get_v5_execution_list(
    self, category: Literal["linear", "inverse", "spot", "option"], **kwargs
):
    """
    Get Trade History
    https://bybit-exchange.github.io/docs/v5/order/execution
    """
    endpoint = "/v5/execution/list"
    payload = {
        "category": category,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_order_create_batch(
    self,
    category: Literal["linear", "inverse", "spot", "option"],
    request: list[Dict[str, Any]],
):
    """
    Batch Place Order
    https://bybit-exchange.github.io/docs/v5/order/batch-place
    """
    endpoint = "/v5/order/create-batch"
    payload = {
        "category": category,
        "request": request,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_order_amend_batch(
    self,
    category: Literal["linear", "inverse", "spot", "option"],
    request: list[Dict[str, Any]],
):
    """
    Batch Amend Order
    https://bybit-exchange.github.io/docs/v5/order/batch-amend
    """
    endpoint = "/v5/order/amend-batch"
    payload = {
        "category": category,
        "request": request,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_order_cancel_batch(
    self,
    category: Literal["linear", "inverse", "spot", "option"],
    request: list[Dict[str, Any]],
):
    """
    Batch Cancel Order
    https://bybit-exchange.github.io/docs/v5/order/batch-cancel
    """
    endpoint = "/v5/order/cancel-batch"
    payload = {
        "category": category,
        "request": request,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def get_v5_order_spot_borrow_check(
    self,
    symbol: str,
    side: Literal["buy", "sell"],
    category: str = "spot",
):
    """
    Get Borrow Quota (Spot)
    https://bybit-exchange.github.io/docs/v5/order/spot-borrow-quota
    """
    endpoint = "/v5/order/spot-borrow-check"
    payload = {
        "symbol": symbol,
        "side": side,
        "category": category,
    }
    raw = await self._fetch("GET", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_order_disconnected_cancel_all(
    self,
    time_window: int,
    product: Literal["OPTIONS", "DERIVATIVES", "SPOT"] = "OPTIONS",
):
    """
    Set Disconnect Cancel All
    https://bybit-exchange.github.io/docs/v5/order/dcp
    """
    endpoint = "/v5/order/disconnected-cancel-all"
    payload = {
        "timeWindow": time_window,
        "product": product,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)
