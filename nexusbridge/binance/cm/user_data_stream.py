async def post_dapi_v1_listen_key(self, signed=False):
    """
    Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream
    """
    endpoint = "/dapi/v1/listenKey"
    raw = await self._fetch("POST", endpoint, signed=signed)
    return raw


async def put_dapi_v1_listen_key(self, signed=False):
    """
    Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 60 minutes.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Keepalive-User-Data-Stream
    """
    endpoint = "/dapi/v1/listenKey"
    raw = await self._fetch("PUT", endpoint, signed=signed)
    return raw


async def delete_dapi_v1_listen_key(self, signed=False):
    """
    Close out a user data stream.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream
    """
    endpoint = "/dapi/v1/listenKey"
    raw = await self._fetch("DELETE", endpoint, signed=signed)
    return raw
