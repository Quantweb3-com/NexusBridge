from typing import Literal


async def get_papi_v1_balance(self, **kwargs):
    endpoint = "/papi/v1/balance"
    """
    Query account balance
    https://developers.binance.com/docs/derivatives/portfolio-margin/account
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_account(self, **kwargs):
    endpoint = "/papi/v1/account"
    """
    Query account information
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Account-Information
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_margin_max_borrowable(self, asset: str, **kwargs):
    endpoint = "/papi/v1/margin/maxBorrowable"
    """
    Query margin max borrow
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Margin-Max-Borrow
    """
    payload = {"asset": asset, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_margin_max_withdraw(self, asset: str, **kwargs):
    endpoint = "/papi/v1/margin/maxWithdraw"
    """
    Query Margin Max Withdraw
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw
    """
    payload = {"asset": asset, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_position_risk(self, **kwargs):
    endpoint = "/papi/v1/um/positionRisk"
    """
    Get current UM position information.
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Query-UM-Position-Information
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_position_risk(self, **kwargs):
    endpoint = "/papi/v1/cm/positionRisk"
    """
    Get current CM position information.
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Query-CM-Position-Information
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def post_papi_v1_um_leverage(self, symbol: str, leverage: int, **kwargs):
    endpoint = "/papi/v1/um/leverage"
    """
    Change user's initial leverage of specific symbol in UM.
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage
    """
    payload = {"symbol": symbol, "leverage": leverage, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_papi_v1_cm_leverage(self, symbol: str, leverage: int, **kwargs):
    endpoint = "/papi/v1/cm/leverage"
    """
    Change user's initial leverage of specific symbol in CM.
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage
    """
    payload = {"symbol": symbol, "leverage": leverage, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_papi_v1_um_position_side_dual(
    self, dual_side_position: Literal["true", "false"], **kwargs
):
    endpoint = "/papi/v1/um/positionSide/dual"
    """
    Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in UM
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Change-UM-Position-Mode
    """
    payload = {"dualSidePosition": dual_side_position, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_papi_v1_cm_position_side_dual(
    self, dual_side_position: Literal["true", "false"], **kwargs
):
    endpoint = "/papi/v1/cm/positionSide/dual"
    """
    Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in CM
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Change-CM-Position-Mode
    """
    payload = {"dualSidePosition": dual_side_position, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_position_side_dual(self, **kwargs):
    endpoint = "/papi/v1/um/positionSide/dual"
    """
    Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in UM
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_position_side_dual(self, **kwargs):
    endpoint = "/papi/v1/cm/positionSide/dual"
    """
    Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in CM
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-CM-Current-Position-Mode
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_leverage_bracket(self, **kwargs):
    endpoint = "/papi/v1/um/leverageBracket"
    """
    Query UM notional and leverage brackets
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_leverage_bracket(self, **kwargs):
    endpoint = "/papi/v1/cm/leverageBracket"
    """
    Query CM notional and leverage brackets
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_api_trading_status(self, **kwargs):
    endpoint = "/papi/v1/um/apiTradingStatus"
    """
    Portfolio Margin UM Trading Quantitative Rules Indicators
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_commission_rate(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/um/commissionRate"
    """
    Get User Commission Rate for UM
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_commission_rate(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/cm/commissionRate"
    """
    Get User Commission Rate for CM
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_margin_margin_loan(self, asset: str, **kwargs):
    endpoint = "/papi/v1/margin/marginLoan"
    """
    Query margin loan record
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Query-Margin-Loan-Record
    """
    payload = {"asset": asset, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_margin_repay_loan(self, asset: str, **kwargs):
    endpoint = "/papi/v1/margin/repayLoan"
    """
    Query margin repay record.
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Query-Margin-repay-Record
    """
    payload = {"asset": asset, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_repay_futures_switch(self, **kwargs):
    endpoint = "/papi/v1/repay-futures-switch"
    """
    Query Auto-repay-futures Status
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def post_papi_v1_repay_futures_switch(
    self, auto_repay: Literal["true", "false"], **kwargs
):
    endpoint = "/papi/v1/repay-futures-switch"
    """
    Change Auto-repay-futures Status
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status
    """
    payload = {"autoRepay": auto_repay, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_margin_margin_interest_history(self, **kwargs):
    endpoint = "/papi/v1/margin/marginInterestHistory"
    """
    Get Margin Borrow/Loan Interest History
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def post_papi_v1_repay_futures_negative_balance(self, **kwargs):
    endpoint = "/papi/v1/repay-futures-negative-balance"
    """
    Repay futures Negative Balance
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Repay-futures-Negative-Balance
    """
    payload = {**kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_portfolio_interest_history(self, **kwargs):
    endpoint = "/papi/v1/portfolio/interest-history"
    """
    Query interest history of negative balance for portfolio margin.
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def post_papi_v1_auto_collection(self, **kwargs):
    endpoint = "/papi/v1/auto-collection"
    """
    Fund collection for Portfolio Margin
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Fund-Auto-collection
    """
    payload = {**kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_papi_v1_asset_collection(self, asset: str, **kwargs):
    endpoint = "/papi/v1/asset-collection"
    """
    Transfers specific asset from Futures Account to Margin account
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Fund-Collection-by-Asset
    """
    payload = {"asset": asset, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_papi_v1_bnb_transfer(
    self, transfer_side: Literal["TO_UM", "FROM_UM"], amount: float, **kwargs
):
    endpoint = "/papi/v1/bnb-transfer"
    """
    Transfer BNB in and out of UM
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/BNB-transfer
    """
    payload = {"transferSide": transfer_side, "amount": amount, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_income(self, **kwargs):
    endpoint = "/papi/v1/um/income"
    """
    Get UM Income History
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Income-History
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_income(self, **kwargs):
    endpoint = "/papi/v1/cm/income"
    """
    Get CM Income History
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-CM-Income-History
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_account(self, **kwargs):
    endpoint = "/papi/v1/um/account"
    """
    Get current UM account asset and position information.
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Account-Detail
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_account(self, **kwargs):
    endpoint = "/papi/v1/cm/account"
    """
    Get current CM account asset and position information.
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-CM-Account-Detail
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_account_config(self, **kwargs):
    endpoint = "/papi/v1/um/accountConfig"
    """
    Query UM Futures account configuration
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_symbol_config(self, **kwargs):
    endpoint = "/papi/v1/um/symbolConfig"
    """
    Get current UM account symbol configuration.
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v2_um_account(self, **kwargs):
    endpoint = "/papi/v2/um/account"
    """
    Get current UM account asset and position information.
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Account-Detail-V2
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_trade_asyn(self, start_time: int, end_time: int, **kwargs):
    endpoint = "/papi/v1/um/trade/asyn"
    """
    Get download id for UM futures trade history
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Trade-History
    """
    payload = {"startTime": start_time, "endTime": end_time, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_trade_asyn_id(self, _id: str, **kwargs):
    endpoint = "/papi/v1/um/trade/asyn/id"
    """
    Get UM futures trade download link by Id
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Trade-Download-Link-by-Id
    """
    payload = {"downloadId": _id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_order_asyn(self, start_time: int, end_time: int, **kwargs):
    endpoint = "/papi/v1/um/order/asyn"
    """
    Get download id for UM futures order history
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History
    """
    payload = {"startTime": start_time, "endTime": end_time, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)

    return raw


async def get_papi_v1_um_order_asyn_id(self, _id: str, **kwargs):
    endpoint = "/papi/v1/um/order/asyn/id"
    """
    Get UM futures order download link by Id
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id
    """
    payload = {"downloadId": _id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_income_asyn(self, start_time: int, end_time: int, **kwargs):
    endpoint = "/papi/v1/um/income/asyn"
    """
    Get download id for UM futures transaction history
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Transaction-History
    """
    payload = {"startTime": start_time, "endTime": end_time, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_income_asyn_id(self, _id: str, **kwargs):
    endpoint = "/papi/v1/um/income/asyn/id"
    """
    Get UM futures Transaction download link by Id
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Transaction-Download-Link-by-Id
    """
    payload = {"downloadId": _id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_rate_limit_order(self, **kwargs):
    endpoint = "/papi/v1/rateLimit/order"
    """
    Query User Rate Limit
    https://developers.binance.com/docs/derivatives/portfolio-margin/account/Query-User-Rate-Limit
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw
