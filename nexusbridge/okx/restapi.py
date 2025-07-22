from typing import Dict, Any
import orjson
import hmac
import base64
import asyncio
import aiohttp
from urllib.parse import urljoin, urlencode, unquote

from nexusbridge.base import ApiClient
from nexusbridge.okx.constants import OkxUrl
from nexusbridge.okx.error import OkxHttpError, OkxRequestError


class OkxApiClient(ApiClient):
    def __init__(
        self,
        api_key: str = None,
        secret: str = None,
        passphrase: str = None,
        url: OkxUrl = OkxUrl.DEMO,
        timeout: int = 10,
        max_rate: int | None = None,
    ):
        super().__init__(
            api_key=api_key,
            secret=secret,
            timeout=timeout,
            max_rate=max_rate,
        )

        self._base_url = url.base_url
        self._passphrase = passphrase
        self._testnet = url.is_testnet
        self._headers = {
            "Content-Type": "application/json",
            "User-Agent": "TradingBot/1.0",
        }

    def _generate_signature(self, message: str) -> str:
        mac = hmac.new(
            bytes(self._secret, encoding="utf8"),
            bytes(message, encoding="utf-8"),
            digestmod="sha256",
        )
        return base64.b64encode(mac.digest()).decode()

    async def _get_signature(
        self, ts: str, method: str, request_path: str, payload: Dict[str, Any] = None
    ) -> str:
        body = ""
        if method == "POST":
            body = {}
        if payload:
            body = orjson.dumps(payload).decode()

        sign_str = f"{ts}{method}{request_path}{body}"
        signature = self._generate_signature(sign_str)
        return signature

    def _get_timestamp(self) -> str:
        return (
            self._clock.utc_now()
            .isoformat(timespec="milliseconds")
            .replace("+00:00", "Z")
        )

    async def _get_headers(
        self, ts: str, method: str, request_path: str, payload: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        headers = self._headers
        signature = await self._get_signature(ts, method, request_path, payload)
        headers.update(
            {
                "OK-ACCESS-KEY": self._api_key,
                "OK-ACCESS-SIGN": signature,
                "OK-ACCESS-TIMESTAMP": ts,
                "OK-ACCESS-PASSPHRASE": self._passphrase,
            }
        )
        if self._testnet:
            headers["x-simulated-trading"] = "1"
        return headers

    async def _fetch(
        self,
        method: str,
        endpoint: str,
        payload: list[Dict[str, Any]] | Dict[str, Any] = None,
        signed: bool = False,
    ) -> bytes:
        if self._limiter:
            await self._limiter.wait()

        self._init_session()
        url = urljoin(self._base_url, endpoint)
        request_path = endpoint
        headers = self._headers
        timestamp = self._get_timestamp()

        payload = payload or {}

        payload_json = (
            unquote(urlencode(payload)) if method == "GET" else orjson.dumps(payload)
        )

        if method == "GET":
            url += f"?{payload_json}"
            request_path = (
                f"{request_path}?{payload_json}" if payload_json != "" else request_path
            )
            payload_json = None
            # when method is GET, payload should be empty
            payload = {}

        if signed and self._api_key:
            headers = await self._get_headers(timestamp, method, request_path, payload)

        try:
            self._log.debug(
                f"Request {method} Url: {url} Headers: {headers} Payload: {payload_json}"
            )

            response = await self._session.request(
                method=method,
                url=url,
                headers=headers,
                data=payload_json,
            )
            raw = await response.read()
            if response.status >= 400:
                raise OkxHttpError(
                    status_code=response.status,
                    message=orjson.loads(raw),
                    headers=response.headers,
                )
            okx_response = orjson.loads(raw)
            if okx_response["code"] == "0":
                return raw
            else:
                if len(okx_response["data"]) == 0:
                    raise OkxRequestError(
                        error_code=okx_response["code"],
                        status_code=okx_response["code"],
                        message=okx_response["msg"],
                    )
                else:
                    for data in okx_response["data"]:
                        raise OkxRequestError(
                            error_code=data["sCode"],
                            status_code=response.status,
                            message=data["sMsg"],
                        )
        except aiohttp.ClientError as e:
            self._log.error(f"Client Error {method} Url: {url} {e}")
            raise
        except asyncio.TimeoutError:
            self._log.error(f"Timeout {method} Url: {url}")
            raise
        except Exception as e:
            self._log.error(f"Error {method} Url: {url} {e}")
            raise

    # AlgoTradingApi
    from nexusbridge.okx.api.algo_trading import post_api_v5_trade_order_algo
    from nexusbridge.okx.api.algo_trading import post_api_v5_trade_cancel_algos
    from nexusbridge.okx.api.algo_trading import post_api_v5_trade_amend_algos
    from nexusbridge.okx.api.algo_trading import post_api_v5_trade_cancel_advance_algos
    from nexusbridge.okx.api.algo_trading import get_api_v5_trade_order_algo
    from nexusbridge.okx.api.algo_trading import get_api_v5_trade_orders_algo_pending
    from nexusbridge.okx.api.algo_trading import get_api_v5_trade_orders_algo_history
    from nexusbridge.okx.api.algo_trading import post_api_v5_trading_bot_grid_order_algo

    # CopyTradingApi
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_current_subpositions,
    )
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_subpositions_history,
    )
    from nexusbridge.okx.api.copy_trading import post_api_v5_copytrading_algo_order
    from nexusbridge.okx.api.copy_trading import (
        post_api_v5_copytrading_close_subposition,
    )
    from nexusbridge.okx.api.copy_trading import get_api_v5_copytrading_instruments
    from nexusbridge.okx.api.copy_trading import post_api_v5_copytrading_set_instruments
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_profit_sharing_details,
    )
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_total_profit_sharing,
    )
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_unrealized_profit_sharing_details,
    )
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_total_unrealized_profit_sharing,
    )
    from nexusbridge.okx.api.copy_trading import (
        post_api_v5_copytrading_apply_lead_trading,
    )
    from nexusbridge.okx.api.copy_trading import (
        post_api_v5_copytrading_stop_lead_trading,
    )
    from nexusbridge.okx.api.copy_trading import (
        post_api_v5_copytrading_amend_profit_sharing_ratio,
    )
    from nexusbridge.okx.api.copy_trading import get_api_v5_copytrading_config
    from nexusbridge.okx.api.copy_trading import (
        post_api_v5_copytrading_first_copy_settings,
    )
    from nexusbridge.okx.api.copy_trading import (
        post_api_v5_copytrading_amend_copy_settings,
    )
    from nexusbridge.okx.api.copy_trading import (
        post_api_v5_copytrading_stop_copy_trading,
    )
    from nexusbridge.okx.api.copy_trading import get_api_v5_copytrading_copy_settings
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_current_lead_traders,
    )
    from nexusbridge.okx.api.copy_trading import get_api_v5_copytrading_public_config
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_public_lead_traders,
    )
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_public_weekly_pnl,
    )
    from nexusbridge.okx.api.copy_trading import get_api_v5_copytrading_public_pnl
    from nexusbridge.okx.api.copy_trading import get_api_v5_copytrading_public_stats
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_public_preference_currency,
    )
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_public_current_subpositions,
    )
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_public_subpositions_history,
    )
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_public_copy_traders,
    )
    from nexusbridge.okx.api.copy_trading import get_api_v5_copytrading_lead_traders
    from nexusbridge.okx.api.copy_trading import get_api_v5_copytrading_weekly_pnl
    from nexusbridge.okx.api.copy_trading import get_api_v5_copytrading_pnl
    from nexusbridge.okx.api.copy_trading import get_api_v5_copytrading_stats
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_preference_currency,
    )
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_performance_current_subpositions,
    )
    from nexusbridge.okx.api.copy_trading import (
        get_api_v5_copytrading_performance_subpositions_history,
    )
    from nexusbridge.okx.api.copy_trading import get_api_v5_copytrading_copy_traders

    # GridTradingApi
    from nexusbridge.okx.api.grid_trading import post_api_v5_trading_bot_grid_order_algo
    from nexusbridge.okx.api.grid_trading import (
        post_api_v5_trading_bot_grid_amend_order_algo,
    )
    from nexusbridge.okx.api.grid_trading import (
        post_api_v5_trading_bot_grid_stop_order_algo,
    )
    from nexusbridge.okx.api.grid_trading import (
        post_api_v5_trading_bot_grid_close_position,
    )
    from nexusbridge.okx.api.grid_trading import (
        post_api_v5_trading_bot_grid_cancel_close_order,
    )
    from nexusbridge.okx.api.grid_trading import (
        post_api_v5_trading_bot_grid_order_instant_trigger,
    )
    from nexusbridge.okx.api.grid_trading import (
        get_api_v5_trading_bot_grid_orders_algo_pending,
    )
    from nexusbridge.okx.api.grid_trading import (
        get_api_v5_trading_bot_grid_orders_algo_history,
    )
    from nexusbridge.okx.api.grid_trading import (
        get_api_v5_trading_bot_grid_orders_algo_details,
    )
    from nexusbridge.okx.api.grid_trading import get_api_v5_trading_bot_grid_sub_orders
    from nexusbridge.okx.api.grid_trading import get_api_v5_trading_bot_grid_positions
    from nexusbridge.okx.api.grid_trading import (
        post_api_v5_trading_bot_grid_withdraw_income,
    )
    from nexusbridge.okx.api.grid_trading import (
        post_api_v5_trading_bot_grid_compute_margin_balance,
    )
    from nexusbridge.okx.api.grid_trading import (
        post_api_v5_trading_bot_grid_margin_balance,
    )
    from nexusbridge.okx.api.grid_trading import (
        post_api_v5_trading_bot_grid_adjust_investment,
    )
    from nexusbridge.okx.api.grid_trading import get_api_v5_trading_bot_grid_ai_param
    from nexusbridge.okx.api.grid_trading import (
        post_api_v5_trading_bot_grid_min_investment,
    )
    from nexusbridge.okx.api.grid_trading import get_api_v5_trading_bot_rsi_back_testing
    from nexusbridge.okx.api.grid_trading import get_api_v5_trading_bot_grid_quantity

    # MarketDataApi
    from nexusbridge.okx.api.market_data import get_api_v5_market_tickers
    from nexusbridge.okx.api.market_data import get_api_v5_market_ticker
    from nexusbridge.okx.api.market_data import get_api_v5_market_books
    from nexusbridge.okx.api.market_data import get_api_v5_market_books_full
    from nexusbridge.okx.api.market_data import get_api_v5_market_candles
    from nexusbridge.okx.api.market_data import get_api_v5_market_history_candles
    from nexusbridge.okx.api.market_data import get_api_v5_market_trades
    from nexusbridge.okx.api.market_data import get_api_v5_market_history_trades
    from nexusbridge.okx.api.market_data import (
        get_api_v5_market_option_instrument_family_trades,
    )
    from nexusbridge.okx.api.market_data import get_api_v5_public_option_trades
    from nexusbridge.okx.api.market_data import get_api_v5_market_platform_24_volume
    from nexusbridge.okx.api.market_data import get_api_v5_market_call_auction_details

    # PublicDataApi
    from nexusbridge.okx.api.public_data import get_api_v5_public_instruments
    from nexusbridge.okx.api.public_data import (
        get_api_v5_public_delivery_exercise_history,
    )
    from nexusbridge.okx.api.public_data import get_api_v5_public_open_interest
    from nexusbridge.okx.api.public_data import get_api_v5_public_funding_rate
    from nexusbridge.okx.api.public_data import get_api_v5_public_funding_rate_history
    from nexusbridge.okx.api.public_data import get_api_v5_public_price_limit
    from nexusbridge.okx.api.public_data import get_api_v5_public_opt_summary
    from nexusbridge.okx.api.public_data import get_api_v5_public_estimated_price
    from nexusbridge.okx.api.public_data import (
        get_api_v5_public_discount_rate_interest_free_quota,
    )
    from nexusbridge.okx.api.public_data import get_api_v5_public_time
    from nexusbridge.okx.api.public_data import get_api_v5_public_mark_price
    from nexusbridge.okx.api.public_data import get_api_v5_public_position_tiers
    from nexusbridge.okx.api.public_data import (
        get_api_v5_public_interest_rate_loan_quota,
    )
    from nexusbridge.okx.api.public_data import get_api_v5_public_underlying
    from nexusbridge.okx.api.public_data import get_api_v5_public_insurance_fund
    from nexusbridge.okx.api.public_data import get_api_v5_public_convert_contract_coin
    from nexusbridge.okx.api.public_data import get_api_v5_public_instrument_tick_bands
    from nexusbridge.okx.api.public_data import get_api_v5_public_premium_history
    from nexusbridge.okx.api.public_data import get_api_v5_market_index_tickers
    from nexusbridge.okx.api.public_data import get_api_v5_market_index_candles
    from nexusbridge.okx.api.public_data import get_api_v5_market_history_index_candles
    from nexusbridge.okx.api.public_data import get_api_v5_market_mark_price_candles
    from nexusbridge.okx.api.public_data import (
        get_api_v5_market_history_mark_price_candles,
    )
    from nexusbridge.okx.api.public_data import get_api_v5_market_open_oracle
    from nexusbridge.okx.api.public_data import get_api_v5_market_exchange_rate
    from nexusbridge.okx.api.public_data import get_api_v5_market_index_components
    from nexusbridge.okx.api.public_data import get_api_v5_public_economic_calendar

    # RecurringBuyApi
    from nexusbridge.okx.api.recurring_buy import (
        post_api_v5_trading_bot_signal_create_signal,
    )
    from nexusbridge.okx.api.recurring_buy import (
        post_api_v5_trading_bot_recurring_order_algo,
    )
    from nexusbridge.okx.api.recurring_buy import (
        post_api_v5_trading_bot_recurring_amend_order_algo,
    )
    from nexusbridge.okx.api.recurring_buy import (
        post_api_v5_trading_bot_recurring_stop_order_algo,
    )
    from nexusbridge.okx.api.recurring_buy import (
        get_api_v5_trading_bot_recurring_orders_algo_pending,
    )
    from nexusbridge.okx.api.recurring_buy import (
        get_api_v5_trading_bot_recurring_orders_algo_history,
    )
    from nexusbridge.okx.api.recurring_buy import (
        get_api_v5_trading_bot_recurring_orders_algo_details,
    )
    from nexusbridge.okx.api.recurring_buy import (
        get_api_v5_trading_bot_recurring_sub_orders,
    )

    # SignalBotTradingApi
    from nexusbridge.okx.api.signal_bot_trading import (
        post_api_v5_trading_bot_signal_create_signal,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        get_api_v5_trading_bot_signal_signals,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        post_api_v5_trading_bot_signal_order_algo,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        post_api_v5_trading_bot_signal_stop_order_algo,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        post_api_v5_trading_bot_signal_margin_balance,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        post_api_v5_trading_bot_signal_amend_tp_sl,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        post_api_v5_trading_bot_signal_set_instruments,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        get_api_v5_trading_bot_signal_orders_algo_details,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        get_api_v5_trading_bot_signal_orders_algo_pending,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        get_api_v5_trading_bot_signal_orders_algo_history,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        get_api_v5_trading_bot_signal_positions,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        get_api_v5_trading_bot_signal_positions_history,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        post_api_v5_trading_bot_signal_close_position,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        post_api_v5_trading_bot_signal_sub_order,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        post_api_v5_trading_bot_signal_cancel_sub_order,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        get_api_v5_trading_bot_signal_sub_orders,
    )
    from nexusbridge.okx.api.signal_bot_trading import (
        get_api_v5_trading_bot_signal_event_history,
    )

    # TradeApi
    from nexusbridge.okx.api.trade import post_api_v5_trade_order
    from nexusbridge.okx.api.trade import post_api_v5_trade_cancel_order
    from nexusbridge.okx.api.trade import post_api_v5_trade_batch_orders
    from nexusbridge.okx.api.trade import post_api_v5_trade_cancel_batch_orders
    from nexusbridge.okx.api.trade import post_api_v5_trade_amend_order
    from nexusbridge.okx.api.trade import post_api_v5_trade_amend_batch_orders
    from nexusbridge.okx.api.trade import post_api_v5_trade_close_position
    from nexusbridge.okx.api.trade import get_api_v5_trade_order
    from nexusbridge.okx.api.trade import get_api_v5_trade_orders_pending
    from nexusbridge.okx.api.trade import get_api_v5_trade_orders_history
    from nexusbridge.okx.api.trade import get_api_v5_trade_orders_history_archive
    from nexusbridge.okx.api.trade import get_api_v5_trade_fills
    from nexusbridge.okx.api.trade import get_api_v5_trade_fills_history
    from nexusbridge.okx.api.trade import get_api_v5_trade_easy_convert_currency_list
    from nexusbridge.okx.api.trade import post_api_v5_trade_easy_convert
    from nexusbridge.okx.api.trade import get_api_v5_trade_easy_convert_history
    from nexusbridge.okx.api.trade import get_api_v5_trade_one_click_repay_currency_list
    from nexusbridge.okx.api.trade import post_api_v5_trade_one_click_repay
    from nexusbridge.okx.api.trade import get_api_v5_trade_one_click_repay_history
    from nexusbridge.okx.api.trade import post_api_v5_trade_mass_cancel
    from nexusbridge.okx.api.trade import post_api_v5_trade_cancel_all_after
    from nexusbridge.okx.api.trade import get_api_v5_trade_account_rate_limit
    from nexusbridge.okx.api.trade import post_api_v5_trade_order_precheck

    # TradingAccountApi
    from nexusbridge.okx.api.trading_account import get_api_v5_account_instruments
    from nexusbridge.okx.api.trading_account import get_api_v5_account_balance
    from nexusbridge.okx.api.trading_account import get_api_v5_account_positions
    from nexusbridge.okx.api.trading_account import get_api_v5_account_positions_history
    from nexusbridge.okx.api.trading_account import get_api_v5_account_position_risk
    from nexusbridge.okx.api.trading_account import get_api_v5_account_bills
    from nexusbridge.okx.api.trading_account import get_api_v5_account_bills_archive
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_bills_history_archive,
    )
    from nexusbridge.okx.api.trading_account import (
        get_api_v5_account_bills_history_archive,
    )
    from nexusbridge.okx.api.trading_account import get_api_v5_account_config
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_set_position_mode,
    )
    from nexusbridge.okx.api.trading_account import post_api_v5_account_set_leverage
    from nexusbridge.okx.api.trading_account import get_api_v5_account_max_size
    from nexusbridge.okx.api.trading_account import get_api_v5_account_max_avail_size
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_position_margin_balance,
    )
    from nexusbridge.okx.api.trading_account import get_api_v5_account_leverage_info
    from nexusbridge.okx.api.trading_account import (
        get_api_v5_account_adjust_leverage_info,
    )
    from nexusbridge.okx.api.trading_account import get_api_v5_account_max_loan
    from nexusbridge.okx.api.trading_account import get_api_v5_account_trade_fee
    from nexusbridge.okx.api.trading_account import get_api_v5_account_interest_accrued
    from nexusbridge.okx.api.trading_account import get_api_v5_account_interest_rate
    from nexusbridge.okx.api.trading_account import post_api_v5_account_set_greeks
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_set_isolated_mode,
    )
    from nexusbridge.okx.api.trading_account import get_api_v5_account_max_withdrawal
    from nexusbridge.okx.api.trading_account import get_api_v5_account_risk_state
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_quick_margin_borrow_repay,
    )
    from nexusbridge.okx.api.trading_account import (
        get_api_v5_account_quick_margin_borrow_repay_history,
    )
    from nexusbridge.okx.api.trading_account import get_api_v5_account_interest_limits
    from nexusbridge.okx.api.trading_account import (
        get_api_v5_account_fixed_loan_borrowing_limit,
    )
    from nexusbridge.okx.api.trading_account import (
        get_api_v5_account_fixed_loan_borrowing_quote,
    )
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_fixed_loan_borrowing_order,
    )
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_fixed_loan_amend_borrowing_order,
    )
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_fixed_loan_manual_reborrow,
    )
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_fixed_loan_repay_borrowing_order,
    )
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_fixed_loan_convert_to_market_loan,
    )
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_fixed_loan_reduce_liabilities,
    )
    from nexusbridge.okx.api.trading_account import (
        get_api_v5_account_fixed_loan_borrowing_orders_list,
    )
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_spot_manual_borrow_repay,
    )
    from nexusbridge.okx.api.trading_account import post_api_v5_account_set_auto_repay
    from nexusbridge.okx.api.trading_account import (
        get_api_v5_account_spot_borrow_repay_history,
    )
    from nexusbridge.okx.api.trading_account import post_api_v5_account_position_builder
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_set_risk_offset_amt,
    )
    from nexusbridge.okx.api.trading_account import get_api_v5_account_greeks
    from nexusbridge.okx.api.trading_account import get_api_v5_account_position_tiers
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_set_risk_offset_type,
    )
    from nexusbridge.okx.api.trading_account import post_api_v5_account_activate_option
    from nexusbridge.okx.api.trading_account import post_api_v5_account_set_auto_loan
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_account_level_switch_preset,
    )
    from nexusbridge.okx.api.trading_account import (
        get_api_v5_account_set_account_switch_precheck,
    )
    from nexusbridge.okx.api.trading_account import (
        post_api_v5_account_set_account_level,
    )
    from nexusbridge.okx.api.trading_account import post_api_v5_account_mmp_reset
    from nexusbridge.okx.api.trading_account import post_api_v5_account_mmp_config
    from nexusbridge.okx.api.trading_account import get_api_v5_account_mmp_config

    # FinancialProductApi
    from nexusbridge.okx.api.financial_product import (
        get_api_v5_finance_savings_lending_rate_history,
    )
    from nexusbridge.okx.api.financial_product import (
        get_api_v5_finance_savings_lending_rate_summary,
    )
