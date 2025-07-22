from typing import Literal

from nexusbridge.binance.constants import Interval, ContractType


async def get_dapi_v1_ping(
    self,
):
    """
    Test connectivity to the Rest API.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data
    """
    endpoint = "/dapi/v1/ping"
    raw = await self._fetch("GET", endpoint, signed=False)
    return raw


async def get_dapi_v1_time(
    self,
):
    """
    Test connectivity to the Rest API and get the current server time.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Check-Server-time
    """
    endpoint = "/dapi/v1/time"
    raw = await self._fetch("GET", endpoint, signed=False)
    return raw


async def get_dapi_v1_exchange_info(
    self,
):
    """
    Current exchange trading rules and symbol information
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Exchange-Information
    """
    endpoint = "/dapi/v1/exchangeInfo"
    raw = await self._fetch("GET", endpoint, signed=False)
    return raw


async def get_dapi_v1_depth(self, symbol: str, **kwargs):
    """
    Query orderbook on specific symbol
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Order-Book
    """
    endpoint = "/dapi/v1/depth"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_trades(self, symbol: str, **kwargs):
    """
    Get recent market trades
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Recent-Trades-List
    """
    endpoint = "/dapi/v1/trades"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_historical_trades(self, symbol: str, **kwargs):
    """
    Get older market historical trades.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Old-Trades-Lookup
    """
    endpoint = "/dapi/v1/historicalTrades"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_agg_trades(self, symbol: str, **kwargs):
    """
    Get compressed, aggregate trades. Market trades that fill in 100ms with the same price and the same taking side will have the quantity aggregated.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Compressed-Aggregate-Trades-List
    """
    endpoint = "/dapi/v1/aggTrades"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_premium_index(self, **kwargs):
    """
    Query index price and mark price
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Index-Price-and-Mark-Price
    """
    endpoint = "/dapi/v1/premiumIndex"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_funding_rate(self, symbol: str, **kwargs):
    """
    Get Funding Rate History of Perpetual Futures
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Get-Funding-Rate-History-of-Perpetual-Futures
    """
    endpoint = "/dapi/v1/fundingRate"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_funding_info(
    self,
):
    """
    Query funding rate info for symbols that had FundingRateCap/ FundingRateFloor / fundingIntervalHours adjustment
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Get-Funding-Info
    """
    endpoint = "/dapi/v1/fundingInfo"
    raw = await self._fetch("GET", endpoint, signed=False)
    return raw


async def get_dapi_v1_klines(self, symbol: str, interval: Interval, **kwargs):
    """
    Kline/candlestick bars for a symbol.
    Klines are uniquely identified by their open time.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/kline-candlestick-data
    """
    endpoint = "/dapi/v1/klines"
    payload = {"symbol": symbol, "interval": interval.value, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_continuous_klines(
    self, pair: str, interval: Interval, contract_type: ContractType, **kwargs
):
    """
    Kline/candlestick bars for a specific contract type. Klines are uniquely identified by their open time.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Continuous-Contract-Kline-Candlestick-Data
    """
    endpoint = "/dapi/v1/continuousKlines"
    payload = {
        "pair": pair,
        "contractType": contract_type.value,
        "interval": interval.value,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_index_price_klines(self, pair: str, interval: Interval, **kwargs):
    """
    Kline/candlestick bars for the index price of a pair. Klines are uniquely identified by their open time.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Index-Price-Kline-Candlestick-Data
    """
    endpoint = "/dapi/v1/indexPriceKlines"
    payload = {"pair": pair, "interval": interval.value, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_mark_price_klines(
    self, symbol: str, interval: Interval, **kwargs
):
    """
    Kline/candlestick bars for the mark price of a symbol. Klines are uniquely identified by their open time.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Mark-Price-Kline-Candlestick-Data
    """
    endpoint = "/dapi/v1/markPriceKlines"
    payload = {"symbol": symbol, "interval": interval.value, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_premium_index_klines(
    self, symbol: str, interval: Interval, **kwargs
):
    """
    Premium index kline bars of a symbol. Klines are uniquely identified by their open time.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Premium-Index-Kline-Data
    """
    endpoint = "/dapi/v1/premiumIndexKlines"
    payload = {"symbol": symbol, "interval": interval.value, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_ticker_24hr(self, **kwargs):
    """
    24 hour rolling window price change statistics.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/24hr-Ticker-Price-Change-Statistics
    """
    endpoint = "/dapi/v1/ticker/24hr"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_ticker_price(self, **kwargs):
    """
    Latest price for a symbol or symbols.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Symbol-Price-Ticker
    """
    endpoint = "/dapi/v1/ticker/price"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_ticker_book_ticker(self, **kwargs):
    """
    Best price/qty on the order book for a symbol or symbols.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Symbol-Order-Book-Ticker
    """
    endpoint = "/dapi/v1/ticker/bookTicker"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_open_interest(
    self,
    symbol: str,
):
    """
    Get present open interest of a specific symbol.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Open-Interest
    """
    endpoint = "/dapi/v1/openInterest"
    payload = {
        "symbol": symbol,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_futures_data_open_interest_hist(
    self,
    pair: str,
    contract_type: ContractType,
    period: Literal["5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d"],
    **kwargs,
):
    """
    Query open interest stats
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Open-Interest-Statistics
    """
    endpoint = "/futures/data/openInterestHist"
    payload = {
        "pair": pair,
        "contractType": contract_type.value,
        "period": period,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_futures_data_top_long_short_position_ratio(
    self,
    pair: str,
    period: Literal["5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d"],
    **kwargs,
):
    """
    The proportion of net long and net short positions to total open positions of the top 20% users with the highest margin balance. Long Position % = Long positions of top traders / Total open positions of top traders Short Position % = Short positions of top traders / Total open positions of top traders Long/Short Ratio (Positions) = Long Position % / Short Position %
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Top-Trader-Long-Short-Ratio
    """
    endpoint = "/futures/data/topLongShortPositionRatio"
    payload = {"pair": pair, "period": period, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_futures_data_top_long_short_account_ratio(
    self,
    pair: str,
    period: Literal["5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d"],
    **kwargs,
):
    """
    The proportion of net long and net short accounts to total accounts of the top 20% users with the highest margin balance. Each account is counted once only. Long Account % = Accounts of top traders with net long positions / Total accounts of top traders with open positions Short Account % = Accounts of top traders with net short positions / Total accounts of top traders with open positions Long/Short Ratio (Accounts) = Long Account % / Short Account %
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Top-Long-Short-Account-Ratio
    """
    endpoint = "/futures/data/topLongShortAccountRatio"
    payload = {"pair": pair, "period": period, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_futures_data_global_long_short_account_ratio(
    self,
    pair: str,
    period: Literal["5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d"],
    **kwargs,
):
    """
    Query symbol Long/Short Ratio
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Long-Short-Ratio
    """
    endpoint = "/futures/data/globalLongShortAccountRatio"
    payload = {"pair": pair, "period": period, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_futures_data_taker_buy_sell_vol(
    self,
    pair: str,
    contract_type: ContractType,
    period: Literal["5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d"],
    **kwargs,
):
    """
    Taker Buy Volume: the total volume of buy orders filled by takers within the period. Taker Sell Volume: the total volume of sell orders filled by takers within the period.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Taker-Buy-Sell-Volume
    """
    endpoint = "/futures/data/takerBuySellVol"
    payload = {
        "pair": pair,
        "period": period,
        "contractType": contract_type.value,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_futures_data_basis(
    self,
    pair: str,
    contract_type: ContractType,
    period: Literal["5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d"],
    **kwargs,
):
    """
    Query Basis
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Basis
    """
    endpoint = "/futures/data/basis"
    payload = {
        "pair": pair,
        "period": period,
        "contractType": contract_type.value,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw


async def get_dapi_v1_constituents(
    self,
    symbol: str,
):
    """
    Query index price constituents
    https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Index-Constituents
    """
    endpoint = "/dapi/v1/constituents"
    payload = {
        "symbol": symbol,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return raw
