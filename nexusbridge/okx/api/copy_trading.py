from typing import Literal

import orjson


async def get_api_v5_copytrading_current_subpositions(self, **kwargs):
    """
    Retrieve lead positions that are not closed.
    Returns reverse chronological order with openTime
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-existing-lead-positions
    """
    endpoint = "/api/v5/copytrading/current-subpositions"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_subpositions_history(self, **kwargs):
    """
    Retrieve the completed lead position of the last 3 months.
    Returns reverse chronological order with subPosId
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-lead-position-history
    """
    endpoint = "/api/v5/copytrading/subpositions-history"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_copytrading_algo_order(self, sub_pos_id: str, **kwargs):
    """
    Set TP/SL for the current lead position that are not closed.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-post-place-lead-stop-order
    """
    endpoint = "/api/v5/copytrading/algo-order"
    payload = {"subPosId": sub_pos_id, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_copytrading_close_subposition(self, sub_pos_id: str, **kwargs):
    """
    You can only close a lead position once a time.
    It is required to pass subPosId which can get from Get existing leading positions.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-post-close-lead-position
    """
    endpoint = "/api/v5/copytrading/close-subposition"
    payload = {"subPosId": sub_pos_id, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_instruments(self, **kwargs):
    """
    Retrieve instruments that are supported to lead by the platform. Retrieve instruments that the lead trader has set.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-leading-instruments
    """
    endpoint = "/api/v5/copytrading/instruments"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_copytrading_set_instruments(self, inst_id: str, **kwargs):
    """
    The leading trader can amend current leading instruments, need to set initial leading instruments while applying to become a leading trader.
    All non-leading instruments can't have position or pending orders for the current request when setting non-leading instruments as leading instruments.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-post-amend-leading-instruments
    """
    endpoint = "/api/v5/copytrading/set-instruments"
    payload = {"instId": inst_id, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_profit_sharing_details(self, **kwargs):
    """
    The leading trader gets profits shared details for the last 3 months.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-profit-sharing-details
    """
    endpoint = "/api/v5/copytrading/profit-sharing-details"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_total_profit_sharing(
    self, inst_type: str | None = None
):
    """
    The leading trader gets the total amount of profit shared since joining the platform.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-total-profit-sharing
    """
    endpoint = "/api/v5/copytrading/total-profit-sharing"
    payload = {}
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_unrealized_profit_sharing_details(
    self, inst_type: str | None = None
):
    """
    The leading trader gets the profit sharing details that are expected to be shared in the next settlement cycle.
    The unrealized profit sharing details will update once there copy position is closed.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-unrealized-profit-sharing-details
    """
    endpoint = "/api/v5/copytrading/unrealized-profit-sharing-details"
    payload = {}
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_total_unrealized_profit_sharing(
    self, inst_type: str | None = None
):
    """
    The leading trader gets the total unrealized amount of profit shared.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-total-unrealized-profit-sharing
    """
    endpoint = "/api/v5/copytrading/total-unrealized-profit-sharing"
    payload = {}
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_copytrading_apply_lead_trading(
    self,
    inst_id: str,
    inst_type: str | None = None,
):
    """
    Only ND broker sub-account whitelisted can apply for lead trader by this endpoint. It will be passed immediately.
    Please reach out to BD for help if you want to be whitelisted.
    For other accounts, e.g. ND main accounts and general main and sub-accounts, still need to apply on the web manually
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-post-apply-for-lead-trading
    """
    endpoint = "/api/v5/copytrading/apply-lead-trading"
    payload = {
        "instId": inst_id,
    }
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_copytrading_stop_lead_trading(self, inst_type: str | None = None):
    """
    It is used to stop lead trading for ND broker sub-account.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-post-stop-lead-trading
    """
    endpoint = "/api/v5/copytrading/stop-lead-trading"
    payload = {}
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_copytrading_amend_profit_sharing_ratio(
    self,
    profit_sharing_ratio: str,
    inst_id: str | None = None,
):
    """
    It is used to amend profit sharing ratio.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-post-amend-profit-sharing-ratio
    """
    endpoint = "/api/v5/copytrading/amend-profit-sharing-ratio"
    payload = {"profitSharingRatio": profit_sharing_ratio}
    if inst_id:
        payload["instId"] = inst_id
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_config(self):
    """
    Retrieve the configuration of the copy trading system.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-copy-trading-config
    """
    endpoint = "/api/v5/copytrading/config"
    raw = await self._fetch("GET", endpoint, signed=True)
    return orjson.loads(raw)


async def post_api_v5_copytrading_first_copy_settings(
    self,
    unique_code: str,
    copy_mgn_mode: Literal["cross", "isolated", "copy"],
    copy_inst_id_type: Literal["custom", "copy"],
    copy_total_amt: str,
    sub_pos_close_type: Literal["market_close", "copy_close", "manual_close"],
    **kwargs,
):
    """
    The first copy settings for the certain lead trader. You need to first copy settings after stopping copying.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-post-first-copy-settings
    """
    endpoint = "/api/v5/copytrading/first-copy-settings"
    payload = {
        "uniqueCode": unique_code,
        "copyMgnMode": copy_mgn_mode,
        "copyInstIdType": copy_inst_id_type,
        "copyTotalAmt": copy_total_amt,
        "subPosCloseType": sub_pos_close_type,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_copytrading_amend_copy_settings(
    self,
    unique_code: str,
    copy_mgn_mode: Literal["cross", "isolated", "copy"],
    copy_inst_id_type: Literal["custom", "copy"],
    copy_total_amt: str,
    sub_pos_close_type: Literal["market_close", "copy_close", "manual_close"],
    **kwargs,
):
    """
    You need to use this endpoint to amend copy settings
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-post-amend-copy-settings
    """
    endpoint = "/api/v5/copytrading/amend-copy-settings"
    payload = {
        "uniqueCode": unique_code,
        "copyMgnMode": copy_mgn_mode,
        "copyInstIdType": copy_inst_id_type,
        "copyTotalAmt": copy_total_amt,
        "subPosCloseType": sub_pos_close_type,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_api_v5_copytrading_stop_copy_trading(
    self,
    unique_code: str,
    sub_pos_close_type: Literal["market_close", "copy_close", "manual_close"],
    inst_type: str | None = None,
):
    """
    You need to use this endpoint to stop copy trading
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-post-stop-copying
    """
    endpoint = "/api/v5/copytrading/stop-copy-trading"
    payload = {
        "uniqueCode": unique_code,
        "subPosCloseType": sub_pos_close_type,
    }
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_copy_settings(
    self,
    unique_code: str,
    inst_type: str | None = None,
):
    """
    Retrieve the copy settings about certain lead trader.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-copy-settings
    """
    endpoint = "/api/v5/copytrading/copy-settings"
    payload = {
        "uniqueCode": unique_code,
    }
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_current_lead_traders(
    self,
    inst_type: str | None = None,
):
    """
    Retrieve my lead traders.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-my-lead-traders
    """
    endpoint = "/api/v5/copytrading/current-lead-traders"
    payload = {}
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_public_config(self, inst_type: str | None = None):
    """
    Public endpoint. Retrieve copy trading parameter configuration information of copy settings
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-copy-trading-configuration
    """
    endpoint = "/api/v5/copytrading/public-config"
    payload = {}
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_copytrading_public_lead_traders(self, **kwargs):
    """
    Retrieve public lead traders.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-lead-trader-ranks
    """
    endpoint = "/api/v5/copytrading/public-lead-traders"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_copytrading_public_weekly_pnl(
    self,
    unique_code: str,
    inst_type: str | None = None,
):
    """
    Public endpoint. Retrieve lead trader weekly pnl. Results are returned in counter chronological order.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-lead-trader-weekly-pnl
    """
    endpoint = "/api/v5/copytrading/public-weekly-pnl"
    payload = {
        "uniqueCode": unique_code,
    }
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_copytrading_public_pnl(
    self,
    unique_code: str,
    last_days: Literal["1", "2", "3", "4"],
    inst_type: str | None = None,
):
    """
    Public endpoint. Retrieve lead trader daily pnl. Results are returned in counter chronological order.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-lead-trader-daily-pnl
    """
    endpoint = "/api/v5/copytrading/public-pnl"
    payload = {
        "uniqueCode": unique_code,
        "lastDays": last_days,
    }
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_copytrading_public_stats(
    self,
    unique_code: str,
    last_days: Literal["1", "2", "3", "4"],
    inst_type: str | None = None,
):
    """
    Public endpoint. Key data related to lead trader performance.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-lead-trader-stats
    """
    endpoint = "/api/v5/copytrading/public-stats"
    payload = {
        "uniqueCode": unique_code,
        "lastDays": last_days,
    }
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_copytrading_public_preference_currency(
    self,
    unique_code: str,
    inst_type: str | None = None,
):
    """
    Public endpoint. The most frequently traded crypto of this lead trader. Results are sorted by ratio from large to small.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-lead-trader-currency-preferences
    """
    endpoint = "/api/v5/copytrading/public-preference-currency"
    payload = {
        "uniqueCode": unique_code,
    }
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_copytrading_public_current_subpositions(
    self, unique_code: str, **kwargs
):
    """
    Public endpoint. Get current leading positions of lead trader
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-lead-trader-current-lead-positions
    """
    endpoint = "/api/v5/copytrading/public-current-subpositions"
    payload = {"uniqueCode": unique_code, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_copytrading_public_subpositions_history(
    self, unique_code: str, **kwargs
):
    """
    Public endpoint. Retrieve the lead trader completed leading position of the last 3 months.
    Returns reverse chronological order with subPosId.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-lead-trader-lead-position-history
    """
    endpoint = "/api/v5/copytrading/public-subpositions-history"
    payload = {"uniqueCode": unique_code, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_copytrading_public_copy_traders(self, unique_code: str, **kwargs):
    """
    Public endpoint. Retrieve copy trader coming from certain lead trader. Return according to pnl from high to low
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-copy-traders
    """
    endpoint = "/api/v5/copytrading/public-copy-traders"
    payload = {"uniqueCode": unique_code, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_copytrading_lead_traders(self, **kwargs):
    """
    Private endpoint. Retrieve lead trader ranks.
    For requests from the ND sub-account, under the same ND broker, this private endpoint can return ND lead trader information that the related public endpoint can't return.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-lead-trader-ranks-private
    """
    endpoint = "/api/v5/copytrading/lead-traders"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_weekly_pnl(
    self,
    unique_code: str,
    inst_type: str | None = None,
):
    """
    Private endpoint. Retrieve lead trader weekly pnl. Results are returned in counter chronological order.
    For requests from the ND sub-account, under the same ND broker, uniqueCode is supported for ND lead trader unique code by this endpoint, but the related public endpoint does not support it.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-lead-trader-weekly-pnl-private
    """
    endpoint = "/api/v5/copytrading/weekly-pnl"
    payload = {
        "uniqueCode": unique_code,
    }
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_pnl(
    self,
    unique_code: str,
    last_days: Literal["1", "2", "3", "4"],
    inst_type: str | None = None,
):
    """
    Private endpoint. Retrieve lead trader daily pnl. Results are returned in counter chronological order.
    For requests from the ND sub-account, under the same ND broker, uniqueCode is supported for ND lead trader unique code by this endpoint, but the related public endpoint does not support it.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-lead-trader-daily-pnl-private
    """
    endpoint = "/api/v5/copytrading/pnl"
    payload = {
        "uniqueCode": unique_code,
        "lastDays": last_days,
    }
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_stats(
    self,
    unique_code: str,
    last_days: Literal["1", "2", "3", "4"],
    inst_type: str | None = None,
):
    """
    Private endpoint. Key data related to lead trader performance.
    For requests from the ND sub-account, under the same ND broker, uniqueCode is supported for ND lead trader unique code by this endpoint, but the related public endpoint does not support it.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-lead-trader-stats-private
    """
    endpoint = "/api/v5/copytrading/stats"
    payload = {
        "uniqueCode": unique_code,
        "lastDays": last_days,
    }
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_preference_currency(
    self, unique_code: str, inst_type: str | None = None
):
    """
    Private endpoint. The most frequently traded crypto of this lead trader. Results are sorted by ratio from large to small.
    For requests from the ND sub-account, under the same ND broker, uniqueCode is supported for ND lead trader unique code by this endpoint, but the related public endpoint does not support it.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-lead-trader-currency-preferences-private
    """
    endpoint = "/api/v5/copytrading/preference-currency"
    payload = {
        "uniqueCode": unique_code,
    }
    if inst_type:
        payload["instType"] = inst_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_performance_current_subpositions(
    self, unique_code: str, **kwargs
):
    """
    Private endpoint. Get current leading positions of lead trader
    For requests from the ND sub-account, under the same ND broker, uniqueCode is supported for ND lead trader unique code by this endpoint, but the related public endpoint does not support it.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-performance-of-existing-lead-positions
    """
    endpoint = "/api/v5/copytrading/performance-current-subpositions"
    payload = {"uniqueCode": unique_code, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_performance_subpositions_history(
    self, unique_code: str, **kwargs
):
    """
    Private endpoint. Retrieve the lead trader completed leading position of the last 3 months.
    Returns reverse chronological order with subPosId.
    For requests from the ND sub-account, under the same ND broker, uniqueCode is supported for ND lead trader unique code by this endpoint, but the related public endpoint does not support it.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-performance-of-lead-position-history
    """
    endpoint = "/api/v5/copytrading/performance-subpositions-history"
    payload = {"uniqueCode": unique_code, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_api_v5_copytrading_copy_traders(self, unique_code: str, **kwargs):
    """
    Private endpoint. Retrieve copy trader coming from certain lead trader. Return according to pnl from high to low
    For requests from the ND sub-account, under the same ND broker, uniqueCode is supported for ND lead trader unique code by this endpoint, but the related public endpoint does not support it.
    https://www.okx.com/docs-v5/en/?shell#order-book-trading-copy-trading-get-copy-traders
    """
    endpoint = "/api/v5/copytrading/copy-traders"
    payload = {"uniqueCode": unique_code, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)
