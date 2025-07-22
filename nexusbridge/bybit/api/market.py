import orjson
from typing import Literal


async def get_v5_market_time(self):
    """
    Get Bybit Server Time
    https://bybit-exchange.github.io/docs/v5/market/time
    """
    endpoint = "/v5/market/time"
    raw = await self._fetch("GET", endpoint, signed=False)
    return orjson.loads(raw)


async def get_v5_market_kline(self, symbol: str, interval: str, **kwargs):
    """
    Query for historical klines (also known as candles/candlesticks). Charts are returned in groups based on the requested interval.
    https://bybit-exchange.github.io/docs/v5/market/kline
    """
    endpoint = "/v5/market/kline"
    payload = {"symbol": symbol, "interval": interval, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_v5_market_mark_price_kline(self, symbol: str, interval: str, **kwargs):
    """
    Query for historical mark price klines. Charts are returned in groups based on the requested interval.
    https://bybit-exchange.github.io/docs/v5/market/mark-kline
    """
    endpoint = "/v5/market/mark-price-kline"
    payload = {"symbol": symbol, "interval": interval, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_v5_market_index_price_kline(self, symbol: str, interval: str, **kwargs):
    """
    Query for historical index price klines. Charts are returned in groups based on the requested interval.
    https://bybit-exchange.github.io/docs/v5/market/index-kline
    """
    endpoint = "/v5/market/index-price-kline"
    payload = {"symbol": symbol, "interval": interval, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_v5_market_premium_index_price_kline(
    self, symbol: str, interval: str, **kwargs
):
    """
    Query for historical premium index klines. Charts are returned in groups based on the requested interval.
    https://bybit-exchange.github.io/docs/v5/market/premium-index-kline
    """
    endpoint = "/v5/market/premium-index-price-kline"
    payload = {"symbol": symbol, "interval": interval, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_v5_market_instruments_info(self, **kwargs):
    """
    Query for the instrument specification of online trading pairs.
    https://bybit-exchange.github.io/docs/v5/market/instrument
    """
    endpoint = "/v5/market/instruments-info"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_v5_market_orderbook(
    self,
    symbol: str,
    category: Literal["spot", "linear", "inverse", "option"],
    limit: int | None = None,
):
    """
    Query for orderbook depth data.
    https://bybit-exchange.github.io/docs/v5/market/orderbook
    """
    endpoint = "/v5/market/orderbook"
    payload = {
        "symbol": symbol,
        "category": category,
    }
    if limit:
        payload["limit"] = limit
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_v5_market_tickers(
    self, category: Literal["spot", "linear", "inverse", "option"], **kwargs
):
    """
    Query for the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours.
    https://bybit-exchange.github.io/docs/v5/market/tickers
    """
    endpoint = "/v5/market/tickers"
    payload = {"category": category, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_v5_market_funding_history(
    self, symbol: str, category: Literal["linear", "inverse"], **kwargs
):
    """
    Query for historical funding rates. Each symbol has a different funding interval. For example, if the interval is 8 hours and the current time is UTC 12, then it returns the last funding rate, which settled at UTC 8.
    https://bybit-exchange.github.io/docs/v5/market/history-fund-rate
    """
    endpoint = "/v5/market/funding/history"
    payload = {"symbol": symbol, "category": category, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_v5_market_recent_trade(
    self, category: Literal["spot", "linear", "inverse", "option"], **kwargs
):
    """
    Query recent public trading data in Bybit.
    https://bybit-exchange.github.io/docs/v5/market/recent-trade
    """
    endpoint = "/v5/market/recent-trade"
    payload = {"category": category, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_v5_market_open_interest(
    self,
    symbol: str,
    category: Literal["linear", "inverse"],
    interval_time: Literal["5min", "15min", "30min", "1h", "4h", "1d"],
    **kwargs,
):
    """
    Get the open interest of each symbol.
    https://bybit-exchange.github.io/docs/v5/market/open-interest
    """
    endpoint = "/v5/market/open-interest"
    payload = {
        "symbol": symbol,
        "category": category,
        "interval_time": interval_time,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_v5_market_historical_volatility(self, category: str = "option", **kwargs):
    """
    Query option historical volatility
    https://bybit-exchange.github.io/docs/v5/market/iv
    """
    endpoint = "/v5/market/historical-volatility"
    payload = {"category": category, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_v5_market_insurance(
    self,
    coin: str | None = None,
):
    """
    Query for Bybit insurance pool data (BTC/USDT/USDC etc). The data is updated every 24 hours.
    https://bybit-exchange.github.io/docs/v5/market/insurance
    """
    endpoint = "/v5/market/insurance"
    payload = {}
    if coin:
        payload["coin"] = coin
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_v5_market_risk_limit(
    self, category: Literal["linear", "inverse"], **kwargs
):
    """
    Query for the risk limit.
    https://bybit-exchange.github.io/docs/v5/market/risk-limit
    """
    endpoint = "/v5/market/risk-limit"
    payload = {"category": category, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_v5_market_delivery_price(
    self, category: Literal["linear", "inverse", "option"], **kwargs
):
    """
    Get the delivery price.
    https://bybit-exchange.github.io/docs/v5/market/delivery-price
    """
    endpoint = "/v5/market/delivery-price"
    payload = {"category": category, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_v5_market_account_ratio(
    self,
    category: Literal["linear", "inverse"],
    symbol: str,
    period: Literal["5min", "15min", "30min", "1h", "4h", "1d"],
    **kwargs,
):
    """
     Get Long Short Ratio
    https://bybit-exchange.github.io/docs/v5/market/long-short-ratio
    """
    endpoint = "/v5/market/account-ratio"
    payload = {"category": category, "symbol": symbol, "period": period, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)
