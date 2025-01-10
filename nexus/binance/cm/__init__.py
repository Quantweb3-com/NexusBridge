from typing import Literal, Callable, Any

from nexus.binance.base import BinanceApiClient, BinanceWSClient
from nexus.binance.constants import BinanceUrl, ALL_URL, BinanceInstrumentType


class CmTradingApi(BinanceApiClient):
    def __init__(
            self,
            key=None,
            secret=None,
            binance_url: Literal[BinanceUrl.MAIN, BinanceUrl.TEST] = BinanceUrl.MAIN,
            **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = ALL_URL[BinanceInstrumentType.Derivatives_CM].get_url(binance_url)
        super().__init__(key=key, secret=secret, **kwargs)

    # Market Data endpoints
    from nexus.binance.cm.market_data import get_dapi_v1_ping
    from nexus.binance.cm.market_data import get_dapi_v1_time
    from nexus.binance.cm.market_data import get_dapi_v1_exchange_info
    from nexus.binance.cm.market_data import get_dapi_v1_depth
    from nexus.binance.cm.market_data import get_dapi_v1_trades
    from nexus.binance.cm.market_data import get_dapi_v1_historical_trades
    from nexus.binance.cm.market_data import get_dapi_v1_agg_trades
    from nexus.binance.cm.market_data import get_dapi_v1_premium_index
    from nexus.binance.cm.market_data import get_dapi_v1_funding_rate
    from nexus.binance.cm.market_data import get_dapi_v1_funding_info
    from nexus.binance.cm.market_data import get_dapi_v1_klines
    from nexus.binance.cm.market_data import get_dapi_v1_continuous_klines
    from nexus.binance.cm.market_data import get_dapi_v1_index_price_klines
    from nexus.binance.cm.market_data import get_dapi_v1_mark_price_klines
    from nexus.binance.cm.market_data import get_dapi_v1_premium_index_klines
    from nexus.binance.cm.market_data import get_dapi_v1_ticker_24hr
    from nexus.binance.cm.market_data import get_dapi_v1_ticker_price
    from nexus.binance.cm.market_data import get_dapi_v1_ticker_book_ticker
    from nexus.binance.cm.market_data import get_dapi_v1_open_interest
    from nexus.binance.cm.market_data import get_futures_data_open_interest_hist
    from nexus.binance.cm.market_data import get_futures_data_top_long_short_position_ratio
    from nexus.binance.cm.market_data import get_futures_data_top_long_short_account_ratio
    from nexus.binance.cm.market_data import get_futures_data_global_long_short_account_ratio
    from nexus.binance.cm.market_data import get_futures_data_taker_buy_sell_vol
    from nexus.binance.cm.market_data import get_futures_data_basis
    from nexus.binance.cm.market_data import get_dapi_v1_constituents

    # Trade endpoints
    from nexus.binance.cm.trade import post_dapi_v1_order
    from nexus.binance.cm.trade import post_dapi_v1_batch_order
    from nexus.binance.cm.trade import put_dapi_v1_order
    from nexus.binance.cm.trade import put_dapi_v1_batch_order
    from nexus.binance.cm.trade import get_dapi_v1_order_amendment
    from nexus.binance.cm.trade import delete_dapi_v1_order
    from nexus.binance.cm.trade import delete_dapi_v1_batch_order
    from nexus.binance.cm.trade import delete_dapi_v1_all_open_orders
    from nexus.binance.cm.trade import post_dapi_v1_countdown_cancel_all
    from nexus.binance.cm.trade import get_dapi_v1_order
    from nexus.binance.cm.trade import get_dapi_v1_all_orders
    from nexus.binance.cm.trade import get_dapi_v1_open_orders
    from nexus.binance.cm.trade import get_dapi_v1_open_order
    from nexus.binance.cm.trade import get_dapi_v1_force_orders
    from nexus.binance.cm.trade import get_dapi_v1_user_trades
    from nexus.binance.cm.trade import get_dapi_v1_position_risk
    from nexus.binance.cm.trade import post_dapi_v1_position_side_dual
    from nexus.binance.cm.trade import post_dapi_v1_margin_type
    from nexus.binance.cm.trade import post_dapi_v1_leverage
    from nexus.binance.cm.trade import get_dapi_v1_adl_quantile
    from nexus.binance.cm.trade import post_dapi_v1_position_margin
    from nexus.binance.cm.trade import get_dapi_v1_position_margin_history

    # User Data Streams endpoints
    from nexus.binance.cm.user_data_stream import post_dapi_v1_listen_key
    from nexus.binance.cm.user_data_stream import put_dapi_v1_listen_key
    from nexus.binance.cm.user_data_stream import delete_dapi_v1_listen_key

    # Account endpoints
    from nexus.binance.cm.account import get_dapi_v1_balance
    from nexus.binance.cm.account import get_dapi_v1_commission_rate
    from nexus.binance.cm.account import get_dapi_v1_account
    from nexus.binance.cm.account import get_dapi_v2_leverage_bracket
    from nexus.binance.cm.account import get_dapi_v1_leverage_bracket
    from nexus.binance.cm.account import get_dapi_v1_position_side_dual
    from nexus.binance.cm.account import get_dapi_v1_income
    from nexus.binance.cm.account import get_dapi_v1_income_asyn
    from nexus.binance.cm.account import get_dapi_v1_income_asyn_id
    from nexus.binance.cm.account import get_dapi_v1_order_asyn
    from nexus.binance.cm.account import get_dapi_v1_order_asyn_id
    from nexus.binance.cm.account import get_dapi_v1_trade_asyn
    from nexus.binance.cm.account import get_dapi_v1_trade_asyn_id
    from nexus.binance.cm.account import get_dapi_v1_pm_account_info


class CmTradingWebsocket(BinanceWSClient):
    def __init__(
            self,
            handler: Callable[..., Any],
            key=None,
            secret=None,
            binance_url: Literal[BinanceUrl.WS, BinanceUrl.TEST_WS] = BinanceUrl.WS,
            **kwargs
    ):
        if "base_url" not in kwargs:
            self.baseUrl = ALL_URL[BinanceInstrumentType.SPOT].get_url(binance_url)
        else:
            self.baseUrl = kwargs["base_url"]
        super().__init__(url=self.baseUrl, handler=handler, key=key, secret=secret, **kwargs)
