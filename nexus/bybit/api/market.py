import orjson
from typing import Any, Dict, Literal


class MarketApi:
    def __init__(self, fetch_func: callable):
        self._fetch = fetch_func

    async def get_v5_market_time(self):
        """
        Get Bybit Server Time
        https://bybit-exchange.github.io/docs/v5/market/time
        """
        endpoint = "/v5/market/time"
        raw = await self._fetch("GET", endpoint, signed=False)
        return orjson.loads(raw)

    async def get_v5_market_kline(
            self,
            symbol: str,
            interval: str,
            **kwargs
    ):
        """
        Query for historical klines (also known as candles/candlesticks). Charts are returned in groups based on the requested interval.
        https://bybit-exchange.github.io/docs/v5/market/kline
        """
        endpoint = "/v5/market/kline"
        payload = {
            "symbol": symbol,
            "interval": interval,
            **kwargs
        }
        raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
        return orjson.loads(raw)

    async def get_v5_market_mark_price_kline(
            self,
            symbol: str,
            interval: str,
            **kwargs
    ):
        """
        Query for historical mark price klines. Charts are returned in groups based on the requested interval.
        https://bybit-exchange.github.io/docs/v5/market/mark-kline
        """
        endpoint = "/v5/market/mark-price-kline"
        payload = {
            "symbol": symbol,
            "interval": interval,
            **kwargs
        }
        raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
        return orjson.loads(raw)

    async def get_v5_market_index_price_kline(
            self,
            symbol: str,
            interval: str,
            **kwargs
    ):
        """
        Query for historical index price klines. Charts are returned in groups based on the requested interval.
        https://bybit-exchange.github.io/docs/v5/market/index-kline
        """
        endpoint = "/v5/market/index-price-kline"
        payload = {
            "symbol": symbol,
            "interval": interval,
            **kwargs
        }
        raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
        return orjson.loads(raw)

    async def get_v5_market_premium_index_price_kline(
            self,
            symbol: str,
            interval: str,
            **kwargs
    ):
        """
        Query for historical premium index klines. Charts are returned in groups based on the requested interval.
        https://bybit-exchange.github.io/docs/v5/market/premium-index-kline
        """
        endpoint = "/v5/market/premium-index-price-kline"
        payload = {
            "symbol": symbol,
            "interval": interval,
            **kwargs
        }
        raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
        return orjson.loads(raw)

    async def get_v5_market_instruments_info(self, **kwargs):
        """
        Query for the instrument specification of online trading pairs.
        https://bybit-exchange.github.io/docs/v5/market/instrument
        """
        endpoint = "/v5/market/instruments-info"
        payload = {
            **kwargs
        }
        raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
        return orjson.loads(raw)

    async def get_v5_market_orderbook(
            self,
            symbol: str,
            category: Literal["spot", "linear", "inverse", "option"],
            limit: int | None = None
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
            self,
            category: Literal["spot", "linear", "inverse", "option"],
            **kwargs
    ):
        """
        Query for the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours.
        https://bybit-exchange.github.io/docs/v5/market/tickers
        """
        endpoint = "/v5/market/tickers"
        payload = {
            "category": category,
            **kwargs
        }
        raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
        return orjson.loads(raw)

    async def get_v5_market_funding_history(
            self,
            symbol: str,
            category: Literal["linear", "inverse"],
            **kwargs
    ):
        """
        Query for historical funding rates. Each symbol has a different funding interval. For example, if the interval is 8 hours and the current time is UTC 12, then it returns the last funding rate, which settled at UTC 8.
        https://bybit-exchange.github.io/docs/v5/market/history-fund-rate
        """
        endpoint = "/v5/market/funding/history"
        payload = {
            "symbol": symbol,
            "category": category,
            **kwargs
        }
        raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
        return orjson.loads(raw)

    async def get_v5_market_recent_trade(
            self,
            category: Literal["spot", "linear", "inverse", "option"],
            **kwargs
    ):
        """
        Query recent public trading data in Bybit.
        https://bybit-exchange.github.io/docs/v5/market/recent-trade
        """
        endpoint = "/v5/market/recent-trade"
        payload = {
            "category": category,
            **kwargs
        }
        raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
        return orjson.loads(raw)

