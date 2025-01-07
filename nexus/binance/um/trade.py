async def fapi_v1_order(self, symbol: str, side: str, type: str, **kwargs):
    """
    Place a new order
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trading/rest-api
    """
    endpoint = "/fapi/v1/order"
    payload = {
        "symbol": symbol,
        "side": side,
        "type": type,
        **kwargs
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw
