from typing import Literal
from urllib.parse import urlencode

from nexus.binance.authentication import hmac_hashing, rsa_signature, ed_25519
from nexus.binance.constants import Interval, OrderType


async def agg_trade(
        self,
        symbol: str,
        subscription: bool = True,
        _id: int | None = None
):
    """
    The Aggregate Trade Streams push trade information that is aggregated for a single taker order.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#aggregate-trade-streams
    """
    stream_name = "{}@aggTrade".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def trade(
        self,
        symbol: str,
        subscription: bool = True,
        _id: int | None = None
):
    """
    The Trade Streams push raw trade information; each trade has a unique buyer and seller.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#trade-streams
    """
    stream_name = "{}@trade".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def kline(
        self,
        symbol: str,
        interval: Literal[
            "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M"],
        subscription: bool = True,
        _id: int | None = None
):
    """
    The Kline/Candlestick Stream push updates to the current klines/candlestick every second in UTC+0 timezone
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#klinecandlestick-streams-for-utc
    """
    stream_name = "{}@kline_{}".format(symbol.lower(), interval)
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def ui_kline(
        self,
        symbol: str,
        interval: Literal[
            "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M"],
        subscription: bool = True,
        _id: int | None = None
):
    """
    The Kline/Candlestick Stream push updates to the current klines/candlestick every second in UTC+8 timezone
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#klinecandlestick-streams-with-timezone-offset
    """
    stream_name = "{}@kline_{}@+08:00".format(symbol.lower(), interval)
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def mini_ticker(
        self,
        symbol: str,
        subscription: bool = True,
        _id: int | None = None
):
    """
    24hr rolling window mini-ticker statistics. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-mini-ticker-stream
    """
    stream_name = "{}@miniTicker".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def mini_ticker_arr(
        self,
        subscription: bool = True,
        _id: int | None = None
):
    """
    24hr rolling window mini-ticker statistics for all symbols that changed in an array. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs. Note that only tickers that have changed will be present in the array.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-mini-tickers-stream
    """
    stream_name = "!miniTicker@arr"
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def ticker(
        self,
        symbol: str,
        subscription: bool = True,
        _id: int | None = None
):
    """
    24hr rolling window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-ticker-streams
    """
    stream_name = "{}@ticker".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def ticker_arr(
        self,
        subscription: bool = True,
        _id: int | None = None
):
    """
    24hr rolling window ticker statistics for all symbols that changed in an array. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs. Note that only tickers that have changed will be present in the array.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-tickers-stream
    """
    stream_name = "!ticker@arr"
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def ticker_window(
        self,
        symbol: str,
        window_size: Literal["1h", "4h", "1d"],
        subscription: bool = True,
        _id: int | None = None
):
    """
    Rolling window ticker statistics for a single symbol, computed over multiple windows.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-rolling-window-statistics-streams
    """
    stream_name = "{}@ticker_{}".format(symbol.lower(), window_size)
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def ticker_window_arr(
        self,
        window_size: Literal["1h", "4h", "1d"],
        subscription: bool = True,
        _id: int | None = None
):
    """
    Rolling window ticker statistics for all market symbols, computed over multiple windows. Note that only tickers that have changed will be present in the array.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-rolling-window-statistics-streams
    """
    stream_name = "!ticker_{}@arr".format(window_size)
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def book_ticker(
        self,
        symbol: str,
        subscription: bool = True,
        _id: int | None = None
):
    """
    Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol. Multiple <symbol>@bookTicker streams can be subscribed to over one connection.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-book-ticker-streams
    """
    stream_name = "{}@bookTicker".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def avg_price(
        self,
        symbol: str,
        subscription: bool = True,
        _id: int | None = None
):
    """
    Average price streams push changes in the average price over a fixed time interval.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#average-price
    """
    stream_name = "{}@avgPrice".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def depth(
        self,
        symbol: str,
        levels: Literal[5, 10, 20],
        subscription: bool = True,
        _id: int | None = None
):
    """
    Top <levels> bids and asks, pushed every second. Valid <levels> are 5, 10, or 20.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#partial-book-depth-streams
    """
    stream_name = "{}@depth{}".format(symbol.lower(), levels)
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def diff_depth(
        self,
        symbol: str,
        subscription: bool = True,
        _id: int | None = None
):
    """
    Order book price and quantity depth updates used to locally manage an order book.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#diff-depth-stream
    """
    stream_name = "{}@depth".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def order_book_api(
        self,
        symbol: str,
        limit: int = 100,
        _id: int | None = None
):
    """
    Get current order book.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/market-data-requests
    """
    payload = {
        "symbol": symbol,
        "limit": limit
    }
    await self.send("depth", params=payload, _id=_id)
    return


async def recent_trades_api(
        self,
        symbol: str,
        limit: int = 100,
        _id: int | None = None
):
    """
    Get recent trades.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/market-data-requests#recent-trades
    """
    payload = {
        "symbol": symbol,
        "limit": limit
    }
    await self.send("trades.recent", params=payload, _id=_id)
    return


async def historical_trades_api(
        self,
        symbol: str,
        _id: int | None = None,
        **kwargs
):
    """
    Get historical trades.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/market-data-requests#historical-trades
    """
    payload = {
        "symbol": symbol,
        **kwargs
    }

    return await self.send("trades.historical", params=payload, _id=_id)


async def agg_trades_api(
        self,
        symbol: str,
        _id: int | None = None,
        **kwargs
):
    """
    Get aggregate trades.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/market-data-requests#aggregate-trades
    """
    payload = {
        "symbol": symbol,
        **kwargs
    }
    return await self.send("trades.aggregate", params=payload, _id=_id)


async def klines_api(
        self,
        symbol: str,
        interval: Interval,
        _id: int | None = None,
        **kwargs
):
    """
    Get klines (candlestick bars).
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/market-data-requests#klines
    """
    payload = {
        "symbol": symbol,
        "interval": interval.value,
        **kwargs
    }
    return await self.send("klines", params=payload, _id=_id)


async def ui_klines_api(
        self,
        symbol: str,
        interval: Interval,
        _id: int | None = None,
        **kwargs
):
    """
    Get klines (candlestick bars) optimized for presentation.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/market-data-requests#ui-klines
    """
    payload = {
        "symbol": symbol,
        "interval": interval.value,
        **kwargs
    }
    return await self.send("uiKlines", params=payload, _id=_id)


async def avg_price_api(
        self,
        symbol: str,
        _id: int | None = None,
):
    """
    Get current average price for a symbol.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/market-data-requests#current-average-price
    """
    payload = {
        "symbol": symbol,
    }
    return await self.send("avgPrice", params=payload, _id=_id)


async def ticker_24hr_api(
        self,
        symbol: str,
        _id: int | None = None,
):
    """
    Get 24-hour rolling window price change statistics.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/market-data-requests#24hr-ticker-price-change-statistics
    """
    payload = {
        "symbol": symbol,
    }
    return await self.send("ticker.24hr", params=payload, _id=_id)


async def ticker_trading_day_api(
        self,
        symbol: str | list[str],
        _id: int | None = None,
):
    """
    Price change statistics for a trading day.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/market-data-requests#trading-day-ticker
    """
    payload = {}
    if isinstance(symbol, str):
        payload["symbol"] = symbol
    else:
        payload["symbols"] = symbol
    return await self.send("ticker.tradingDay", params=payload, _id=_id)


async def ticker_api(
        self,
        symbol: str | list[str],
        _id: int | None = None,
        **kwargs
):
    """
    Get rolling window price change statistics with a custom window.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/market-data-requests#rolling-window-price-change-statistics
    """
    payload = {
        **kwargs
    }
    if isinstance(symbol, str):
        payload["symbol"] = symbol
    else:
        payload["symbols"] = symbol
    return await self.send("ticker", params=payload, _id=_id)


async def ticker_price_api(
        self,
        symbol: str | list[str],
        _id: int | None = None,
):
    """
    Get the latest market price for a symbol.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/market-data-requests#symbol-price-ticker
    """
    payload = {}
    if isinstance(symbol, str):
        payload["symbol"] = symbol
    else:
        payload["symbols"] = symbol
    return await self.send("ticker.price", params=payload, _id=_id)


async def ticker_book_api(
        self,
        symbol: str | list[str],
        _id: int | None = None,
):
    """
    Get the current best price and quantity on the order book.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/market-data-requests#symbol-order-book-ticker
    """
    payload = {}
    if isinstance(symbol, str):
        payload["symbol"] = symbol
    else:
        payload["symbols"] = symbol
    return await self.send("ticker.book", params=payload, _id=_id)


async def session_logon_api(
        self,
        _id: int | None = None,
        **kwargs
):
    """
    Authenticate WebSocket connection using the provided API key.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/authentication-requests#log-in-with-api-key-signed
    """
    payload = {
        "apiKey": self.key,
        "timestamp": self._clock.timestamp_ms(),
        **kwargs
    }
    encoded_payload = urlencode(payload)
    payload["signature"] = ed_25519(self.private_key, encoded_payload, self.private_key_passphrase)
    return await self.send("session.logon", params=payload, _id=_id)


async def session_status_api(
        self,
        _id: int | None = None,
):
    """
    Query the status of the WebSocket connection, inspecting which API key (if any) is used to authorize requests.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/authentication-requests#query-session-status
    """
    return await self.send("session.status", _id=_id)


async def session_logout_api(
        self,
        _id: int | None = None,
):
    """
    Forget the API key previously authenticated. If the connection is not authenticated, this request does nothing.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/authentication-requests#log-out-of-the-session
    """
    return await self.send("session.logout", _id=_id)


async def order_place_api(
        self,
        symbol: str,
        side: Literal["BUY", "SELL"],
        _type: OrderType,
        _id: int | None = None,
        sign: bool = False,
        **kwargs
):
    """
    Send in a new order.
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/trading-requests
    """
    payload = {
        "symbol": symbol,
        "side": side,
        "type": _type.value,
        "timestamp": self._clock.timestamp_ms(),
        **kwargs
    }
    if sign:
        payload["apiKey"] = self.key
        encoded_payload = urlencode(payload)
        payload["signature"] = self._get_sign(encoded_payload)
    return await self.send("order.place", params=payload, _id=_id)
