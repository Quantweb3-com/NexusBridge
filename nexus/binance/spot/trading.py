from nexus.binance.constants import Side, OrderType


async def post_api_v3_order(
        self,
        symbol: str,
        side: Side,
        _type: OrderType,
        **kwargs
):
    """
    Send in a new order.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints
    """
    endpoint = "/api/v3/order"
    payload = {
        "symbol": symbol,
        "side": side.value,
        "type": _type.value,
        **kwargs
    }

    raw = await self._fetch("GET", endpoint, payload=payload, signed=False, timestamp=True)
    return raw
