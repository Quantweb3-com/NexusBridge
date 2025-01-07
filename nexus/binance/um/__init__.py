from typing import Literal

from nexus.binance.base import BinanceApiClient
from nexus.binance.constants import BinanceUrl, ALL_URL, BinanceInstrumentType


class UmTradingApi(BinanceApiClient):
    def __init__(
            self,
            key=None,
            secret=None,
            binance_url: Literal[BinanceUrl.MAIN, BinanceUrl.TEST] = BinanceUrl.MAIN,
            **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = ALL_URL[BinanceInstrumentType.Derivatives_UM].get_url(binance_url)
        super().__init__(key=key, secret=secret, **kwargs)

    # Market Data endpoints
    from nexus.binance.um.market_data import get_fapi_v1_ping
    from nexus.binance.um.market_data import get_fapi_v1_time
    from nexus.binance.um.market_data import get_fapi_v1_exchange_info
    from nexus.binance.um.market_data import get_fapi_v1_depth
    from nexus.binance.um.market_data import get_fapi_v1_trades
    from nexus.binance.um.market_data import get_fapi_v1_historical_trades
    from nexus.binance.um.market_data import get_fapi_v1_agg_trades
    from nexus.binance.um.market_data import get_fapi_v1_klines
    from nexus.binance.um.market_data import get_fapi_v1_continuous_klines
    from nexus.binance.um.market_data import get_fapi_v1_index_price_klines
    from nexus.binance.um.market_data import get_fapi_v1_mark_price_klines
    from nexus.binance.um.market_data import get_fapi_v1_premium_index_klines
    from nexus.binance.um.market_data import get_fapi_v1_premium_index
    from nexus.binance.um.market_data import get_fapi_v1_funding_rate
    from nexus.binance.um.market_data import get_fapi_v1_funding_info
    from nexus.binance.um.market_data import get_fapi_v1_ticker_24hr
    from nexus.binance.um.market_data import get_fapi_v1_ticker_price
    from nexus.binance.um.market_data import get_fapi_v2_ticker_price
    from nexus.binance.um.market_data import get_fapi_v1_book_ticker
    from nexus.binance.um.market_data import get_fapi_v1_delivery_price
    from nexus.binance.um.market_data import get_fapi_v1_open_interest
    from nexus.binance.um.market_data import get_fapi_v1_open_interest_hist
    from nexus.binance.um.market_data import get_futures_data_top_long_short_position_ratio
    from nexus.binance.um.market_data import get_futures_data_top_long_short_account_ratio
    from nexus.binance.um.market_data import get_futures_data_global_long_short_account_ratio
    from nexus.binance.um.market_data import get_futures_data_taker_long_short_ratio
    from nexus.binance.um.market_data import get_fapi_v1_lvt_klines
    from nexus.binance.um.market_data import get_fapi_v1_index_info
    from nexus.binance.um.market_data import get_fapi_v1_asset_index
    from nexus.binance.um.market_data import get_fapi_v1_constituents

    # Trading endpoints
    from nexus.binance.um.trade import post_fapi_v1_order
    from nexus.binance.um.trade import post_fapi_v1_batch_order
    from nexus.binance.um.trade import put_fapi_v1_order
    from nexus.binance.um.trade import put_fapi_v1_batch_order
    from nexus.binance.um.trade import get_fapi_v1_order_amendment
    from nexus.binance.um.trade import delete_fapi_v1_order
    from nexus.binance.um.trade import delete_fapi_v1_batch_order
    from nexus.binance.um.trade import delete_fapi_v1_all_open_orders
    from nexus.binance.um.trade import post_fapi_v1_countdown_cancel_all
    from nexus.binance.um.trade import get_fapi_v1_order
    from nexus.binance.um.trade import get_fapi_v1_all_orders
    from nexus.binance.um.trade import get_fapi_v1_open_orders
    from nexus.binance.um.trade import get_fapi_v1_open_order
    from nexus.binance.um.trade import get_fapi_v1_force_orders
    from nexus.binance.um.trade import get_fapi_v1_user_trades
    from nexus.binance.um.trade import post_fapi_v1_margin_type
    from nexus.binance.um.trade import post_fapi_v1_position_side_dual
    from nexus.binance.um.trade import post_fapi_v1_leverage
    from nexus.binance.um.trade import post_fapi_v1_multi_assets_margin
    from nexus.binance.um.trade import post_fapi_v1_position_margin
    from nexus.binance.um.trade import get_fapi_v2_position_risk
    from nexus.binance.um.trade import get_fapi_v3_position_risk
    from nexus.binance.um.trade import get_fapi_v1_adl_quantile
    from nexus.binance.um.trade import get_fapi_v1_position_margin_history
    from nexus.binance.um.trade import post_fapi_v1_order_test

