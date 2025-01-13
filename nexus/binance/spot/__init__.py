from typing import Literal, Callable, Any

from nexus.binance.base import BinanceApiClient, BinanceWSClient
from nexus.binance.constants import BinanceUrl, ALL_URL, BinanceInstrumentType


class SpotTradingApi(BinanceApiClient):
    def __init__(
            self,
            key=None,
            secret=None,
            binance_url: Literal[BinanceUrl.MAIN, BinanceUrl.TEST] = BinanceUrl.MAIN,
            **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = ALL_URL[BinanceInstrumentType.SPOT].get_url(binance_url)
        super().__init__(key=key, secret=secret, **kwargs)

    # General endpoints
    from nexus.binance.spot.general import get_api_v3_ping
    from nexus.binance.spot.general import get_api_v3_time
    from nexus.binance.spot.general import get_api_v3_exchangeInfo

    # Market Data endpoints
    from nexus.binance.spot.market_data import get_api_v3_depth
    from nexus.binance.spot.market_data import get_api_v3_trades
    from nexus.binance.spot.market_data import get_api_v3_historical_trades
    from nexus.binance.spot.market_data import get_api_v3_klines
    from nexus.binance.spot.market_data import get_api_v3_ui_klines
    from nexus.binance.spot.market_data import get_api_v3_avgPrice
    from nexus.binance.spot.market_data import get_api_v3_ticker_24hr
    from nexus.binance.spot.market_data import get_api_v3_ticker_tradingDay
    from nexus.binance.spot.market_data import get_api_v3_ticker_price
    from nexus.binance.spot.market_data import get_api_v3_ticker_bookTicker
    from nexus.binance.spot.market_data import get_api_v3_ticker

    # Trading endpoints
    from nexus.binance.spot.trading import post_api_v3_order
    from nexus.binance.spot.trading import post_api_v3_order_test
    from nexus.binance.spot.trading import get_api_v3_order
    from nexus.binance.spot.trading import delete_api_v3_order
    from nexus.binance.spot.trading import delete_api_v3_open_orders
    from nexus.binance.spot.trading import post_api_v3_order_cancel_replace
    from nexus.binance.spot.trading import get_api_v3_open_orders
    from nexus.binance.spot.trading import get_api_v3_all_orders
    from nexus.binance.spot.trading import post_api_v3_order_oco
    from nexus.binance.spot.trading import post_api_v3_sor_order

    # Account Endpoints
    from nexus.binance.spot.account import get_api_v3_account
    from nexus.binance.spot.account import get_api_v3_my_trades
    from nexus.binance.spot.account import get_api_v3_rate_limit_order
    from nexus.binance.spot.account import get_api_v3_my_prevented_matches
    from nexus.binance.spot.account import get_api_v3_my_allocations
    from nexus.binance.spot.account import get_api_v3_account_commission

    # User data stream endpoints
    from nexus.binance.spot.user_data_stream import post_api_v3_user_data_stream
    from nexus.binance.spot.user_data_stream import put_api_v3_user_data_stream
    from nexus.binance.spot.user_data_stream import delete_api_v3_user_data_stream


class BinanceSpotWSClient(BinanceWSClient):
    def __init__(
            self,
            handler: Callable[..., Any],
            key=None,
            secret=None,
            listen_key=None,
            binance_url: Literal[BinanceUrl.WS, BinanceUrl.TEST_WS] = BinanceUrl.WS,
            **kwargs
    ):
        if "base_url" not in kwargs:
            self.baseUrl = ALL_URL[BinanceInstrumentType.SPOT].get_url(binance_url)
        else:
            self.baseUrl = kwargs["base_url"]
            kwargs.pop("base_url", None)
        if listen_key:
            self.baseUrl = f"{self.baseUrl}/{listen_key}"
        super().__init__(url=self.baseUrl, handler=handler, **kwargs)

    # wss://stream.binance.com:443
    from nexus.binance.spot.web_socket_stream import agg_trade
    from nexus.binance.spot.web_socket_stream import trade
    from nexus.binance.spot.web_socket_stream import kline
    from nexus.binance.spot.web_socket_stream import ui_kline
    from nexus.binance.spot.web_socket_stream import mini_ticker
    from nexus.binance.spot.web_socket_stream import mini_ticker_arr
    from nexus.binance.spot.web_socket_stream import ticker
    from nexus.binance.spot.web_socket_stream import ticker_arr
    from nexus.binance.spot.web_socket_stream import ticker_window
    from nexus.binance.spot.web_socket_stream import ticker_window_arr
    from nexus.binance.spot.web_socket_stream import book_ticker
    from nexus.binance.spot.web_socket_stream import avg_price
    from nexus.binance.spot.web_socket_stream import depth
    from nexus.binance.spot.web_socket_stream import diff_depth

    # wss://ws-api.binance.com:443/ws-api/v3
    from nexus.binance.spot.web_socket_stream import order_book
    from nexus.binance.spot.web_socket_stream import recent_trades
    from nexus.binance.spot.web_socket_stream import historical_trades
    from nexus.binance.spot.web_socket_stream import agg_trades
    from nexus.binance.spot.web_socket_stream import klines