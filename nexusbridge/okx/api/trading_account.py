from typing import Literal

import orjson


async def get_api_v5_account_instruments(self, inst_type: str, **kwargs):
    """
    Retrieve available instruments info of current account.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-instruments
    """
    endpoint = "/api/v5/account/instruments"
    payload = {"instType": inst_type, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_balance(self, ccy: str | None = None):
    """
    Retrieve a list of assets (with non-zero balance), remaining balance, and available amount in the trading account.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-balance
    """
    endpoint = "/api/v5/account/balance"
    payload = {}
    if ccy:
        payload["ccy"] = ccy
    raw = await self._fetch("GET", endpoint, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_positions(self, **kwargs):
    """
    Retrieve information on your positions. When the account is in net mode, net positions will be displayed, and when the account is in long/short mode, long or short positions will be displayed. Return in reverse chronological order using ctime.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-positions
    """
    endpoint = "/api/v5/account/positions"
    payload = {**kwargs}

    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_positions_history(self, **kwargs):
    """
    Retrieve the updated position data for the last 3 months. Return in reverse chronological order using utime. Getting positions history is supported under Portfolio margin mode since 04:00 AM (UTC) on November 11, 2024
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-positions-history
    """
    endpoint = "/api/v5/account/positions-history"
    payload = {**kwargs}

    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_position_risk(
    self, inst_type: Literal["MARGIN", "SWAP", "FUTURES", "OPTION"] | None = None
):
    """
    Retrieve the risk limit of the account.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-account-and-position-risk
    """
    endpoint = "/api/v5/account/account-position-risk"
    payload = {}
    if inst_type:
        payload["instType"] = inst_type

    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_bills(self, **kwargs):
    """
    Retrieve the bills of the account. The bill refers to all transaction records that result in changing the balance of an account. Pagination is supported, and the response is sorted with the most recent first. This endpoint can retrieve data from the last 7 days.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-bills-details-last-7-days
    """
    endpoint = "/api/v5/account/bills"
    payload = {**kwargs}

    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_bills_archive(self, **kwargs):
    """
    Retrieve the account’s bills. The bill refers to all transaction records that result in changing the balance of an account. Pagination is supported, and the response is sorted with most recent first. This endpoint can retrieve data from the last 3 months.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-bills-details-last-3-months
    """
    endpoint = "/api/v5/account/bills-archive"
    payload = {**kwargs}

    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_bills_history_archive(
    self,
    year: str,
    quarter: Literal["Q1", "Q2", "Q3", "Q4"],
):
    """
    Apply for bill data since 1 February, 2021 except for the current quarter.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-apply-bills-details-since-2021
    """
    endpoint = "/api/v5/account/bills-history-archive"
    payload = {"year": year, "quarter": quarter}

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_bills_history_archive(
    self,
    year: str,
    quarter: Literal["Q1", "Q2", "Q3", "Q4"],
):
    """
    Apply for bill data since 1 February, 2021 except for the current quarter.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-bills-details-since-2021
    """
    endpoint = "/api/v5/account/bills-history-archive"
    payload = {"year": year, "quarter": quarter}

    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_config(self):
    """
    Retrieve current account configuration.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-account-configuration
    """
    endpoint = "/api/v5/account/config"
    raw = await self._fetch("GET", endpoint, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_set_position_mode(
    self, pos_mode: Literal["long_short_mode", "net_mode"]
):
    """
    Spot and futures mode and Multi-currency mode: FUTURES and SWAP support both long/short mode and net mode. In net mode, users can only have positions in one direction; In long/short mode, users can hold positions in long and short directions.
    Portfolio margin mode: FUTURES and SWAP only support net mode
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-set-position-mode
    """
    endpoint = "/api/v5/account/set-position-mode"
    payload = {"posMode": pos_mode}

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_set_leverage(
    self, mgn_mode: Literal["isolated", "cross"], lever: str, ccy: str, **kwargs
):
    """
    There are 10 different scenarios for leverage setting:
    1. Set leverage for MARGIN instruments under isolated-margin trade mode at pairs level.
    2. Set leverage for MARGIN instruments under cross-margin trade mode and Spot mode (enabled borrow) at currency level.
    3. Set leverage for MARGIN instruments under cross-margin trade mode and Spot and futures mode account mode at pairs level.
    4. Set leverage for MARGIN instruments under cross-margin trade mode and Multi-currency margin at currency level.
    5. Set leverage for MARGIN instruments under cross-margin trade mode and Portfolio margin at currency level.
    6. Set leverage for FUTURES instruments under cross-margin trade mode at underlying level.
    7. Set leverage for FUTURES instruments under isolated-margin trade mode and buy/sell position mode at contract level.
    8. Set leverage for FUTURES instruments under isolated-margin trade mode and long/short position mode at contract and position side level.
    9. Set leverage for SWAP instruments under cross-margin trade at contract level.
    10. Set leverage for SWAP instruments under isolated-margin trade mode and buy/sell position mode at contract level.
    11. Set leverage for SWAP instruments under isolated-margin trade mode and long/short position mode at contract and position side level.
    Note that the request parameter posSide is only required when margin mode is isolated in long/short position mode for FUTURES/SWAP instruments (see scenario 8 and 11 above).
    Please refer to the request examples on the right for each case.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-set-leverage
    """
    endpoint = "/api/v5/account/set-leverage"
    payload = {"lever": lever, "mgnMode": mgn_mode, "ccy": ccy, **kwargs}

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_max_size(
    self,
    inst_id: str,
    td_mode: Literal["cross", "isolated", "cash", "spot_isolated"],
    **kwargs,
):
    """
    The maximum quantity to buy or sell. It corresponds to the "sz" from placement.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-maximum-order-quantity
    """
    endpoint = "/api/v5/account/max-size"
    payload = {"instId": inst_id, "tdMode": td_mode, **kwargs}

    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_max_avail_size(
    self,
    inst_id: str,
    td_mode: Literal["cross", "isolated", "cash", "spot_isolated"],
    **kwargs,
):
    """
    Available balance for isolated margin positions and SPOT, available equity for cross margin positions.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-maximum-available-balance-equity
    """
    endpoint = "/api/v5/account/max-avail-size"
    payload = {"instId": inst_id, "tdMode": td_mode, **kwargs}

    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_position_margin_balance(
    self,
    inst_id: str,
    pos_side: Literal["long", "short"],
    _type: Literal["add", "reduce"],
    amt: str,
    ccy: str | None = None,
):
    """
    Increase or decrease the margin of the isolated position. Margin reduction may result in the change of the actual leverage.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-increase-decrease-margin
    """
    endpoint = "/api/v5/account/position/margin-balance"
    payload = {
        "instId": inst_id,
        "posSide": pos_side,
        "type": _type,
        "amt": amt,
    }
    if ccy:
        payload["ccy"] = ccy

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_leverage_info(
    self, mgn_mode: Literal["isolated", "cross"], **kwargs
):
    """
    Get leverage
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-leverage
    """
    endpoint = "/api/v5/account/leverage-info"
    payload = {"mgnMode": mgn_mode, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_adjust_leverage_info(
    self,
    inst_type: Literal["MARGIN", "SWAP", "FUTURES"],
    mgn_mode: Literal["isolated", "cross"],
    lever: str,
    **kwargs,
):
    """
    Get leverage estimated info
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-leverage-estimated-info
    """
    endpoint = "/api/v5/account/adjust-leverage-info"
    payload = {"instType": inst_type, "mgnMode": mgn_mode, "lever": lever, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_max_loan(
    self, mgn_mode: Literal["isolated", "cross"], **kwargs
):
    """
    Get the maximum loan of instrument
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-the-maximum-loan-of-instrument
    """
    endpoint = "/api/v5/account/max-loan"
    payload = {"mgnMode": mgn_mode, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_trade_fee(
    self,
    inst_type: Literal["SPOT", "MARGIN", "SWAP", "FUTURES", "OPTION"],
    rule_type: Literal["normal", "pre_market"] | None = None,
    **kwargs,
):
    """
    Get fee rates
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-fee-rates
    """
    endpoint = "/api/v5/account/trade-fee"
    payload = {"instType": inst_type, **kwargs}
    if rule_type:
        payload["ruleType"] = rule_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_interest_accrued(self, **kwargs):
    """
    Get interest accrued data. Only data within the last one year can be obtained.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-interest-accrued-data
    """
    endpoint = "/api/v5/account/interest-accrued"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_interest_rate(self, ccy: str | None = None):
    """
    Get the user's current leveraged currency borrowing market interest rate
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-interest-rate
    """
    endpoint = "/api/v5/account/interest-rate"
    payload = {}
    if ccy:
        payload["ccy"] = ccy
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_set_greeks(
    self,
    greeks_type: Literal["PA", "BS"],
):
    """
    Set the display type of Greeks.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-set-greeks-pa-bs
    """
    endpoint = "/api/v5/account/set-greeks"
    payload = {"greeksType": greeks_type}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_set_isolated_mode(
    self, _type: Literal["MARGIN", "CONTRACTS"], iso_mode: str = "automatic"
):
    """
    Set isolated margin mode
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-set-isolated-margin-mode
    """
    endpoint = "/api/v5/account/set-isolated-mode"
    payload = {"type": _type, "isoMode": iso_mode}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_max_withdrawal(self, ccy: str | None = None):
    """
    Retrieve the maximum transferable amount from trading account to funding account. If no currency is specified, the transferable amount of all owned currencies will be returned.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-maximum-withdrawals
    """
    endpoint = "/api/v5/account/max-withdrawal"
    payload = {}
    if ccy:
        payload["ccy"] = ccy
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_risk_state(self):
    """
    Only applicable to Portfolio margin account
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-account-risk-state
    """
    endpoint = "/api/v5/account/risk-state"
    raw = await self._fetch("GET", endpoint, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_quick_margin_borrow_repay(
    self,
    inst_id: str,
    ccy: str,
    amt: str,
    side: Literal["borrow", "repay"],
):
    """
    Please note that this endpoint will be deprecated soon.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-manual-borrow-and-repay-in-quick-margin-mode
    """
    endpoint = "/api/v5/account/quick-margin-borrow-repay"
    payload = {
        "instId": inst_id,
        "ccy": ccy,
        "amt": amt,
        "side": side,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_quick_margin_borrow_repay_history(self, **kwargs):
    """
    Get borrow and repay history in Quick Margin Mode
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-borrow-and-repay-history-in-quick-margin-mode
    """
    endpoint = "/api/v5/account/quick-margin-borrow-repay-history"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_interest_limits(
    self, _type: str | None = None, ccy: str | None = None
):
    """
    Get borrow interest and limit
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-borrow-interest-and-limit
    """
    endpoint = "/api/v5/account/interest-limits"
    payload = {}
    if _type:
        payload["type"] = _type
    if ccy:
        payload["ccy"] = ccy
    raw = await self._fetch("GET", endpoint, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_fixed_loan_borrowing_limit(self):
    """
    Get fixed loan borrow limit
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-fixed-loan-borrow-limit
    """
    endpoint = "/api/v5/account/fixed-loan/borrowing-limit"

    raw = await self._fetch("GET", endpoint, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_fixed_loan_borrowing_quote(
    self, _type: Literal["normal", "reborrow"], **kwargs
):
    """
    Get fixed loan borrow quote
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-fixed-loan-borrow-quote
    """
    endpoint = "/api/v5/account/fixed-loan/borrowing-quote"
    payload = {"type": _type, **kwargs}

    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_fixed_loan_borrowing_order(
    self, ccy: str, amt: str, max_rate: str, term: str = "30D", **kwargs
):
    """
    For new borrowing orders, they belong to the IOC (immediately close and cancel the remaining) type. For renewal orders, they belong to the FOK (Fill-or-kill) type.
    Order book may refer to Get lending volume (public).
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-place-fixed-loan-borrowing-order
    """
    endpoint = "/api/v5/account/fixed-loan/borrowing-order"
    payload = {"ccy": ccy, "amt": amt, "term": term, "maxRate": max_rate, **kwargs}

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_fixed_loan_amend_borrowing_order(
    self, ord_id: str, **kwargs
):
    """
    Amend fixed loan borrowing order
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-amend-fixed-loan-borrowing-order
    """
    endpoint = "/api/v5/account/fixed-loan/amend-borrowing-order"
    payload = {"ordId": ord_id, **kwargs}

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_fixed_loan_manual_reborrow(
    self, ord_id: str, max_rate: str
):
    """
    Manual renew fixed loan borrowing order
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-manual-renew-fixed-loan-borrowing-order
    """
    endpoint = "/api/v5/account/fixed-loan/manual-reborrow"
    payload = {"ordId": ord_id, "maxRate": max_rate}

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_fixed_loan_repay_borrowing_order(
    self,
    ord_id: str,
):
    """
    Repay fixed loan borrowing order
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-repay-fixed-loan-borrowing-order
    """
    endpoint = "/api/v5/account/fixed-loan/repay-borrowing-order"
    payload = {
        "ordId": ord_id,
    }

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_fixed_loan_convert_to_market_loan(
    self,
    ord_id: str,
):
    """
    Convert fixed loan to market loan
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-convert-fixed-loan-to-market-loan
    """
    endpoint = "/api/v5/account/fixed-loan/convert-to-market-loan"
    payload = {
        "ordId": ord_id,
    }

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_fixed_loan_reduce_liabilities(
    self,
    ord_id: str,
    pending_repay: bool,
):
    """
    Provide the function of "setting pending repay state / canceling pending repay state" for fixed loan order.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-reduce-liabilities-for-fixed-loan
    """
    endpoint = "/api/v5/account/fixed-loan/reduce-liabilities"
    payload = {
        "ordId": ord_id,
        "pendingRepay": pending_repay,
    }

    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_fixed_loan_borrowing_orders_list(self, **kwargs):
    """
    Get fixed loan borrow order list
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-fixed-loan-borrow-order-list
    """
    endpoint = "/api/v5/account/fixed-loan/borrowing-orders-list"
    payload = {**kwargs}

    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_spot_manual_borrow_repay(
    self,
    ccy: str,
    amt: str,
    side: Literal["borrow", "repay"],
):
    """
    Only applicable to Spot mode (enabled borrowing)
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-manual-borrow-repay
    """
    endpoint = "/api/v5/account/spot-manual-borrow-repay"
    payload = {
        "ccy": ccy,
        "amt": amt,
        "side": side,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_set_auto_repay(
    self,
    auto_repay: bool,
):
    """
    Only applicable to Spot mode (enabled borrowing)
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-set-auto-repay
    """
    endpoint = "/api/v5/account/set-auto-repay"
    payload = {
        "autoRepay": auto_repay,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_spot_borrow_repay_history(self, **kwargs):
    """
    Retrieve the borrow/repay history under Spot mode
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-borrow-repay-history
    """
    endpoint = "/api/v5/account/spot-borrow-repay-history"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_position_builder(self, **kwargs):
    """
    Calculates portfolio margin information for virtual position/assets or current position of the user.
    You can add up to 200 virtual positions and 200 virtual assets in one request.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-position-builder-new
    """
    endpoint = "/api/v5/account/position-builder"
    payload = {**kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_set_risk_offset_amt(
    self,
    cl_spot_in_use_amt: str,
    ccy: str,
):
    """
    Set risk offset amount. This does not represent the actual spot risk offset amount. Only applicable to Portfolio Margin Mode.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-set-risk-offset-amount
    """
    endpoint = "/api/v5/account/set-riskOffset-amt"
    payload = {"clSpotInUseAmt": cl_spot_in_use_amt, "ccy": ccy}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_greeks(self, ccy: str | None = None):
    """
    Retrieve a greeks list of all assets in the account.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-greeks
    """
    endpoint = "/api/v5/account/greeks"
    payload = {}
    if ccy:
        payload["ccy"] = ccy
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_position_tiers(
    self, inst_type: Literal["SWAP", "FUTURES", "OPTION"], **kwargs
):
    """
    Retrieve cross position limitation of SWAP/FUTURES/OPTION under Portfolio margin mode.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-pm-position-limitation
    """
    endpoint = "/api/v5/account/position-tiers"
    payload = {"instType": inst_type, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_set_risk_offset_type(
    self, _type: Literal["1", "2", "3", "4"]
):
    """
    Configure the risk offset type in portfolio margin mode.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-set-risk-offset-type
    """
    endpoint = "/api/v5/account/set-riskOffset-type"
    payload = {"type": _type}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_activate_option(self):
    """
    Activate option
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-activate-option
    """
    endpoint = "/api/v5/account/activate-option"

    raw = await self._fetch("POST", endpoint, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_set_auto_loan(
    self,
    auto_loan: bool | None = None,
):
    """
    Only applicable to Multi-currency margin and Portfolio margin
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-set-auto-loan
    """
    endpoint = "/api/v5/account/set-auto-loan"
    payload = {}
    if auto_loan is not None:
        payload["autoLoan"] = auto_loan
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_account_level_switch_preset(
    self, acct_lv: Literal["2", "3", "4"], **kwargs
):
    """
    Pre-set the required information for account mode switching. When switching from Spot and futures mode / Multi-currency margin mode to Portfolio margin mode, you may optionally pre-set riskOffetType. When switching from Portfolio margin mode back to Spot and futures mode / Multi-currency margin mode, and if there are existing cross-margin contract positions, it is mandatory to pre-set leverage.
    If the user does not follow the required settings, they will receive an error message during the pre-check or when setting the account mode.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-preset-account-mode-switch
    """
    endpoint = "/api/v5/account/account-level-switch-preset"
    payload = {"acctLv": acct_lv, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_set_account_switch_precheck(
    self,
    acct_lv: Literal["1", "2", "3", "4"],
):
    """
    Retrieve precheck information for account mode switching.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-preset-account-mode-switch
    """
    endpoint = "/api/v5/account/set-account-switch-precheck"
    payload = {
        "acctLv": acct_lv,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_set_account_level(
    self,
    acct_lv: Literal["1", "2", "3", "4"],
):
    """
    You need to set on the Web/App for the first set of every account mode. If users plan to switch account modes while holding positions, they should first call the preset endpoint to conduct necessary settings, then call the precheck endpoint to get unmatched information, margin check, and other related information, and finally call the account mode switch endpoint to switch account modes.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-set-account-mode
    """
    endpoint = "/api/v5/account/set-account-level"
    payload = {
        "acctLv": acct_lv,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_mmp_reset(
    self, inst_family: str, inst_type: str = "OPTION"
):
    """
    You can unfreeze by this endpoint once MMP is triggered.
    Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-reset-mmp-status
    """
    endpoint = "/api/v5/account/mmp-reset"
    payload = {"instFamily": inst_family, "instType": inst_type}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_account_mmp_config(
    self,
    inst_family: str,
    time_interval: str,
    frozen_interval: str,
    qty_limit: str,
):
    """
    This endpoint is used to set MMP configure
    Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-set-mmp
    """
    endpoint = "/api/v5/account/mmp-config"
    payload = {
        "instFamily": inst_family,
        "timeInterval": time_interval,
        "frozenInterval": frozen_interval,
        "qtyLimit": qty_limit,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_account_mmp_config(self, inst_family: str | None = None):
    """
    This endpoint is used to get MMP configure information
    Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.
    https://www.okx.com/docs-v5/en/?shell#trading-account-rest-api-get-mmp-config
    """
    endpoint = "/api/v5/account/mmp-config"
    payload = {}
    if inst_family:
        payload["instFamily"] = inst_family
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)
