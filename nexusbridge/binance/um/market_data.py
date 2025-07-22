from typing import Literal

from nexusbridge.binance.constants import Interval, ContractType


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


async def get_fapi_v1_exchange_info(
    self,
):
    """
    Current exchange trading rules and symbol information
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information
    """
    endpoint = "/fapi/v1/exchangeInfo"
    raw = await self._fetch("GET", endpoint, signed=False)
    return raw


async def get_fapi_v1_depth(
    self,
    symbol: str,
    limit: int = 500,
):
    """
    Query symbol orderbook
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book
    """
    endpoint = "/fapi/v1/depth"
    payload = {"symbol": symbol, "limit": limit}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_trades(
    self,
    symbol: str,
    limit: int = 500,
):
    """
    Get recent market trades
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Recent-Trades-List
    """
    endpoint = "/fapi/v1/trades"
    payload = {"symbol": symbol, "limit": limit}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_historical_trades(self, symbol: str, **kwargs):
    """
    Get older market historical trades.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Old-Trades-Lookup
    """
    endpoint = "/fapi/v1/historicalTrades"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_agg_trades(self, symbol: str, **kwargs):
    """
    Get compressed, aggregate market trades. Market trades that fill in 100ms with the same price and the same taking side will have the quantity aggregated.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List
    """
    endpoint = "/fapi/v1/aggTrades"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_klines(self, symbol: str, interval: Interval, **kwargs):
    """
    Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Kline-Candlestick-Data
    """
    endpoint = "/fapi/v1/klines"
    payload = {"symbol": symbol, "interval": interval.value, **kwargs}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_continuous_klines(
    self, pair: str, contract_type: ContractType, interval: Interval, **kwargs
):
    """
    Kline/candlestick bars for a specific contract type of a pair. Klines are uniquely identified by their open time.
    https://binance-docs.github.io/apidocs/futures/en/#continuous-contract-kline-candlestick-data
    """
    endpoint = "/fapi/v1/continuousKlines"
    payload = {
        "pair": pair,
        "contractType": contract_type.value,
        "interval": interval.value,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_index_price_klines(self, pair: str, interval: Interval, **kwargs):
    """
    Kline/candlestick bars for the index price of a pair. Klines are uniquely identified by their open time.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Index-Price-Kline-Candlestick-Data
    """
    endpoint = "/fapi/v1/indexPriceKlines"
    payload = {"pair": pair, "interval": interval.value, **kwargs}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_mark_price_klines(
    self, symbol: str, interval: Interval, **kwargs
):
    """
    Kline/candlestick bars for the mark price of a symbol. Klines are uniquely identified by their open time.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data
    """
    endpoint = "/fapi/v1/markPriceKlines"
    payload = {"symbol": symbol, "interval": interval.value, **kwargs}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_premium_index_klines(
    self, symbol: str, interval: Interval, **kwargs
):
    """
    Premium index kline bars of a symbol. Klines are uniquely identified by their open time.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data
    """
    endpoint = "/fapi/v1/premiumIndexKlines"
    payload = {"symbol": symbol, "interval": interval.value, **kwargs}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_premium_index(
    self,
    symbol: str,
):
    """
    Mark Price and Funding Rate
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price
    """
    endpoint = "/fapi/v1/premiumIndex"
    payload = {
        "symbol": symbol,
    }
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_funding_rate(self, **kwargs):
    """
    Get Funding Rate History
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History
    """
    endpoint = "/fapi/v1/fundingRate"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_funding_info(self):
    """
    Query funding rate info for symbols that had FundingRateCap/ FundingRateFloor / fundingIntervalHours adjustment
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info
    """
    endpoint = "/fapi/v1/fundingInfo"
    raw = await self._fetch("GET", endpoint, signed=False)
    return raw


async def get_fapi_v1_ticker_24hr(self, symbol: str = None):
    """
    24 hour rolling window price change statistics.
    Careful when accessing this with no symbol.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics
    """
    endpoint = "/fapi/v1/ticker/24hr"
    payload = {}
    if symbol:
        payload["symbol"] = symbol
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_ticker_price(self, symbol: str = None):
    """
    Latest price for a symbol or symbols.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/latestPrice
    """
    endpoint = "/fapi/v1/ticker/price"
    payload = {}
    if symbol:
        payload["symbol"] = symbol
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v2_ticker_price(self, symbol: str = None):
    """
    Latest price for a symbol or symbols.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker-v2
    """
    endpoint = "/fapi/v2/ticker/price"
    payload = {}
    if symbol:
        payload["symbol"] = symbol
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_book_ticker(self, symbol: str = None):
    """
    Best price/qty on the order book for a symbol or symbols.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker
    """
    endpoint = "/fapi/v1/ticker/bookTicker"
    payload = {}
    if symbol:
        payload["symbol"] = symbol
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_delivery_price(self, pair: str):
    """
    Latest price for a symbol or symbols.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Delivery-Price
    """
    endpoint = "/fapi/v1/deliveryPrice"
    payload = {"pair": pair}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_open_interest(self, symbol: str):
    """
    Get present open interest of a specific symbol.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest
    """
    endpoint = "/fapi/v1/openInterest"
    payload = {"symbol": symbol}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_open_interest_hist(
    self,
    symbol: str,
    period: Literal["5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d"],
    **kwargs,
):
    """
    Open Interest Statistics
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics
    """
    endpoint = "/fapi/v1/openInterestHist"
    payload = {"symbol": symbol, "period": period, **kwargs}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_futures_data_top_long_short_position_ratio(
    self,
    symbol: str,
    period: Literal["5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d"],
    **kwargs,
):
    """
    The proportion of net long and net short positions to total open positions of the top 20% users with the highest margin balance. Long Position % = Long positions of top traders / Total open positions of top traders Short Position % = Short positions of top traders / Total open positions of top traders Long/Short Ratio (Positions) = Long Position % / Short Position %
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio
    """
    endpoint = "/futures/data/topLongShortPositionRatio"
    payload = {"symbol": symbol, "period": period, **kwargs}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_futures_data_top_long_short_account_ratio(
    self,
    symbol: str,
    period: Literal["5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d"],
    **kwargs,
):
    """
    The proportion of net long and net short accounts to total accounts of the top 20% users with the highest margin balance. Each account is counted once only. Long Account % = Accounts of top traders with net long positions / Total accounts of top traders with open positions Short Account % = Accounts of top traders with net short positions / Total accounts of top traders with open positions Long/Short Ratio (Accounts) = Long Account % / Short Account %
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Top-Long-Short-Account-Ratio
    """
    endpoint = "/futures/data/topLongShortAccountRatio"
    payload = {"symbol": symbol, "period": period, **kwargs}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_futures_data_global_long_short_account_ratio(
    self,
    symbol: str,
    period: Literal["5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d"],
    **kwargs,
):
    """
    Query symbol Long/Short Ratio
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio
    """
    endpoint = "/futures/data/globalLongShortAccountRatio"
    payload = {"symbol": symbol, "period": period, **kwargs}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_futures_data_taker_long_short_ratio(
    self,
    symbol: str,
    period: Literal["5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d"],
    **kwargs,
):
    """
    Taker Buy/Sell Volume
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Taker-BuySell-Volume
    """
    endpoint = "/futures/data/takerlongshortRatio"
    payload = {"symbol": symbol, "period": period, **kwargs}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_lvt_klines(self, symbol: str, interval: Interval, **kwargs):
    """
    Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Kline-Candlestick-Data
    """
    endpoint = "/fapi/v1/lvtKlines"
    payload = {"symbol": symbol, "interval": interval.value, **kwargs}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw


async def get_fapi_v1_index_info(self, symbol: str | None = None):
    """
    Query composite index symbol information
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information
    """
    endpoint = "/fapi/v1/indexInfo"
    payload = {}
    if symbol:
        payload["symbol"] = symbol
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_fapi_v1_asset_index(self, symbol: str | None = None):
    """
    asset index for Multi-Assets mode
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index
    """
    endpoint = "/fapi/v1/assetIndex"
    payload = {}
    if symbol:
        payload["symbol"] = symbol
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_fapi_v1_constituents(self, symbol: str):
    """
    Query index price constituents
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Index-Constituents
    """
    endpoint = "/fapi/v1/constituents"
    payload = {"symbol": symbol}
    raw = await self._fetch("GET", endpoint, signed=False, payload=payload)
    return raw
