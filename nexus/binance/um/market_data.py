async def get_fapi_v1_ping(
        self,
):
    """
    Test connectivity
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api
    """
    endpoint = "/fapi/v1/ping"
    raw = await self._fetch("GET", endpoint, signed=False)
    return raw

async def get_fapi_v1_time(self):
    """
    Check server time
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Check-Server-Time
    """
    endpoint = "/fapi/v1/time"
    raw = await self._fetch("GET", endpoint, signed=False)
    return raw
