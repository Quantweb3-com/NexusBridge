import json

from nexusbridge.binance.constants import Interval


async def get_api_v3_depth(self, symbol: str, limit: int = 100):
    """
    Order book
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
    """
    endpoint = "/api/v3/depth"
    payload = {"symbol": symbol, "limit": limit}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_api_v3_trades(self, symbol: str, limit: int = 500):
    """
    Recent trades list
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
    """
    endpoint = "/api/v3/trades"
    payload = {"symbol": symbol, "limit": limit}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_api_v3_historical_trades(self, symbol: str, **kwargs):
    """
    Old trade lookup
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
    """
    endpoint = "/api/v3/historicalTrades"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_api_v3_klines(self, symbol: str, interval: Interval, **kwargs):
    """
    Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
    """
    endpoint = "/api/v3/klines"
    payload = {"symbol": symbol, "interval": interval.value, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_api_v3_ui_klines(self, symbol: str, interval: Interval, **kwargs):
    """
    The request is similar to klines having the same parameters and response.
    uiKlines return modified kline data, optimized for presentation of candlestick charts.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
    """
    endpoint = "/api/v3/uiKlines"
    payload = {"symbol": symbol, "interval": interval.value, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_api_v3_avgPrice(self, symbol: str):
    """
    Current average price for a symbol.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
    """
    endpoint = "/api/v3/avgPrice"
    payload = {"symbol": symbol}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_api_v3_ticker_24hr(self, **kwargs):
    """
    24 hour rolling window price change statistics. Careful when accessing this with no symbol.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
    """
    endpoint = "/api/v3/ticker/24hr"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_api_v3_ticker_tradingDay(self, symbols: str | list[str], **kwargs):
    """
    Price change statistics for a trading day.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
    """
    endpoint = "/api/v3/ticker/tradingDay"
    payload = {**kwargs}
    if isinstance(symbols, str):
        payload["symbol"] = symbols
    else:
        payload["symbols"] = str(json.dumps(symbols)).replace(" ", "")
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_api_v3_ticker_price(self, **kwargs):
    """
    Latest price for a symbol or symbols.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
    """
    endpoint = "/api/v3/ticker/price"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_api_v3_ticker_bookTicker(self, **kwargs):
    """
    Best price/qty on the order book for a symbol or symbols.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
    """
    endpoint = "/api/v3/ticker/bookTicker"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_api_v3_ticker(self, symbols: str | list[str], **kwargs):
    """
    Rolling window price change statistics
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
    """
    endpoint = "/api/v3/ticker"
    payload = {**kwargs}
    if isinstance(symbols, str):
        payload["symbol"] = symbols
    else:
        payload["symbols"] = str(json.dumps(symbols)).replace(" ", "")
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw
