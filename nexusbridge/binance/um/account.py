from typing import Literal


async def get_fapi_v3_balance(self, **kwargs):
    """
    Query account balance info
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V3
    """
    endpoint = "/fapi/v3/balance"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v2_balance(self, **kwargs):
    """
    Query account balance info
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2
    """
    endpoint = "/fapi/v2/balance"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v3_account(self, **kwargs):
    """
    Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V3
    """
    endpoint = "/fapi/v3/account"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v2_account(self, **kwargs):
    """
    Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2
    """
    endpoint = "/fapi/v2/account"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_commission_rate(self, symbol: str, **kwargs):
    """
    Get User Commission Rate
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate
    """
    endpoint = "/fapi/v1/commissionRate"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_account_config(self, **kwargs):
    """
    Query account configuration
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Config
    """
    endpoint = "/fapi/v1/accountConfig"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_symbol_config(self, **kwargs):
    """
    Get current account symbol configuration.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config
    """
    endpoint = "/fapi/v1/symbolConfig"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_rate_limit_order(self, **kwargs):
    """
    Query User Rate Limit
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Query-Rate-Limit
    """
    endpoint = "/fapi/v1/rateLimit/order"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_leverage_bracket(self, **kwargs):
    """
    Query user notional and leverage bracket on speicfic symbol
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets
    """
    endpoint = "/fapi/v1/leverageBracket"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_multi_assets_margin(self, **kwargs):
    """
    Get user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode
    """
    endpoint = "/fapi/v1/multiAssetsMargin"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_position_side_dual(self, **kwargs):
    """
    Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Position-Mode
    """
    endpoint = "/fapi/v1/positionSide/dual"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_income(self, **kwargs):
    """
    Query income history
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Income-History
    """
    endpoint = "/fapi/v1/income"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_api_trading_status(self, **kwargs):
    """
    Futures trading quantitative rules indicators, for more information on this, please refer to the Futures Trading Quantitative Rules
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Trading-Quantitative-Rules-Indicators
    """
    endpoint = "/fapi/v1/apiTradingStatus"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_income_asyn(self, start_time: int, end_time: int, **kwargs):
    """
    Get download id for futures transaction history
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Transaction-History
    """
    endpoint = "/fapi/v1/income/asyn"
    payload = {"startTime": start_time, "endTime": end_time, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_income_asyn_id(self, download_id: str, **kwargs):
    """
    Get futures transaction history download link by Id
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Futures-Transaction-History-Download-Link-by-Id
    """
    endpoint = "/fapi/v1/income/asyn/id"
    payload = {"downloadId": download_id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_order_asyn(self, start_time: int, end_time: int, **kwargs):
    """
    Get Download Id For Futures Order History
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Order-History
    """
    endpoint = "/fapi/v1/order/asyn"
    payload = {"startTime": start_time, "endTime": end_time, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_order_asyn_id(self, download_id: str, **kwargs):
    """
    Get futures order history download link by Id
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Futures-Order-History-Download-Link-by-Id
    """
    endpoint = "/fapi/v1/order/asyn/id"
    payload = {"downloadId": download_id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_trade_asyn(self, start_time: int, end_time: int, **kwargs):
    """
    Get download id for futures trade history
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Trade-History
    """
    endpoint = "/fapi/v1/trade/asyn"
    payload = {"startTime": start_time, "endTime": end_time, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_trade_asyn_id(self, download_id: str, **kwargs):
    """
    Get futures trade download link by Id
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Futures-Trade-Download-Link-by-Id
    """
    endpoint = "/fapi/v1/trade/asyn/id"
    payload = {"downloadId": download_id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def post_fapi_v1_fee_burn(self, fee_burn: Literal["true", "false"], **kwargs):
    """
    Change user's BNB Fee Discount (Fee Discount On or Fee Discount Off ) on EVERY symbol
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade
    """
    endpoint = "/fapi/v1/feeBurn"
    payload = {"feeBurn": fee_burn, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)

    return raw


async def get_fapi_v1_fee_burn(self, **kwargs):
    """
    Get user's BNB Fee Discount (Fee Discount On or Fee Discount Off )
    https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status
    """
    endpoint = "/fapi/v1/feeBurn"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_fapi_v1_pm_account_info(self, asset: str, **kwargs):
    """
    Get Classic Portfolio Margin current account information.
    https://developers.binance.com/docs/derivatives/usds-margined-futures/portfolio-margin-endpoints
    """
    endpoint = "/fapi/v1/pmAccountInfo"
    payload = {"asset": asset, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw
