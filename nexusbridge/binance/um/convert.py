async def get_fapi_v1_convert_exchange_info(
    self,
    from_asset: str | None = None,
    to_asset: str | None = None,
):
    """
    Query for all convertible token pairs and the tokens’ respective upper/lower limits
    https://developers.binance.com/docs/derivatives/usds-margined-futures/convert
    """
    endpoint = "/fapi/v1/convert/exchangeInfo"
    payload = {}
    if from_asset:
        payload["fromAsset"] = from_asset
    if to_asset:
        payload["toAsset"] = to_asset
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def post_fapi_v1_convert_get_quote(
    self, from_asset: str, to_asset: str, **kwargs
):
    """
    Request a quote for the requested token pairs
    https://developers.binance.com/docs/derivatives/usds-margined-futures/convert/Send-quote-request
    """
    endpoint = "/fapi/v1/convert/getQuote"
    payload = {"fromAsset": from_asset, "toAsset": to_asset, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_fapi_v1_convert_accept_quote(self, quote_id: str, **kwargs):
    """
    Accept the offered quote by quote ID.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/convert/Accept-Quote
    """
    endpoint = "/fapi/v1/convert/acceptQuote"
    payload = {"quoteId": quote_id, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_convert_order_status(self, **kwargs):
    """
    Query order status by order ID.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/convert/Order-Status
    """
    endpoint = "/fapi/v1/convert/orderStatus"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw
