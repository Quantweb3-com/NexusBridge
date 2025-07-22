from typing import Literal, Callable, Any

from nexusbridge.binance.base import BinanceApiClient, BinanceWSClient
from nexusbridge.binance.constants import (
    BinanceUrl,
    ALL_URL,
    BinanceInstrumentType,
    KeyType,
)


class UmTradingApi(BinanceApiClient):
    def __init__(
        self,
        key=None,
        secret=None,
        binance_url: Literal[BinanceUrl.MAIN, BinanceUrl.TEST] = BinanceUrl.MAIN,
        **kwargs,
    ):
        if "base_url" not in kwargs:
            kwargs["base_url"] = ALL_URL[BinanceInstrumentType.Derivatives_UM].get_url(
                binance_url
            )
        super().__init__(key=key, secret=secret, **kwargs)

    # General endpoints
    from nexusbridge.binance.um.general import get_fapi_v1_exchangeInfo

    # Market Data endpoints
    from nexusbridge.binance.um.market_data import get_fapi_v1_ping
    from nexusbridge.binance.um.market_data import get_fapi_v1_time
    from nexusbridge.binance.um.market_data import get_fapi_v1_exchange_info
    from nexusbridge.binance.um.market_data import get_fapi_v1_depth
    from nexusbridge.binance.um.market_data import get_fapi_v1_trades
    from nexusbridge.binance.um.market_data import get_fapi_v1_historical_trades
    from nexusbridge.binance.um.market_data import get_fapi_v1_agg_trades
    from nexusbridge.binance.um.market_data import get_fapi_v1_klines
    from nexusbridge.binance.um.market_data import get_fapi_v1_continuous_klines
    from nexusbridge.binance.um.market_data import get_fapi_v1_index_price_klines
    from nexusbridge.binance.um.market_data import get_fapi_v1_mark_price_klines
    from nexusbridge.binance.um.market_data import get_fapi_v1_premium_index_klines
    from nexusbridge.binance.um.market_data import get_fapi_v1_premium_index
    from nexusbridge.binance.um.market_data import get_fapi_v1_funding_rate
    from nexusbridge.binance.um.market_data import get_fapi_v1_funding_info
    from nexusbridge.binance.um.market_data import get_fapi_v1_ticker_24hr
    from nexusbridge.binance.um.market_data import get_fapi_v1_ticker_price
    from nexusbridge.binance.um.market_data import get_fapi_v2_ticker_price
    from nexusbridge.binance.um.market_data import get_fapi_v1_book_ticker
    from nexusbridge.binance.um.market_data import get_fapi_v1_delivery_price
    from nexusbridge.binance.um.market_data import get_fapi_v1_open_interest
    from nexusbridge.binance.um.market_data import get_fapi_v1_open_interest_hist
    from nexusbridge.binance.um.market_data import (
        get_futures_data_top_long_short_position_ratio,
    )
    from nexusbridge.binance.um.market_data import (
        get_futures_data_top_long_short_account_ratio,
    )
    from nexusbridge.binance.um.market_data import (
        get_futures_data_global_long_short_account_ratio,
    )
    from nexusbridge.binance.um.market_data import (
        get_futures_data_taker_long_short_ratio,
    )
    from nexusbridge.binance.um.market_data import get_fapi_v1_lvt_klines
    from nexusbridge.binance.um.market_data import get_fapi_v1_index_info
    from nexusbridge.binance.um.market_data import get_fapi_v1_asset_index
    from nexusbridge.binance.um.market_data import get_fapi_v1_constituents

    # Trading endpoints
    from nexusbridge.binance.um.trade import post_fapi_v1_order
    from nexusbridge.binance.um.trade import post_fapi_v1_batch_order
    from nexusbridge.binance.um.trade import put_fapi_v1_order
    from nexusbridge.binance.um.trade import put_fapi_v1_batch_order
    from nexusbridge.binance.um.trade import get_fapi_v1_order_amendment
    from nexusbridge.binance.um.trade import delete_fapi_v1_order
    from nexusbridge.binance.um.trade import delete_fapi_v1_batch_order
    from nexusbridge.binance.um.trade import delete_fapi_v1_all_open_orders
    from nexusbridge.binance.um.trade import post_fapi_v1_countdown_cancel_all
    from nexusbridge.binance.um.trade import get_fapi_v1_order
    from nexusbridge.binance.um.trade import get_fapi_v1_all_orders
    from nexusbridge.binance.um.trade import get_fapi_v1_open_orders
    from nexusbridge.binance.um.trade import get_fapi_v1_open_order
    from nexusbridge.binance.um.trade import get_fapi_v1_force_orders
    from nexusbridge.binance.um.trade import get_fapi_v1_user_trades
    from nexusbridge.binance.um.trade import post_fapi_v1_margin_type
    from nexusbridge.binance.um.trade import post_fapi_v1_position_side_dual
    from nexusbridge.binance.um.trade import post_fapi_v1_leverage
    from nexusbridge.binance.um.trade import post_fapi_v1_multi_assets_margin
    from nexusbridge.binance.um.trade import post_fapi_v1_position_margin
    from nexusbridge.binance.um.trade import get_fapi_v2_position_risk
    from nexusbridge.binance.um.trade import get_fapi_v3_position_risk
    from nexusbridge.binance.um.trade import get_fapi_v1_adl_quantile
    from nexusbridge.binance.um.trade import get_fapi_v1_position_margin_history
    from nexusbridge.binance.um.trade import post_fapi_v1_order_test

    # User Data Streams endpoints
    from nexusbridge.binance.um.user_data_stream import post_fapi_v1_listen_key
    from nexusbridge.binance.um.user_data_stream import put_fapi_v1_listen_key
    from nexusbridge.binance.um.user_data_stream import delete_fapi_v1_listen_key

    # Account endpoints
    from nexusbridge.binance.um.account import get_fapi_v3_balance
    from nexusbridge.binance.um.account import get_fapi_v2_balance
    from nexusbridge.binance.um.account import get_fapi_v3_account
    from nexusbridge.binance.um.account import get_fapi_v2_account
    from nexusbridge.binance.um.account import get_fapi_v1_commission_rate
    from nexusbridge.binance.um.account import get_fapi_v1_account_config
    from nexusbridge.binance.um.account import get_fapi_v1_symbol_config
    from nexusbridge.binance.um.account import get_fapi_v1_rate_limit_order
    from nexusbridge.binance.um.account import get_fapi_v1_leverage_bracket
    from nexusbridge.binance.um.account import get_fapi_v1_multi_assets_margin
    from nexusbridge.binance.um.account import get_fapi_v1_position_side_dual
    from nexusbridge.binance.um.account import get_fapi_v1_income
    from nexusbridge.binance.um.account import get_fapi_v1_api_trading_status
    from nexusbridge.binance.um.account import get_fapi_v1_income_asyn
    from nexusbridge.binance.um.account import get_fapi_v1_income_asyn_id
    from nexusbridge.binance.um.account import get_fapi_v1_order_asyn
    from nexusbridge.binance.um.account import get_fapi_v1_order_asyn_id
    from nexusbridge.binance.um.account import get_fapi_v1_trade_asyn
    from nexusbridge.binance.um.account import get_fapi_v1_trade_asyn_id
    from nexusbridge.binance.um.account import post_fapi_v1_fee_burn
    from nexusbridge.binance.um.account import get_fapi_v1_fee_burn
    from nexusbridge.binance.um.account import get_fapi_v1_pm_account_info

    # Convert endpoints
    from nexusbridge.binance.um.convert import get_fapi_v1_convert_exchange_info
    from nexusbridge.binance.um.convert import post_fapi_v1_convert_get_quote
    from nexusbridge.binance.um.convert import post_fapi_v1_convert_accept_quote
    from nexusbridge.binance.um.convert import get_fapi_v1_convert_order_status


class UmTradingWebsocket(BinanceWSClient):
    def __init__(
        self,
        handler: Callable[..., Any],
        key=None,
        secret=None,
        listen_key=None,
        private_key=None,
        private_key_passphrase=None,
        key_type: KeyType = KeyType.HMAC,
        binance_url: Literal[
            BinanceUrl.WS, BinanceUrl.TEST_WS, BinanceUrl.WS_STREAM
        ] = BinanceUrl.WS_STREAM,
        **kwargs,
    ):
        if "base_url" not in kwargs:
            self.baseUrl = ALL_URL[BinanceInstrumentType.Derivatives_UM].get_url(
                binance_url
            )
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

    # wss://ws-fapi.binance.com/ws-fapi/v1
    from nexusbridge.binance.um.web_socket_stream import depth
    from nexusbridge.binance.um.web_socket_stream import ticker_price
    from nexusbridge.binance.um.web_socket_stream import ticker_book
    from nexusbridge.binance.um.web_socket_stream import order_place
    from nexusbridge.binance.um.web_socket_stream import order_modify
    from nexusbridge.binance.um.web_socket_stream import order_cancel
    from nexusbridge.binance.um.web_socket_stream import order_status
    from nexusbridge.binance.um.web_socket_stream import account_position_v2
    from nexusbridge.binance.um.web_socket_stream import account_position
    from nexusbridge.binance.um.web_socket_stream import user_data_stream_start
    from nexusbridge.binance.um.web_socket_stream import user_data_stream_ping
    from nexusbridge.binance.um.web_socket_stream import user_data_stream_stop
    from nexusbridge.binance.um.web_socket_stream import account_balance_v2
    from nexusbridge.binance.um.web_socket_stream import account_balance
    from nexusbridge.binance.um.web_socket_stream import account_status_v2
    from nexusbridge.binance.um.web_socket_stream import account_status

    # wss://fstream.binance.com/ws
    from nexusbridge.binance.um.web_socket_stream import agg_trade
    from nexusbridge.binance.um.web_socket_stream import mark_price
    from nexusbridge.binance.um.web_socket_stream import mark_price_arr
    from nexusbridge.binance.um.web_socket_stream import kline
    from nexusbridge.binance.um.web_socket_stream import continuous_kline
    from nexusbridge.binance.um.web_socket_stream import mini_ticker
    from nexusbridge.binance.um.web_socket_stream import ticker_arr
    from nexusbridge.binance.um.web_socket_stream import ticker
    from nexusbridge.binance.um.web_socket_stream import mini_ticker_arr
    from nexusbridge.binance.um.web_socket_stream import book_ticker
    from nexusbridge.binance.um.web_socket_stream import book_ticker_arr
    from nexusbridge.binance.um.web_socket_stream import force_orders
    from nexusbridge.binance.um.web_socket_stream import force_orders_arr
    from nexusbridge.binance.um.web_socket_stream import depth_levels
    from nexusbridge.binance.um.web_socket_stream import diff_depth
    from nexusbridge.binance.um.web_socket_stream import composite_index
    from nexusbridge.binance.um.web_socket_stream import contract_info
    from nexusbridge.binance.um.web_socket_stream import asset_index
