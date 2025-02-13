import hmac
import hashlib
import aiohttp
import asyncio
import orjson
from typing import Any, Dict, List
from urllib.parse import urljoin, urlencode, unquote

from nexus.base import ApiClient
from nexus.bybit.constants import BybitUrl
from nexus.bybit.error import BybitError


class BybitApiClient(ApiClient):
    def __init__(
            self,
            api_key: str = None,
            secret: str = None,
            url: BybitUrl = BybitUrl.TESTNET,
            timeout: int = 10,
    ):
        """
        ### Testnet:
        `https://api-testnet.bybit.com`

        ### Mainnet:
        (both endpoints are available):
        `https://api.bybit.com`
        `https://api.bytick.com`

        ### Important:
        Netherland users: use `https://api.bybit.nl` for mainnet
        Hong Kong users: use `https://api.byhkbit.com` for mainnet
        Turkey users: use `https://api.bybit-tr.com` for mainnet
        Kazakhstan users: use `https://api.bybit.kz` for mainnet
        """

        super().__init__(
            api_key=api_key,
            secret=secret,
            timeout=timeout,
        )
        self._recv_window = 5000

        self._base_url = url.base_url

        self._headers = {
            "Content-Type": "application/json",
            "User-Agent": "TradingBot/1.0",
        }

        if api_key:
            self._headers["X-BAPI-API-KEY"] = api_key

    def _generate_signature(self, payload: str) -> List[str]:
        timestamp = str(self._clock.timestamp_ms())

        param = str(timestamp) + self._api_key + str(self._recv_window) + payload
        hash = hmac.new(
            bytes(self._secret, "utf-8"), param.encode("utf-8"), hashlib.sha256
        )
        signature = hash.hexdigest()
        return [signature, timestamp]

    async def _fetch(
            self,
            method: str,
            endpoint: str,
            payload: Dict[str, Any] = None,
            signed: bool = False,
    ):
        self._init_session()

        url = urljoin(self._base_url, endpoint)
        payload = payload or {}

        payload_str = (
            unquote(urlencode(payload))
            if method == "GET"
            else orjson.dumps(payload).decode("utf-8")
        )

        headers = self._headers
        if signed:
            signature, timestamp = self._generate_signature(payload_str)
            headers = {
                **headers,
                "X-BAPI-TIMESTAMP": timestamp,
                "X-BAPI-SIGN": signature,
                "X-BAPI-RECV-WINDOW": str(self._recv_window),
            }

        if method == "GET":
            url += f"?{payload_str}"
            payload_str = None

        try:
            self._log.debug(f"Request: {url} {payload_str}")
            response = await self._session.request(
                method=method,
                url=url,
                headers=headers,
                data=payload_str,
            )
            raw = await response.read()
            if response.status >= 400:
                raise BybitError(
                    code=response.status,
                    message=orjson.loads(raw) if raw else None,
                )
            bybit_response = orjson.loads(raw)
            if bybit_response["retCode"] == 0:
                return raw
            else:
                raise BybitError(
                    code=bybit_response["retCode"],
                    message=bybit_response["retMsg"],
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

    # Account
    from nexus.bybit.api.account import get_v5_account_wallet_balance
    from nexus.bybit.api.account import get_v5_account_withdrawal
    from nexus.bybit.api.account import post_v5_account_upgrade_to_uta
    from nexus.bybit.api.account import get_v5_account_borrow_history
    from nexus.bybit.api.account import post_v5_account_quick_repayment
    from nexus.bybit.api.account import post_v5_account_set_collateral_switch
    from nexus.bybit.api.account import post_v5_account_set_collateral_switch_batch
    from nexus.bybit.api.account import get_v5_account_collateral_info
    from nexus.bybit.api.account import get_v5_asset_coin_greeks
    from nexus.bybit.api.account import get_v5_account_fee_rate
    from nexus.bybit.api.account import get_v5_account_info
    from nexus.bybit.api.account import get_v5_account_query_dcp_info
    from nexus.bybit.api.account import get_v5_account_transaction_log
    from nexus.bybit.api.account import get_v5_account_contract_transaction_log
    from nexus.bybit.api.account import get_v5_account_smp_group
    from nexus.bybit.api.account import post_v5_account_set_margin_mode
    from nexus.bybit.api.account import post_v5_account_set_hedging_mode
    from nexus.bybit.api.account import post_v5_account_mmp_modify
    from nexus.bybit.api.account import post_v5_account_mmp_reset
    from nexus.bybit.api.account import get_v5_account_mmp_state

    # Asset
    from nexus.bybit.api.asset import get_v5_asset_delivery_record
    from nexus.bybit.api.asset import get_v5_asset_settlement_record
    from nexus.bybit.api.asset import get_v5_asset_exchange_order_record
    from nexus.bybit.api.asset import get_v5_asset_coin_query_info
    from nexus.bybit.api.asset import get_v5_asset_transfer_query_sub_member_list
    from nexus.bybit.api.asset import get_v5_asset_transfer_query_asset_info
    from nexus.bybit.api.asset import get_v5_asset_transfer_query_account_coin_balance
    from nexus.bybit.api.asset import get_v5_asset_withdraw_withdrawable_amount
    from nexus.bybit.api.asset import get_v5_asset_transfer_query_transfer_coin_list
    from nexus.bybit.api.asset import post_v5_asset_transfer_inter_transfer
    from nexus.bybit.api.asset import get_v5_asset_transfer_query_inter_transfer_list
    from nexus.bybit.api.asset import post_v5_asset_transfer_universal_transfer
    from nexus.bybit.api.asset import get_v5_asset_transfer_query_universal_transfer_list
    from nexus.bybit.api.asset import get_v5_asset_deposit_query_allowed_list
    from nexus.bybit.api.asset import post_v5_asset_deposit_to_account
    from nexus.bybit.api.asset import get_v5_asset_deposit_query_record
    from nexus.bybit.api.asset import get_v5_asset_deposit_query_sub_member_record
    from nexus.bybit.api.asset import get_v5_asset_deposit_query_internal_record
    from nexus.bybit.api.asset import get_v5_asset_deposit_query_address
    from nexus.bybit.api.asset import get_v5_asset_deposit_query_sub_member_address
    from nexus.bybit.api.asset import get_v5_asset_withdraw_query_record
    from nexus.bybit.api.asset import get_v5_asset_withdraw_query_vasp_list
    from nexus.bybit.api.asset import post_v5_asset_withdraw_create
    from nexus.bybit.api.asset import post_v5_asset_withdraw_cancel
    from nexus.bybit.api.asset import get_v5_asset_exchange_query_coin_list
    from nexus.bybit.api.asset import post_v5_asset_exchange_quote_apply
    from nexus.bybit.api.asset import post_v5_asset_exchange_convert_execute
    from nexus.bybit.api.asset import get_v5_asset_exchange_convert_result_query
    from nexus.bybit.api.asset import get_v5_asset_exchange_query_convert_history

    # Market
    from nexus.bybit.api.market import get_v5_market_time
    from nexus.bybit.api.market import get_v5_market_kline
    from nexus.bybit.api.market import get_v5_market_mark_price_kline
    from nexus.bybit.api.market import get_v5_market_index_price_kline
    from nexus.bybit.api.market import get_v5_market_premium_index_price_kline
    from nexus.bybit.api.market import get_v5_market_instruments_info
    from nexus.bybit.api.market import get_v5_market_orderbook
    from nexus.bybit.api.market import get_v5_market_tickers
    from nexus.bybit.api.market import get_v5_market_funding_history
    from nexus.bybit.api.market import get_v5_market_recent_trade
    from nexus.bybit.api.market import get_v5_market_open_interest
    from nexus.bybit.api.market import get_v5_market_historical_volatility
    from nexus.bybit.api.market import get_v5_market_insurance
    from nexus.bybit.api.market import get_v5_market_risk_limit
    from nexus.bybit.api.market import get_v5_market_delivery_price
    from nexus.bybit.api.market import get_v5_market_account_ratio

    # Position
    from nexus.bybit.api.position import get_v5_position_list
    from nexus.bybit.api.position import post_v5_position_set_leverage
    from nexus.bybit.api.position import post_v5_position_switch_isolated
    from nexus.bybit.api.position import post_v5_position_switch_mode
    from nexus.bybit.api.position import post_v5_position_trading_stop
    from nexus.bybit.api.position import post_v5_position_set_auto_add_margin
    from nexus.bybit.api.position import post_v5_position_add_margin
    from nexus.bybit.api.position import get_v5_position_closed_pnl
    from nexus.bybit.api.position import post_v5_position_move_positions
    from nexus.bybit.api.position import post_v5_position_confirm_pending_mmr
    from nexus.bybit.api.position import post_v5_position_set_tpsl_mode
    from nexus.bybit.api.position import post_v5_position_set_risk_limit
    from nexus.bybit.api.position import get_v5_position_move_history

    # Trade
    from nexus.bybit.api.trade import post_v5_order_create
    from nexus.bybit.api.trade import post_v5_order_amend
    from nexus.bybit.api.trade import post_v5_order_cancel
    from nexus.bybit.api.trade import get_v5_order_realtime
    from nexus.bybit.api.trade import post_v5_order_cancel_all
    from nexus.bybit.api.trade import get_v5_order_history
    from nexus.bybit.api.trade import get_v5_execution_list
    from nexus.bybit.api.trade import post_v5_order_create_batch
    from nexus.bybit.api.trade import post_v5_order_amend_batch
    from nexus.bybit.api.trade import post_v5_order_cancel_batch
    from nexus.bybit.api.trade import get_v5_order_spot_borrow_check
    from nexus.bybit.api.trade import post_v5_order_disconnected_cancel_all
