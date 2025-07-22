from typing import Literal
from urllib.parse import urlencode

from nexusbridge.binance.constants import OrderType


async def depth(self, symbol: str, _id: int | None = None, **kwargs):
    """
    Get current order book. Note that this request returns limited market depth
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/websocket-api
    """
    payload = {"symbol": symbol, **kwargs}
    return await self.send("depth", params=payload, _id=_id)


async def ticker_price(self, _id: int | None = None, **kwargs):
    """
    Latest price for a symbol or symbols.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Price-Ticker
    """
    payload = {**kwargs}
    return await self.send("ticker.price", params=payload, _id=_id)


async def ticker_book(self, _id: int | None = None, **kwargs):
    """
    Best price/qty on the order book for a symbol or symbols.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker
    """
    payload = {**kwargs}
    return await self.send("ticker.book", params=payload, _id=_id)


async def order_place(
    self,
    symbol: str,
    side: Literal["BUY", "SELL"],
    _type: OrderType,
    _id: int | None = None,
    **kwargs,
):
    """
    Send in a new order.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api
    """
    payload = {
        "apiKey": self.key,
        "symbol": symbol,
        "side": side,
        "type": _type.value,
        "timestamp": self._clock.timestamp_ms(),
        **kwargs,
    }
    encoded_payload = urlencode(payload)
    payload["signature"] = self._get_sign(encoded_payload)
    return await self.send("order.place", params=payload, _id=_id)


async def order_modify(
    self,
    symbol: str,
    side: Literal["BUY", "SELL"],
    _type: OrderType,
    quantity: float,
    price: float,
    _id: int | None = None,
    **kwargs,
):
    """
    Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Modify-Order
    """
    payload = {
        "apiKey": self.key,
        "symbol": symbol,
        "side": side,
        "type": _type.value,
        "quantity": quantity,
        "price": price,
        "timestamp": self._clock.timestamp_ms(),
        **kwargs,
    }
    encoded_payload = urlencode(payload)
    payload["signature"] = self._get_sign(encoded_payload)
    return await self.send("order.modify", params=payload, _id=_id)


async def order_cancel(self, symbol: str, _id: int | None = None, **kwargs):
    """
    Cancel an active order.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order
    """
    payload = {
        "apiKey": self.key,
        "symbol": symbol,
        "timestamp": self._clock.timestamp_ms(),
        **kwargs,
    }
    encoded_payload = urlencode(payload)
    payload["signature"] = self._get_sign(encoded_payload)
    return await self.send("order.cancel", params=payload, _id=_id)


async def order_status(self, symbol: str, _id: int | None = None, **kwargs):
    """
    Check an order's status.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Query-Order
    """
    payload = {
        "apiKey": self.key,
        "symbol": symbol,
        "timestamp": self._clock.timestamp_ms(),
        **kwargs,
    }
    encoded_payload = urlencode(payload)
    payload["signature"] = self._get_sign(encoded_payload)
    return await self.send("order.status", params=payload, _id=_id)


async def account_position_v2(self, _id: int | None = None, **kwargs):
    """
    Get current position information(only symbol that has position or open orders will be returned).
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Info-V2
    """
    payload = {"apiKey": self.key, "timestamp": self._clock.timestamp_ms(), **kwargs}
    encoded_payload = urlencode(payload)
    payload["signature"] = self._get_sign(encoded_payload)
    return await self.send("v2/account.position", params=payload, _id=_id)


async def account_position(self, _id: int | None = None, **kwargs):
    """
    Get current position information.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Information
    """
    payload = {"apiKey": self.key, "timestamp": self._clock.timestamp_ms(), **kwargs}
    encoded_payload = urlencode(payload)
    payload["signature"] = self._get_sign(encoded_payload)
    return await self.send("account.position", params=payload, _id=_id)


async def user_data_stream_start(
    self,
    _id: int | None = None,
):
    """
    Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp
    """
    payload = {
        "apiKey": self.key,
    }
    return await self.send("userDataStream.start", params=payload, _id=_id)


async def user_data_stream_ping(
    self,
    listen_key: str,
    _id: int | None = None,
):
    """
    Keepalive a user data stream to prevent a timeout. User data streams will close after 60 minutes. It's recommended to send a ping about every 30 minutes.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Ping-Pong
    """
    payload = {
        "listenKey": listen_key,
        "apiKey": self.key,
    }
    return await self.send("userDataStream.ping", params=payload, _id=_id)


async def user_data_stream_stop(
    self,
    listen_key: str,
    _id: int | None = None,
):
    """
    Close out a user data stream.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp
    """
    payload = {
        "listenKey": listen_key,
        "apiKey": self.key,
    }
    return await self.send("userDataStream.stop", params=payload, _id=_id)


async def account_balance_v2(self, _id: int | None = None, **kwargs):
    """
    Query account balance info
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/websocket-api
    """
    payload = {"apiKey": self.key, "timestamp": self._clock.timestamp_ms(), **kwargs}
    encoded_payload = urlencode(payload)
    payload["signature"] = self._get_sign(encoded_payload)
    return await self.send("account.balance", params=payload, _id=_id)


async def account_balance(self, _id: int | None = None, **kwargs):
    """
    Query account balance info
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/websocket-api/Futures-Account-Balance
    """
    payload = {"apiKey": self.key, "timestamp": self._clock.timestamp_ms(), **kwargs}
    encoded_payload = urlencode(payload)
    payload["signature"] = self._get_sign(encoded_payload)
    return await self.send("account.balance", params=payload, _id=_id)


async def account_status_v2(self, _id: int | None = None, **kwargs):
    """
    Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2
    """
    payload = {"apiKey": self.key, "timestamp": self._clock.timestamp_ms(), **kwargs}
    encoded_payload = urlencode(payload)
    payload["signature"] = self._get_sign(encoded_payload)
    return await self.send("account.status", params=payload, _id=_id)


async def account_status(self, _id: int | None = None, **kwargs):
    """
    Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/websocket-api/Account-Information
    """
    payload = {"apiKey": self.key, "timestamp": self._clock.timestamp_ms(), **kwargs}
    encoded_payload = urlencode(payload)
    payload["signature"] = self._get_sign(encoded_payload)
    return await self.send("account.status", params=payload, _id=_id)


async def agg_trade(
    self, symbol: str, subscription: bool = True, _id: int | None = None
):
    """
    The Aggregate Trade Streams push market trade information that is aggregated for fills with same price and taking side every 100 milliseconds. Only market trades will be aggregated, which means the insurance fund trades and ADL trades won't be aggregated.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams
    """
    stream_name = "{}@aggTrade".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def mark_price(
    self, symbol: str, subscription: bool = True, _id: int | None = None
):
    """
    Mark price and funding rate for a single symbol pushed every 3 seconds or every second.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream
    """
    stream_name = "{}@markPrice".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def mark_price_arr(self, subscription: bool = True, _id: int | None = None):
    """
    Mark price and funding rate for all symbols pushed every 3 seconds or every second.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market
    """
    stream_name = "!markPrice@arr"
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
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams
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
    Continuous Contract Kline/Candlestick Streams
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Continuous-Contract-Kline-Candlestick-Streams
    """
    stream_name = "{}_{}@continuousKline_{}".format(
        pair.lower(), contract_type, interval
    )
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def mini_ticker(
    self, symbol: str, subscription: bool = True, _id: int | None = None
):
    """
    24hr rolling window mini-ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream
    """
    stream_name = "{}@miniTicker".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def ticker_arr(self, subscription: bool = True, _id: int | None = None):
    """
    24hr rolling window ticker statistics for all symbols. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before. Note that only tickers that have changed will be present in the array.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Tickers-Streams
    """
    stream_name = "!ticker@arr"
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def ticker(self, symbol: str, subscription: bool = True, _id: int | None = None):
    """
    24hr rolling window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams
    """
    stream_name = "{}@ticker".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def mini_ticker_arr(self, subscription: bool = True, _id: int | None = None):
    """
    24hr rolling window mini-ticker statistics for all symbols. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before. Note that only tickers that have changed will be present in the array.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream
    """
    stream_name = "!miniTicker@arr"
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def book_ticker(
    self, symbol: str | list[str], subscription: bool = True, _id: int | None = None
):
    """
    Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams
    """
    if isinstance(symbol, list):
        stream_name = ["{}@bookTicker".format(s.lower()) for s in symbol]
    if isinstance(symbol, str):
        stream_name = "{}@bookTicker".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def book_ticker_arr(self, subscription: bool = True, _id: int | None = None):
    """
    Pushes any update to the best bid or ask's price or quantity in real-time for all symbols.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Book-Tickers-Stream
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
    The Liquidation Order Snapshot Streams push force liquidation order information for specific symbol. For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams
    """
    stream_name = "{}@forceOrder".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def force_orders_arr(self, subscription: bool = True, _id: int | None = None):
    """
    The All Liquidation Order Snapshot Streams push force liquidation order information for all symbols in the market. For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams
    """
    stream_name = "!forceOrder@arr"
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
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams
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
    ids and asks, pushed every 250 milliseconds, 500 milliseconds, 100 milliseconds (if existing)
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams
    """
    stream_name = "{}@depth".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def composite_index(
    self, symbol: str, subscription: bool = True, _id: int | None = None
):
    """
    Composite index information for index symbols pushed every second.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Composite-Index-Symbol-Information-Streams
    """
    stream_name = "{}@compositeIndex".format(symbol.lower())
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def contract_info(self, subscription: bool = True, _id: int | None = None):
    """
    ContractInfo stream pushes when contract info updates(listing/settlement/contract bracket update). bks field only shows up when bracket gets updated.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Contract-Info-Stream
    """
    stream_name = "!contractInfo"
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)


async def asset_index(self, subscription: bool = True, _id: int | None = None):
    """
    Asset index for multi-assets mode user
    https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Multi-Assets-Mode-Asset-Index
    """
    stream_name = "!assetIndex@arr"
    if subscription:
        await self._subscribe(stream_name, _id)
    else:
        await self._unsubscribe(stream_name, _id)
