from typing import Literal, Dict, Any

import orjson


async def get_v5_account_wallet_balance(
    self,
    account_type: Literal["UNIFIED", "CONTRACT", "SPOT"],
    coin: str | None = None,
):
    """
    Get Wallet Balance
    https://bybit-exchange.github.io/docs/v5/account/wallet-balance
    """
    endpoint = "/v5/account/wallet-balance"
    payload = {
        "accountType": account_type,
    }
    if coin:
        payload["coin"] = coin
    raw = await self._fetch("GET", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def get_v5_account_withdrawal(self, coin_name: str):
    """
    Get Transferable Amount (Unified)
    https://bybit-exchange.github.io/docs/v5/account/unified-trans-amnt
    """
    endpoint = "/v5/account/withdrawal"
    payload = {
        "coinName": coin_name,
    }
    raw = await self._fetch("GET", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_account_upgrade_to_uta(
    self,
):
    """
    Upgrade to Unified Account
    https://bybit-exchange.github.io/docs/v5/account/upgrade-unified-account
    """
    endpoint = "/v5/account/upgrade-to-uta"
    raw = await self._fetch("POST", endpoint, signed=True)
    return orjson.loads(raw)


async def get_v5_account_borrow_history(self, **kwargs):
    """
    Get Borrow History
    https://bybit-exchange.github.io/docs/v5/account/borrow-history
    """
    endpoint = "/v5/account/borrow-history"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_account_quick_repayment(self, coin: str | None = None):
    """
    Repay Liability
    https://bybit-exchange.github.io/docs/v5/account/repay-liability
    """
    endpoint = "/v5/account/quick-repayment"
    payload = {}
    if coin:
        payload["coin"] = coin
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_account_set_collateral_switch(
    self, coin: str, collateral_switch: Literal["off", "on"]
):
    """
    Set Collateral Coin
    https://bybit-exchange.github.io/docs/v5/account/set-collateral
    """
    endpoint = "/v5/account/set-collateral-switch"
    payload = {
        "coin": coin,
        "collateralSwitch": collateral_switch,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_account_set_collateral_switch_batch(
    self,
    request: list[Dict[str, Any]],
):
    """
    Batch Set Collateral Coin
    https://bybit-exchange.github.io/docs/v5/account/batch-set-collateral
    """
    endpoint = "/v5/account/set-collateral-switch-batch"
    payload = {
        "request": request,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def get_v5_account_collateral_info(self, currency: str | None = None):
    """
    Get Collateral Info
    https://bybit-exchange.github.io/docs/v5/account/collateral-info
    """
    endpoint = "/v5/account/collateral-info"
    payload = {}
    if currency:
        payload["currency"] = currency
    raw = await self._fetch("GET", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_coin_greeks(self, base_coin: str | None = None):
    """
    Get Coin Greeks
    https://bybit-exchange.github.io/docs/v5/account/coin-greeks
    """
    endpoint = "/v5/asset/coin-greeks"
    payload = {}
    if base_coin:
        payload["baseCoin"] = base_coin
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_account_fee_rate(
    self,
    category: Literal["linear", "inverse", "spot", "option"] | None = None,
    **kwargs,
):
    """
    Get Fee Rate
    https://bybit-exchange.github.io/docs/v5/account/fee-rate
    """
    endpoint = "/v5/account/fee-rate"
    payload = {**kwargs}
    if category:
        payload["category"] = category
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_account_info(self):
    """
    Get Account Info
    https://bybit-exchange.github.io/docs/v5/account/account-info
    """
    endpoint = "/v5/account/info"
    raw = await self._fetch("GET", endpoint, signed=True)
    return orjson.loads(raw)


async def get_v5_account_query_dcp_info(self):
    """
    Get DCP Info
    https://bybit-exchange.github.io/docs/v5/account/dcp-info
    """
    endpoint = "/v5/account/query-dcp-info"
    raw = await self._fetch("GET", endpoint, signed=True)
    return orjson.loads(raw)


async def get_v5_account_transaction_log(self, **kwargs):
    """
    Get Transaction Log
    https://bybit-exchange.github.io/docs/v5/account/transaction-log
    """
    endpoint = "/v5/account/transaction-log"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_account_contract_transaction_log(self, **kwargs):
    """
    Get Contract Transaction Log
    https://bybit-exchange.github.io/docs/v5/account/contract-transaction-log
    """
    endpoint = "/v5/account/contract-transaction-log"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_account_smp_group(self):
    """
    Get SMP Group ID
    https://bybit-exchange.github.io/docs/v5/account/smp-group
    """
    endpoint = "/v5/account/smp-group"
    raw = await self._fetch("GET", endpoint, signed=True)
    return orjson.loads(raw)


async def post_v5_account_set_margin_mode(
    self,
    set_margin_mode: Literal["ISOLATED_MARGIN", "REGULAR_MARGIN", "PORTFOLIO_MARGIN"],
):
    """
    Set Margin Mode
    https://bybit-exchange.github.io/docs/v5/account/set-margin-mode
    """
    endpoint = "/v5/account/set-margin-mode"
    payload = {
        "setMarginMode": set_margin_mode,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_account_set_hedging_mode(
    self, set_hedging_mode: Literal["ON", "OFF"]
):
    """
    Set Spot Hedging
    https://bybit-exchange.github.io/docs/v5/account/set-spot-hedge
    """
    endpoint = "/v5/account/set-hedging-mode"
    payload = {
        "setHedgingMode": set_hedging_mode,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_account_mmp_modify(
    self,
    base_coin: str,
    window: str,
    frozen_period: str,
    qty_limit: str,
    delta_limit: str,
):
    """
    Set MMP
    https://bybit-exchange.github.io/docs/v5/account/set-mmp
    """
    endpoint = "/v5/account/mmp-modify"
    payload = {
        "baseCoin": base_coin,
        "window": window,
        "frozenPeriod": frozen_period,
        "qtyLimit": qty_limit,
        "deltaLimit": delta_limit,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_account_mmp_reset(self, base_coin: str):
    """
    Reset MMP
    https://bybit-exchange.github.io/docs/v5/account/reset-mmp
    """
    endpoint = "/v5/account/mmp-reset"
    payload = {
        "baseCoin": base_coin,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_account_mmp_state(self, base_coin: str):
    """
    Get MMP State
    https://bybit-exchange.github.io/docs/v5/account/get-mmp-state
    """
    endpoint = "/v5/account/mmp-state"
    payload = {
        "baseCoin": base_coin,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)
