async def get_dapi_v1_exchangeInfo(self):
    """
    Get the exchange information
    """
    endpoint = "/dapi/v1/exchangeInfo"
    raw = await self._fetch("GET", endpoint, signed=False)
    return raw
