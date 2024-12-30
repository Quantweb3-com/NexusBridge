import orjson
from typing import Any, Dict, Callable

class TradeApi:
    def __init__(self, fetch_func: Callable):
        self._fetch = fetch_func

    async def post_v5_order_create(
        self,
        category: str,
        symbol: str,
        side: str,
        order_type: str,
        qty: str,
        **kwargs,
    ) -> Dict[str, Any]:
        """
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

    async def post_v5_order_cancel(
        self, category: str, symbol: str, **kwargs
    ) -> Dict[str, Any]:
        """
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


    
    async def get_v5_order_realtime(self, category: str, **kwargs):
        """
        https://bybit-exchange.github.io/docs/v5/order/open-order
        """
        endpoint = "/v5/order/realtime"
        payload = {
            "category": category,
            **kwargs,
        }
        raw = await self._fetch("GET", endpoint, payload, signed=True)
        return orjson.loads(raw)

    async def get_v5_order_history(self, category: str, **kwargs):
        """
        https://bybit-exchange.github.io/docs/v5/order/order-list
        """
        endpoint = "/v5/order/history"
        payload = {
            "category": category,
            **kwargs,
        }
        raw = await self._fetch("GET", endpoint, payload, signed=True)
        return orjson.loads(raw)
