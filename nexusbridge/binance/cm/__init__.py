from typing import Literal, Callable, Any

from nexusbridge.binance.base import BinanceApiClient, BinanceWSClient
from nexusbridge.binance.constants import (
    BinanceUrl,
    ALL_URL,
    BinanceInstrumentType,
    KeyType,
)


class CmTradingApi(BinanceApiClient):
    def __init__(
        self,
        key=None,
        secret=None,
        binance_url: Literal[BinanceUrl.MAIN, BinanceUrl.TEST] = BinanceUrl.MAIN,
        **kwargs,
    ):
        if "base_url" not in kwargs:
            kwargs["base_url"] = ALL_URL[BinanceInstrumentType.Derivatives_CM].get_url(
                binance_url
            )
        super().__init__(key=key, secret=secret, **kwargs)

    # General endpoints
    from nexusbridge.binance.cm.general import get_dapi_v1_exchangeInfo

    # Market Data endpoints
    from nexusbridge.binance.cm.market_data import get_dapi_v1_ping
    from nexusbridge.binance.cm.market_data import get_dapi_v1_time
    from nexusbridge.binance.cm.market_data import get_dapi_v1_exchange_info
    from nexusbridge.binance.cm.market_data import get_dapi_v1_depth
    from nexusbridge.binance.cm.market_data import get_dapi_v1_trades
    from nexusbridge.binance.cm.market_data import get_dapi_v1_historical_trades
    from nexusbridge.binance.cm.market_data import get_dapi_v1_agg_trades
    from nexusbridge.binance.cm.market_data import get_dapi_v1_premium_index
    from nexusbridge.binance.cm.market_data import get_dapi_v1_funding_rate
    from nexusbridge.binance.cm.market_data import get_dapi_v1_funding_info
    from nexusbridge.binance.cm.market_data import get_dapi_v1_klines
    from nexusbridge.binance.cm.market_data import get_dapi_v1_continuous_klines
    from nexusbridge.binance.cm.market_data import get_dapi_v1_index_price_klines
    from nexusbridge.binance.cm.market_data import get_dapi_v1_mark_price_klines
    from nexusbridge.binance.cm.market_data import get_dapi_v1_premium_index_klines
    from nexusbridge.binance.cm.market_data import get_dapi_v1_ticker_24hr
    from nexusbridge.binance.cm.market_data import get_dapi_v1_ticker_price
    from nexusbridge.binance.cm.market_data import get_dapi_v1_ticker_book_ticker
    from nexusbridge.binance.cm.market_data import get_dapi_v1_open_interest
    from nexusbridge.binance.cm.market_data import get_futures_data_open_interest_hist
    from nexusbridge.binance.cm.market_data import (
        get_futures_data_top_long_short_position_ratio,
    )
    from nexusbridge.binance.cm.market_data import (
        get_futures_data_top_long_short_account_ratio,
    )
    from nexusbridge.binance.cm.market_data import (
        get_futures_data_global_long_short_account_ratio,
    )
    from nexusbridge.binance.cm.market_data import get_futures_data_taker_buy_sell_vol
    from nexusbridge.binance.cm.market_data import get_futures_data_basis
    from nexusbridge.binance.cm.market_data import get_dapi_v1_constituents

    # Trade endpoints
    from nexusbridge.binance.cm.trade import post_dapi_v1_order
    from nexusbridge.binance.cm.trade import post_dapi_v1_batch_order
    from nexusbridge.binance.cm.trade import put_dapi_v1_order
    from nexusbridge.binance.cm.trade import put_dapi_v1_batch_order
    from nexusbridge.binance.cm.trade import get_dapi_v1_order_amendment
    from nexusbridge.binance.cm.trade import delete_dapi_v1_order
    from nexusbridge.binance.cm.trade import delete_dapi_v1_batch_order
    from nexusbridge.binance.cm.trade import delete_dapi_v1_all_open_orders
    from nexusbridge.binance.cm.trade import post_dapi_v1_countdown_cancel_all
    from nexusbridge.binance.cm.trade import get_dapi_v1_order
    from nexusbridge.binance.cm.trade import get_dapi_v1_all_orders
    from nexusbridge.binance.cm.trade import get_dapi_v1_open_orders
    from nexusbridge.binance.cm.trade import get_dapi_v1_open_order
    from nexusbridge.binance.cm.trade import get_dapi_v1_force_orders
    from nexusbridge.binance.cm.trade import get_dapi_v1_user_trades
    from nexusbridge.binance.cm.trade import get_dapi_v1_position_risk
    from nexusbridge.binance.cm.trade import post_dapi_v1_position_side_dual
    from nexusbridge.binance.cm.trade import post_dapi_v1_margin_type
    from nexusbridge.binance.cm.trade import post_dapi_v1_leverage
    from nexusbridge.binance.cm.trade import get_dapi_v1_adl_quantile
    from nexusbridge.binance.cm.trade import post_dapi_v1_position_margin
    from nexusbridge.binance.cm.trade import get_dapi_v1_position_margin_history

    # User Data Streams endpoints
    from nexusbridge.binance.cm.user_data_stream import post_dapi_v1_listen_key
    from nexusbridge.binance.cm.user_data_stream import put_dapi_v1_listen_key
    from nexusbridge.binance.cm.user_data_stream import delete_dapi_v1_listen_key

    # Account endpoints
    from nexusbridge.binance.cm.account import get_dapi_v1_balance
    from nexusbridge.binance.cm.account import get_dapi_v1_commission_rate
    from nexusbridge.binance.cm.account import get_dapi_v1_account
    from nexusbridge.binance.cm.account import get_dapi_v2_leverage_bracket
    from nexusbridge.binance.cm.account import get_dapi_v1_leverage_bracket
    from nexusbridge.binance.cm.account import get_dapi_v1_position_side_dual
    from nexusbridge.binance.cm.account import get_dapi_v1_income
    from nexusbridge.binance.cm.account import get_dapi_v1_income_asyn
    from nexusbridge.binance.cm.account import get_dapi_v1_income_asyn_id
    from nexusbridge.binance.cm.account import get_dapi_v1_order_asyn
    from nexusbridge.binance.cm.account import get_dapi_v1_order_asyn_id
    from nexusbridge.binance.cm.account import get_dapi_v1_trade_asyn
    from nexusbridge.binance.cm.account import get_dapi_v1_trade_asyn_id
    from nexusbridge.binance.cm.account import get_dapi_v1_pm_account_info


class CmTradingWebsocket(BinanceWSClient):
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
            self.baseUrl = ALL_URL[BinanceInstrumentType.Derivatives_CM].get_url(
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

    from nexusbridge.binance.cm.web_socket_stream import agg_trade
    from nexusbridge.binance.cm.web_socket_stream import index_price
    from nexusbridge.binance.cm.web_socket_stream import mark_price
    from nexusbridge.binance.cm.web_socket_stream import kline
    from nexusbridge.binance.cm.web_socket_stream import continuous_kline
    from nexusbridge.binance.cm.web_socket_stream import pair_mark_price
    from nexusbridge.binance.cm.web_socket_stream import index_price_kline
    from nexusbridge.binance.cm.web_socket_stream import mark_price_kline
    from nexusbridge.binance.cm.web_socket_stream import mini_ticker
    from nexusbridge.binance.cm.web_socket_stream import mini_ticker_arr
    from nexusbridge.binance.cm.web_socket_stream import ticker
    from nexusbridge.binance.cm.web_socket_stream import ticker_arr
    from nexusbridge.binance.cm.web_socket_stream import book_ticker
    from nexusbridge.binance.cm.web_socket_stream import book_ticker_arr
    from nexusbridge.binance.cm.web_socket_stream import force_orders
    from nexusbridge.binance.cm.web_socket_stream import force_orders_arr
    from nexusbridge.binance.cm.web_socket_stream import contract_info
    from nexusbridge.binance.cm.web_socket_stream import depth_levels
    from nexusbridge.binance.cm.web_socket_stream import diff_depth
