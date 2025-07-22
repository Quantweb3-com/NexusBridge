from typing import Literal


async def agg_trade(
    self, symbol: str, subscription: bool = True, _id: int | None = None
):
    """
    The Aggregate Trade Streams push market trade information that is aggregated for fills with same price and taking side every 100 milliseconds.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams
    """
    stream_name = "{}@aggTrade".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def index_price(
    self, symbol: str, subscription: bool = True, _id: int | None = None
):
    """
    Index Price Stream
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Price-Stream
    """
    stream_name = "{}@indexPrice".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def mark_price(
    self, symbol: str, subscription: bool = True, _id: int | None = None
):
    """
    Mark price update stream
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Mark-Price-Stream
    """
    stream_name = "{}@markPrice".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def kline(
    self,
    symbol: str,
    interval: Literal[
        "1m",
        "3m",
        "5m",
        "15m",
        "30m",
        "1h",
        "2h",
        "4h",
        "6h",
        "8h",
        "12h",
        "1d",
        "3d",
        "1w",
        "1M",
    ],
    subscription: bool = True,
    _id: int | None = None,
):
    """
    The Kline/Candlestick Stream push updates to the current klines/candlestick every 250 milliseconds (if existing).
    Kline/Candlestick chart intervals: m -> minutes; h -> hours; d -> days; w -> weeks; M -> months
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams
    """
    stream_name = "{}@kline_{}".format(symbol.lower(), interval)
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def continuous_kline(
    self,
    pair: str,
    contract_type: Literal["perpetual", "current_quarter", "next_quarter"],
    interval: Literal[
        "1m",
        "3m",
        "5m",
        "15m",
        "30m",
        "1h",
        "2h",
        "4h",
        "6h",
        "8h",
        "12h",
        "1d",
        "3d",
        "1w",
        "1M",
    ],
    subscription: bool = True,
    _id: int | None = None,
):
    """
    Kline update every second
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Continuous-Contract-Kline-Candlestick-Streams
    """
    stream_name = "{}_{}@continuousKline_{}".format(
        pair.lower(), contract_type, interval
    )
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def pair_mark_price(
    self, pair: str, subscription: bool = True, _id: int | None = None
):
    """
    Mark Price of All Symbols of a Pair
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Mark-Price-of-All-Symbols-of-a-Pair
    """
    stream_name = "{}@markPrice".format(pair.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def index_price_kline(
    self,
    pair: str,
    interval: Literal[
        "1m",
        "3m",
        "5m",
        "15m",
        "30m",
        "1h",
        "2h",
        "4h",
        "6h",
        "8h",
        "12h",
        "1d",
        "3d",
        "1w",
        "1M",
    ],
    subscription: bool = True,
    _id: int | None = None,
):
    """
    Index Kline/Candlestick Streams
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Kline-Candlestick-Streams
    """
    stream_name = "{}@indexPriceKline_{}".format(pair.lower(), interval)
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def mark_price_kline(
    self,
    symbol: str,
    interval: Literal[
        "1m",
        "3m",
        "5m",
        "15m",
        "30m",
        "1h",
        "2h",
        "4h",
        "6h",
        "8h",
        "12h",
        "1d",
        "3d",
        "1w",
        "1M",
    ],
    subscription: bool = True,
    _id: int | None = None,
):
    """
    Mark Price Kline/Candlestick Streams
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Mark-Price-Kline-Candlestick-Streams
    """
    stream_name = "{}@markPriceKline_{}".format(symbol.lower(), interval)
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def mini_ticker(
    self, symbol: str, subscription: bool = True, _id: int | None = None
):
    """
    24hr rolling window mini-ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream
    """
    stream_name = "{}@miniTicker".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def mini_ticker_arr(self, subscription: bool = True, _id: int | None = None):
    """
    24hr rolling window mini-ticker statistics for all symbols. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before. Note that only tickers that have changed will be present in the array.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream
    """
    stream_name = "!miniTicker@arr"
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def ticker(self, symbol: str, subscription: bool = True, _id: int | None = None):
    """
    24hr rolling window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams
    """
    stream_name = "{}@ticker".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def ticker_arr(self, subscription: bool = True, _id: int | None = None):
    """
    24hr rolling window ticker statistics for all symbols. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before. Note that only tickers that have changed will be present in the array.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Tickers-Streams
    """
    stream_name = "!ticker@arr"
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def book_ticker(
    self, symbol: str, subscription: bool = True, _id: int | None = None
):
    """
    Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams
    """
    stream_name = "{}@bookTicker".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def book_ticker_arr(self, subscription: bool = True, _id: int | None = None):
    """
    Pushes any update to the best bid or ask's price or quantity in real-time for all symbols.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Book-Tickers-Stream
    """
    stream_name = "!bookTicker"
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def force_orders(
    self, symbol: str, subscription: bool = True, _id: int | None = None
):
    """
    The Liquidation Order Snapshot Streams push force liquidation order information for specific symbol.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Liquidation-Order-Streams
    """
    stream_name = "{}@forceOrder".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def force_orders_arr(self, subscription: bool = True, _id: int | None = None):
    """
    The All Liquidation Order Snapshot Streams push force liquidation order information for all symbols in the market. For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams
    """
    stream_name = "!forceOrder@arr"
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def contract_info(self, subscription: bool = True, _id: int | None = None):
    """
    ContractInfo stream pushes when contract info updates(listing/settlement/contract bracket update). bks field only shows up when bracket gets updated.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Contract-Info-Stream
    """
    stream_name = "!contractInfo"
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def depth_levels(
    self,
    symbol: str,
    levels: Literal[5, 10, 20],
    subscription: bool = True,
    _id: int | None = None,
):
    """
    Top <levels> bids and asks, Valid <levels> are 5, 10, or 20.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams
    """
    stream_name = "{}@depth{}".format(symbol.lower(), levels)
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def diff_depth(
    self, symbol: str, subscription: bool = True, _id: int | None = None
):
    """
    Bids and asks, pushed every 250 milliseconds, 500 milliseconds, or 100 milliseconds
    https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams
    """
    stream_name = "{}@depth".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)
