async def get_fapi_v1_exchangeInfo(self):
    """
    Get the exchange information
    """
    endpoint = "/fapi/v1/exchangeInfo"
    raw = await self._fetch("GET", endpoint, signed=False)
    return raw
