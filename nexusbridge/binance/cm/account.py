from typing import Literal


async def get_dapi_v1_balance(self, **kwargs):
    """
    Query account balance info
    https://developers.binance.com/docs/derivatives/coin-margined-futures/account/Futures-Account-Balance
    """
    endpoint = "/dapi/v1/balance"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_account(self, **kwargs):
    """
    Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/account/Account-Information
    """
    endpoint = "/dapi/v1/account"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_commission_rate(self, symbol: str, **kwargs):
    """
    Query user commission rate
    https://developers.binance.com/docs/derivatives/coin-margined-futures/account/User-Commission-Rate
    """
    endpoint = "/dapi/v1/commissionRate"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v2_leverage_bracket(self, **kwargs):
    """
    Get the symbol's notional bracket list.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/account/Notional-Bracket-for-Symbol
    """
    endpoint = "/dapi/v2/leverageBracket"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_leverage_bracket(self, **kwargs):
    """
    Not recommended to continue using this v1 endpoint
    Get the pair's default notional bracket list, may return ambiguous values when there have been multiple different symbol brackets under the pair, suggest using the following GET /dapi/v2/leverageBracket query instead to get the specific symbol notional bracket list.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/account/Notional-Bracket-for-Pair
    """
    endpoint = "/dapi/v1/leverageBracket"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_position_side_dual(self, **kwargs):
    """
    Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol
    https://developers.binance.com/docs/derivatives/coin-margined-futures/account/Get-Current-Position-Mode
    """
    endpoint = "/dapi/v1/positionSide/dual"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_income(self, **kwargs):
    """
    Query income history
    https://developers.binance.com/docs/derivatives/coin-margined-futures/account/Get-Income-History
    """
    endpoint = "/dapi/v1/income"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_income_asyn(self, start_time: int, end_time: int, **kwargs):
    """
    Get download id for futures transaction history
    https://developers.binance.com/docs/derivatives/coin-margined-futures/account/Get-Download-Id-For-Futures-Transaction-History
    """
    endpoint = "/dapi/v1/income/asyn"
    payload = {"startTime": start_time, "endTime": end_time, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_income_asyn_id(self, download_id: str, **kwargs):
    """
    Get futures transaction history download link by Id
    https://developers.binance.com/docs/derivatives/coin-margined-futures/account/Get-Futures-Transaction-History-Download-Link-by-Id
    """
    endpoint = "/dapi/v1/income/asyn/id"
    payload = {"downloadId": download_id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_order_asyn(self, start_time: int, end_time: int, **kwargs):
    """
    Get Download Id For Futures Order History
    https://developers.binance.com/docs/derivatives/coin-margined-futures/account/Get-Download-Id-For-Futures-Order-History
    """
    endpoint = "/dapi/v1/order/asyn"
    payload = {"startTime": start_time, "endTime": end_time, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_order_asyn_id(self, download_id: str, **kwargs):
    """
    Get futures order history download link by Id
    https://developers.binance.com/docs/derivatives/coin-margined-futures/account/Get-Futures-Order-History-Download-Link-by-Id
    """
    endpoint = "/dapi/v1/order/asyn/id"
    payload = {"downloadId": download_id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_trade_asyn(self, start_time: int, end_time: int, **kwargs):
    """
    Get download id for futures trade history
    https://developers.binance.com/docs/derivatives/coin-margined-futures/account/Get-Download-Id-For-Futures-Trade-History
    """
    endpoint = "/dapi/v1/trade/asyn"
    payload = {"startTime": start_time, "endTime": end_time, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_trade_asyn_id(self, download_id: str, **kwargs):
    """
    Get futures trade download link by Id
    https://developers.binance.com/docs/derivatives/coin-margined-futures/account/Get-Futures-Trade-Download-Link-by-Id
    """
    endpoint = "/dapi/v1/trade/asyn/id"
    payload = {"downloadId": download_id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_dapi_v1_pm_account_info(self, asset: str, **kwargs):
    """
    Get Classic Portfolio Margin current account information.
    https://developers.binance.com/docs/derivatives/coin-margined-futures/portfolio-margin-endpoints
    """
    endpoint = "/dapi/v1/pmAccountInfo"
    payload = {"asset": asset, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw
