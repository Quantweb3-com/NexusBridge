from typing import Literal, Callable, Any

from nexusbridge.binance.base import BinanceApiClient, BinanceWSClient
from nexusbridge.binance.constants import BinanceUrl, ALL_URL, BinanceInstrumentType


class PmTradingApi(BinanceApiClient):
    def __init__(self, key=None, secret=None, **kwargs):
        super().__init__(
            key=key,
            secret=secret,
            base_url=ALL_URL[BinanceInstrumentType.Derivatives_PM].get_url(
                BinanceUrl.MAIN
            ),
            **kwargs,
        )

    # Common endpoints
    from nexusbridge.binance.pm.common import get_papi_v1_ping
    from nexusbridge.binance.pm.common import post_papi_v1_listen_key
    from nexusbridge.binance.pm.common import put_papi_v1_listen_key
    from nexusbridge.binance.pm.common import delete_papi_v1_listen_key

    # Trade endpoints
    from nexusbridge.binance.pm.trade import post_papi_v1_um_order
    from nexusbridge.binance.pm.trade import post_papi_v1_um_conditional_order
    from nexusbridge.binance.pm.trade import post_papi_v1_cm_order
    from nexusbridge.binance.pm.trade import post_papi_v1_cm_conditional_order
    from nexusbridge.binance.pm.trade import post_papi_v1_margin_order
    from nexusbridge.binance.pm.trade import post_papi_v1_margin_loan
    from nexusbridge.binance.pm.trade import post_papi_v1_repay_loan
    from nexusbridge.binance.pm.trade import post_papi_v1_margin_order_oco
    from nexusbridge.binance.pm.trade import delete_papi_v1_um_order
    from nexusbridge.binance.pm.trade import delete_papi_v1_um_all_open_orders
    from nexusbridge.binance.pm.trade import delete_papi_v1_um_conditional_order
    from nexusbridge.binance.pm.trade import (
        delete_papi_v1_um_conditional_all_open_orders,
    )
    from nexusbridge.binance.pm.trade import delete_papi_v1_cm_order
    from nexusbridge.binance.pm.trade import delete_papi_v1_cm_all_open_orders
    from nexusbridge.binance.pm.trade import delete_papi_v1_cm_conditional_order
    from nexusbridge.binance.pm.trade import (
        delete_papi_v1_cm_conditional_all_open_orders,
    )
    from nexusbridge.binance.pm.trade import delete_papi_v1_margin_order
    from nexusbridge.binance.pm.trade import delete_papi_v1_margin_orderList
    from nexusbridge.binance.pm.trade import delete_papi_v1_margin_all_open_orders
    from nexusbridge.binance.pm.trade import put_papi_v1_um_order
    from nexusbridge.binance.pm.trade import put_papi_v1_cm_order
    from nexusbridge.binance.pm.trade import get_papi_v1_um_order
    from nexusbridge.binance.pm.trade import get_papi_v1_um_all_orders
    from nexusbridge.binance.pm.trade import get_papi_v1_um_open_order
    from nexusbridge.binance.pm.trade import get_papi_v1_um_open_orders
    from nexusbridge.binance.pm.trade import get_papi_v1_um_conditional_all_orders
    from nexusbridge.binance.pm.trade import get_papi_v1_um_conditional_open_orders
    from nexusbridge.binance.pm.trade import get_papi_v1_um_conditional_open_order
    from nexusbridge.binance.pm.trade import get_papi_v1_um_conditional_order_history
    from nexusbridge.binance.pm.trade import get_papi_v1_cm_order
    from nexusbridge.binance.pm.trade import get_papi_v1_cm_all_orders
    from nexusbridge.binance.pm.trade import get_papi_v1_cm_open_order
    from nexusbridge.binance.pm.trade import get_papi_v1_cm_open_orders
    from nexusbridge.binance.pm.trade import get_papi_v1_cm_conditional_open_orders
    from nexusbridge.binance.pm.trade import get_papi_v1_cm_conditional_open_order
    from nexusbridge.binance.pm.trade import get_papi_v1_cm_conditional_all_orders
    from nexusbridge.binance.pm.trade import get_papi_v1_cm_conditional_order_history
    from nexusbridge.binance.pm.trade import get_papi_v1_um_force_orders
    from nexusbridge.binance.pm.trade import get_papi_v1_cm_force_orders
    from nexusbridge.binance.pm.trade import get_papi_v1_um_order_amendment
    from nexusbridge.binance.pm.trade import get_papi_v1_cm_order_amendment
    from nexusbridge.binance.pm.trade import get_papi_v1_margin_force_orders
    from nexusbridge.binance.pm.trade import get_papi_v1_um_user_trades
    from nexusbridge.binance.pm.trade import get_papi_v1_cm_user_trades
    from nexusbridge.binance.pm.trade import get_papi_v1_um_adl_quantile
    from nexusbridge.binance.pm.trade import get_papi_v1_cm_adl_quantile
    from nexusbridge.binance.pm.trade import post_papi_v1_um_feeBurn
    from nexusbridge.binance.pm.trade import get_papi_v1_um_feeBurn
    from nexusbridge.binance.pm.trade import get_papi_v1_margin_order
    from nexusbridge.binance.pm.trade import get_papi_v1_margin_openOrders
    from nexusbridge.binance.pm.trade import get_papi_v1_margin_all_open_orders
    from nexusbridge.binance.pm.trade import get_papi_v1_margin_orderList
    from nexusbridge.binance.pm.trade import get_papi_v1_margin_all_orderList
    from nexusbridge.binance.pm.trade import get_papi_v1_margin_openOrderList
    from nexusbridge.binance.pm.trade import get_papi_v1_margin_myTrades
    from nexusbridge.binance.pm.trade import post_papi_v1_margin_repay_debt

    # Account endpoints
    from nexusbridge.binance.pm.account import get_papi_v1_balance
    from nexusbridge.binance.pm.account import get_papi_v1_account
    from nexusbridge.binance.pm.account import get_papi_v1_margin_max_borrowable
    from nexusbridge.binance.pm.account import get_papi_v1_margin_max_withdraw
    from nexusbridge.binance.pm.account import get_papi_v1_um_position_risk
    from nexusbridge.binance.pm.account import get_papi_v1_cm_position_risk
    from nexusbridge.binance.pm.account import post_papi_v1_um_leverage
    from nexusbridge.binance.pm.account import post_papi_v1_cm_leverage
    from nexusbridge.binance.pm.account import post_papi_v1_um_position_side_dual
    from nexusbridge.binance.pm.account import post_papi_v1_cm_position_side_dual
    from nexusbridge.binance.pm.account import get_papi_v1_um_position_side_dual
    from nexusbridge.binance.pm.account import get_papi_v1_cm_position_side_dual
    from nexusbridge.binance.pm.account import get_papi_v1_um_leverage_bracket
    from nexusbridge.binance.pm.account import get_papi_v1_cm_leverage_bracket
    from nexusbridge.binance.pm.account import get_papi_v1_um_api_trading_status
    from nexusbridge.binance.pm.account import get_papi_v1_um_commission_rate
    from nexusbridge.binance.pm.account import get_papi_v1_cm_commission_rate
    from nexusbridge.binance.pm.account import get_papi_v1_margin_margin_loan
    from nexusbridge.binance.pm.account import get_papi_v1_margin_repay_loan
    from nexusbridge.binance.pm.account import get_papi_v1_repay_futures_switch
    from nexusbridge.binance.pm.account import post_papi_v1_repay_futures_switch
    from nexusbridge.binance.pm.account import (
        get_papi_v1_margin_margin_interest_history,
    )
    from nexusbridge.binance.pm.account import (
        post_papi_v1_repay_futures_negative_balance,
    )
    from nexusbridge.binance.pm.account import get_papi_v1_portfolio_interest_history
    from nexusbridge.binance.pm.account import post_papi_v1_auto_collection
    from nexusbridge.binance.pm.account import post_papi_v1_asset_collection
    from nexusbridge.binance.pm.account import post_papi_v1_bnb_transfer
    from nexusbridge.binance.pm.account import get_papi_v1_um_income
    from nexusbridge.binance.pm.account import get_papi_v1_cm_income
    from nexusbridge.binance.pm.account import get_papi_v1_um_account
    from nexusbridge.binance.pm.account import get_papi_v1_cm_account
    from nexusbridge.binance.pm.account import get_papi_v1_um_account_config
    from nexusbridge.binance.pm.account import get_papi_v1_um_symbol_config
    from nexusbridge.binance.pm.account import get_papi_v2_um_account
    from nexusbridge.binance.pm.account import get_papi_v1_um_trade_asyn
    from nexusbridge.binance.pm.account import get_papi_v1_um_trade_asyn_id
    from nexusbridge.binance.pm.account import get_papi_v1_um_order_asyn
    from nexusbridge.binance.pm.account import get_papi_v1_um_order_asyn_id
    from nexusbridge.binance.pm.account import get_papi_v1_um_income_asyn
    from nexusbridge.binance.pm.account import get_papi_v1_um_income_asyn_id
    from nexusbridge.binance.pm.account import get_papi_v1_rate_limit_order


class PmTradingWebsocket(BinanceWSClient):
    def __init__(
        self,
        handler: Callable[..., Any],
        key=None,
        secret=None,
        binance_url: Literal[BinanceUrl.WS, BinanceUrl.TEST_WS] = BinanceUrl.WS,
        **kwargs,
    ):
        if "base_url" not in kwargs:
            self.baseUrl = ALL_URL[BinanceInstrumentType.SPOT].get_url(binance_url)
        else:
            self.baseUrl = kwargs["base_url"]
        super().__init__(
            url=self.baseUrl, handler=handler, key=key, secret=secret, **kwargs
        )
