from typing import Literal, Callable, Any

from nexusbridge.binance.base import BinanceApiClient, BinanceWSClient
from nexusbridge.binance.constants import (
    BinanceUrl,
    ALL_URL,
    BinanceInstrumentType,
    KeyType,
)


class SpotTradingApi(BinanceApiClient):
    def __init__(
        self,
        key=None,
        secret=None,
        binance_url: Literal[BinanceUrl.MAIN, BinanceUrl.TEST] = BinanceUrl.MAIN,
        **kwargs,
    ):
        if "base_url" not in kwargs:
            kwargs["base_url"] = ALL_URL[BinanceInstrumentType.SPOT].get_url(
                binance_url
            )
        super().__init__(key=key, secret=secret, **kwargs)

    # General endpoints
    from nexusbridge.binance.spot.general import get_api_v3_ping
    from nexusbridge.binance.spot.general import get_api_v3_time
    from nexusbridge.binance.spot.general import get_api_v3_exchangeInfo

    # Market Data endpoints
    from nexusbridge.binance.spot.market_data import get_api_v3_depth
    from nexusbridge.binance.spot.market_data import get_api_v3_trades
    from nexusbridge.binance.spot.market_data import get_api_v3_historical_trades
    from nexusbridge.binance.spot.market_data import get_api_v3_klines
    from nexusbridge.binance.spot.market_data import get_api_v3_ui_klines
    from nexusbridge.binance.spot.market_data import get_api_v3_avgPrice
    from nexusbridge.binance.spot.market_data import get_api_v3_ticker_24hr
    from nexusbridge.binance.spot.market_data import get_api_v3_ticker_tradingDay
    from nexusbridge.binance.spot.market_data import get_api_v3_ticker_price
    from nexusbridge.binance.spot.market_data import get_api_v3_ticker_bookTicker
    from nexusbridge.binance.spot.market_data import get_api_v3_ticker

    # Trading endpoints
    from nexusbridge.binance.spot.trading import post_api_v3_order
    from nexusbridge.binance.spot.trading import post_api_v3_order_test
    from nexusbridge.binance.spot.trading import get_api_v3_order
    from nexusbridge.binance.spot.trading import delete_api_v3_order
    from nexusbridge.binance.spot.trading import delete_api_v3_open_orders
    from nexusbridge.binance.spot.trading import post_api_v3_order_cancel_replace
    from nexusbridge.binance.spot.trading import get_api_v3_open_orders
    from nexusbridge.binance.spot.trading import get_api_v3_all_orders
    from nexusbridge.binance.spot.trading import post_api_v3_order_oco
    from nexusbridge.binance.spot.trading import post_api_v3_sor_order

    # Account Endpoints
    from nexusbridge.binance.spot.account import get_api_v3_account
    from nexusbridge.binance.spot.account import get_api_v3_my_trades
    from nexusbridge.binance.spot.account import get_api_v3_rate_limit_order
    from nexusbridge.binance.spot.account import get_api_v3_my_prevented_matches
    from nexusbridge.binance.spot.account import get_api_v3_my_allocations
    from nexusbridge.binance.spot.account import get_api_v3_account_commission

    # User data stream endpoints
    from nexusbridge.binance.spot.user_data_stream import post_api_v3_user_data_stream
    from nexusbridge.binance.spot.user_data_stream import put_api_v3_user_data_stream
    from nexusbridge.binance.spot.user_data_stream import delete_api_v3_user_data_stream


class BinanceSpotWSClient(BinanceWSClient):
    def __init__(
        self,
        handler: Callable[..., Any],
        key=None,
        secret=None,
        listen_key=None,
        private_key=None,
        private_key_passphrase=None,
        key_type: KeyType = KeyType.HMAC,
        binance_url: Literal[BinanceUrl.WS, BinanceUrl.TEST_WS] = BinanceUrl.WS,
        **kwargs,
    ):
        if "base_url" not in kwargs:
            self.baseUrl = ALL_URL[BinanceInstrumentType.SPOT].get_url(binance_url)
        else:
            self.baseUrl = kwargs["base_url"]
            kwargs.pop("base_url", None)
        if listen_key:
            self.baseUrl = f"{self.baseUrl}/{listen_key}"
        self.key = key
        self.secret = secret
        self.private_key = private_key
        self.private_key_passphrase = private_key_passphrase
        self.key_type = key_type
        super().__init__(
            url=self.baseUrl,
            key=key,
            key_type=self.key_type,
            handler=handler,
            private_key=self.private_key,
            private_key_passphrase=self.private_key_passphrase,
            secret=secret,
            **kwargs,
        )

    # wss://stream.binance.com:443
    from nexusbridge.binance.spot.web_socket_stream import agg_trade
    from nexusbridge.binance.spot.web_socket_stream import trade
    from nexusbridge.binance.spot.web_socket_stream import kline
    from nexusbridge.binance.spot.web_socket_stream import ui_kline
    from nexusbridge.binance.spot.web_socket_stream import mini_ticker
    from nexusbridge.binance.spot.web_socket_stream import mini_ticker_arr
    from nexusbridge.binance.spot.web_socket_stream import ticker
    from nexusbridge.binance.spot.web_socket_stream import ticker_arr
    from nexusbridge.binance.spot.web_socket_stream import ticker_window
    from nexusbridge.binance.spot.web_socket_stream import ticker_window_arr
    from nexusbridge.binance.spot.web_socket_stream import book_ticker
    from nexusbridge.binance.spot.web_socket_stream import avg_price
    from nexusbridge.binance.spot.web_socket_stream import depth
    from nexusbridge.binance.spot.web_socket_stream import diff_depth

    # wss://ws-api.binance.com:443/ws-api/v3
    from nexusbridge.binance.spot.web_socket_stream import order_book_api
    from nexusbridge.binance.spot.web_socket_stream import recent_trades_api
    from nexusbridge.binance.spot.web_socket_stream import historical_trades_api
    from nexusbridge.binance.spot.web_socket_stream import agg_trades_api
    from nexusbridge.binance.spot.web_socket_stream import klines_api
    from nexusbridge.binance.spot.web_socket_stream import ui_klines_api
    from nexusbridge.binance.spot.web_socket_stream import avg_price_api
    from nexusbridge.binance.spot.web_socket_stream import ticker_24hr_api
    from nexusbridge.binance.spot.web_socket_stream import ticker_trading_day_api
    from nexusbridge.binance.spot.web_socket_stream import ticker_api
    from nexusbridge.binance.spot.web_socket_stream import ticker_price_api
    from nexusbridge.binance.spot.web_socket_stream import ticker_book_api
    from nexusbridge.binance.spot.web_socket_stream import session_logon_api
    from nexusbridge.binance.spot.web_socket_stream import session_status_api
    from nexusbridge.binance.spot.web_socket_stream import session_logout_api
    from nexusbridge.binance.spot.web_socket_stream import order_place_api
    from nexusbridge.binance.spot.web_socket_stream import order_test_api
    from nexusbridge.binance.spot.web_socket_stream import order_status_api
    from nexusbridge.binance.spot.web_socket_stream import order_cancel_api
    from nexusbridge.binance.spot.web_socket_stream import order_cancel_replace_api
    from nexusbridge.binance.spot.web_socket_stream import open_orders_status_api
    from nexusbridge.binance.spot.web_socket_stream import open_orders_cancel_all_api
    from nexusbridge.binance.spot.web_socket_stream import order_list_place_api
    from nexusbridge.binance.spot.web_socket_stream import order_place
    from nexusbridge.binance.spot.web_socket_stream import account_status_api
    from nexusbridge.binance.spot.web_socket_stream import rate_limit_order_api
    from nexusbridge.binance.spot.web_socket_stream import all_orders_api
    from nexusbridge.binance.spot.web_socket_stream import all_order_lists_api
    from nexusbridge.binance.spot.web_socket_stream import my_trades_api
    from nexusbridge.binance.spot.web_socket_stream import my_prevented_matches_api
    from nexusbridge.binance.spot.web_socket_stream import my_allocations_api
    from nexusbridge.binance.spot.web_socket_stream import account_commission_api
