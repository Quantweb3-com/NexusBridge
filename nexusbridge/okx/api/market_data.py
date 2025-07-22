import orjson


async def get_api_v5_market_tickers(self, inst_type: str, **kwargs):
    """
    Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-market-data-get-tickers
    """
    endpoint = "/api/v5/market/tickers"
    payload = {"instType": inst_type, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_ticker(self, inst_id: str):
    """
    Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-market-data-get-ticker
    """
    endpoint = "/api/v5/market/ticker"
    payload = {"instId": inst_id}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_books(self, inst_id: str, sz: str | None = None):
    """
    Retrieve order book of the instrument.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-market-data-get-order-book
    """
    endpoint = "/api/v5/market/books"
    payload = {
        "instId": inst_id,
    }
    if sz:
        payload["sz"] = sz
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_books_full(self, inst_id: str, sz: str | None = None):
    """
    Retrieve order book of the instrument. The data will be updated once a second.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-market-data-get-full-order-book
    """
    endpoint = "/api/v5/market/books-full"
    payload = {
        "instId": inst_id,
    }
    if sz:
        payload["sz"] = sz
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_candles(self, inst_id: str, **kwargs):
    """
    Retrieve the candlestick charts. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-market-data-get-candlesticks
    """
    endpoint = "/api/v5/market/candles"
    payload = {"instId": inst_id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_history_candles(self, inst_id: str, **kwargs):
    """
    Retrieve history candlestick charts from recent years(It is last 3 months supported for 1s candlestick).
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-market-data-get-candlesticks-history
    """
    endpoint = "/api/v5/market/history-candles"
    payload = {"instId": inst_id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_trades(
    self,
    inst_id: str,
    limit: str | None = None,
):
    """
    Retrieve the recent transactions of an instrument.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-market-data-get-trades
    """
    endpoint = "/api/v5/market/trades"
    payload = {
        "instId": inst_id,
    }
    if limit:
        payload["limit"] = limit
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_history_trades(self, inst_id: str, **kwargs):
    """
    Retrieve the recent transactions of an instrument from the last 3 months with pagination.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-market-data-get-trades-history
    """
    endpoint = "/api/v5/market/history-trades"
    payload = {"instId": inst_id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_option_instrument_family_trades(self, inst_family: str):
    """
    Retrieve the recent transactions of an instrument under same instFamily. The maximum is 100.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-market-data-get-option-trades-by-instrument-family
    """
    endpoint = "/api/v5/market/option/instrument-family-trades"
    payload = {"instFamily": inst_family}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_option_trades(self, **kwargs):
    """
    The maximum is 100.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-market-data-get-option-trades
    """
    endpoint = "/api/v5/public/option-trades"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_platform_24_volume(self):
    """
    The 24-hour trading volume is calculated on a rolling basis.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-market-data-get-24h-total-volume
    """
    endpoint = "/api/v5/market/platform-24-volume"
    raw = await self._fetch("GET", endpoint, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_call_auction_details(self, inst_id: str):
    """
    Retrieve call auction details.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-market-data-get-call-auction-details
    """
    endpoint = "/api/v5/market/call-auction-details"
    payload = {"instId": inst_id}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)
