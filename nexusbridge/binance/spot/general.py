async def get_api_v3_ping(self):
    """
    Test connectivity
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-endpoints
    """
    endpoint = "/api/v3/ping"
    raw = await self._fetch("GET", endpoint, signed=False)
    return raw


async def get_api_v3_time(self):
    """
    Check server time
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-endpoints
    """
    endpoint = "/api/v3/time"
    raw = await self._fetch("GET", endpoint, signed=False)
    return raw


async def get_api_v3_exchangeInfo(self, **kwargs):
    """
    Current exchange trading rules and symbol information
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-endpoints
    """
    endpoint = "/api/v3/exchangeInfo"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw
