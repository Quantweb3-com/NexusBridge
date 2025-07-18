async def get_papi_v1_ping(self):
    endpoint = "/papi/v1/ping"
    """
    Test connectivity to the Rest API.
    https://developers.binance.com/docs/derivatives/portfolio-margin/market-data
    """
    raw = await self._fetch("GET", endpoint, signed=False)
    return raw


async def post_papi_v1_listen_key(self):
    endpoint = "/papi/v1/listenKey"
    """
    Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.
    https://developers.binance.com/docs/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream
    """
    raw = await self._fetch("POST", endpoint, signed=False)
    return raw


async def put_papi_v1_listen_key(self):
    endpoint = "/papi/v1/listenKey"
    """
    Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 30 minutes.
    https://developers.binance.com/docs/derivatives/portfolio-margin/user-data-streams/Keepalive-User-Data-Stream#http-request
    """
    raw = await self._fetch("PUT", endpoint, signed=True)
    return raw


async def delete_papi_v1_listen_key(self):
    endpoint = "/papi/v1/listenKey"
    """
    Close out a user data stream.
    https://developers.binance.com/docs/derivatives/portfolio-margin/user-data-streams/Close-User-Data-Stream
    """
    raw = await self._fetch("DELETE", endpoint, signed=True)
    return raw
