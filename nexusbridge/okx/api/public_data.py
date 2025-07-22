from typing import Literal

import orjson


async def get_api_v5_public_instruments(
    self, inst_type: Literal["SPOT", "MARGIN", "FUTURES", "SWAP", "OPTION"], **kwargs
):
    """
    Retrieve a list of instruments with open contracts.
    https://www.okx.com/docs-v5/en/?shell#public-data-rest-api-get-instruments
    """
    endpoint = "/api/v5/public/instruments"
    payload = {
        "instType": inst_type,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_delivery_exercise_history(
    self, inst_type: Literal["FUTURES", "OPTION"], **kwargs
):
    """
    Retrieve delivery records of Futures and exercise records of Options in the last 3 months.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-delivery-exercise-history
    """
    endpoint = "/api/v5/public/delivery-exercise-history"
    payload = {
        "instType": inst_type,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_open_interest(
    self, inst_type: Literal["FUTURES", "SWAP", "OPTION"], **kwargs
):
    """
    Retrieve the total open interest for contracts on OKX.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-open-interest
    """
    endpoint = "/api/v5/public/open-interest"
    payload = {
        "instType": inst_type,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_funding_rate(
    self,
    inst_id: str,
):
    """
    Retrieve funding rate.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-funding-rate
    """
    endpoint = "/api/v5/public/funding-rate"
    payload = {
        "instId": inst_id,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_funding_rate_history(self, inst_id: str, **kwargs):
    """
    Retrieve funding rate history. This endpoint can retrieve data from the last 3 months.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-funding-rate-history
    """
    endpoint = "/api/v5/public/funding-rate-history"
    payload = {
        "instId": inst_id,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_price_limit(
    self,
    inst_id: str,
):
    """
    Retrieve the highest buy limit and lowest sell limit of the instrument.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-limit-price
    """
    endpoint = "/api/v5/public/price-limit"
    payload = {
        "instId": inst_id,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_opt_summary(self, **kwargs):
    """
    Retrieve option market data.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-option-market-data
    """
    endpoint = "/api/v5/public/opt-summary"
    payload = {
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_estimated_price(self, inst_id: str):
    """
    Retrieve the estimated delivery price which will only have a return value one hour before the delivery/exercise.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-estimated-delivery-exercise-price
    """
    endpoint = "/api/v5/public/estimated-price"
    payload = {
        "instId": inst_id,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_discount_rate_interest_free_quota(self, **kwargs):
    """
    Retrieve discount rate level and interest-free quota.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-discount-rate-and-interest-free-quota
    """
    endpoint = "/api/v5/public/discount-rate-interest-free-quota"
    payload = {
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_time(self):
    """
    Retrieve API server time.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-system-time
    """
    endpoint = "/api/v5/public/time"
    raw = await self._fetch("GET", endpoint, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_mark_price(
    self, inst_id: Literal["MARGIN", "SWAP", "FUTURES", "OPTION"], **kwargs
):
    """
    Retrieve mark price.
    We set the mark price based on the SPOT index and at a reasonable basis to prevent individual users from manipulating the market and causing the contract price to fluctuate.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-mark-price
    """
    endpoint = "/api/v5/public/mark-price"
    payload = {
        "instId": inst_id,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_position_tiers(
    self,
    inst_type: Literal["MARGIN", "SWAP", "FUTURES", "OPTION"],
    td_mode: Literal["cross", "isolated"],
    **kwargs,
):
    """
    Retrieve position tiers information, maximum leverage depends on your borrowings and margin ratio.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-position-tiers
    """

    endpoint = "/api/v5/public/position-tiers"
    payload = {
        "instType": inst_type,
        "tdMode": td_mode,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_interest_rate_loan_quota(self):
    """
    Retrieve interest rate
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-interest-rate-and-loan-quota
    """
    endpoint = "/api/v5/public/interest-rate-loan-quota"

    raw = await self._fetch("GET", endpoint, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_underlying(
    self, inst_type: Literal["SWAP", "FUTURES", "OPTION"]
):
    """
    Retrieve underlying index information.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-underlying-index
    """
    endpoint = "/api/v5/public/underlying"
    payload = {
        "instType": inst_type,
    }

    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_insurance_fund(
    self, inst_type: Literal["MARGIN", "SWAP", "FUTURES", "OPTION"], **kwargs
):
    """
    Get insurance fund balance information
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-insurance-fund
    """
    endpoint = "/api/v5/public/insurance-fund"
    payload = {
        "instType": inst_type,
        **kwargs,
    }

    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_convert_contract_coin(
    self, inst_id: str, sz: str, **kwargs
):
    """
    Convert the crypto value to the number of contracts, or vice versa
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-insurance-fund
    """
    endpoint = "/api/v5/public/convert-contract-coin"
    payload = {
        "instId": inst_id,
        "sz": sz,
        **kwargs,
    }

    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_instrument_tick_bands(
    self,
    inst_type: str = "OPTION",
    inst_family: str | None = None,
):
    """
    Get option tick bands information
    https://www.okx.com/docs-v5/en/?shell#public-data-rest-api-get-option-tick-bands
    """
    endpoint = "/api/v5/public/instrument-tick-bands"
    payload = {
        "instType": inst_type,
    }
    if inst_family:
        payload["instFamily"] = inst_family
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_premium_history(self, inst_id: str, **kwargs):
    """
    It will return premium data in the past 6 months.
    https://www.okx.com/docs-v5/en/?shell#public-data-rest-api-get-premium-history
    """
    endpoint = "/api/v5/public/premium-history"
    payload = {
        "instId": inst_id,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_index_tickers(self, **kwargs):
    """
    Retrieve index tickers.
    https://www.okx.com/docs-v5/en/?shell#public-data-rest-api-get-index-tickers
    """
    endpoint = "/api/v5/market/index-tickers"
    payload = {
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_index_candles(self, inst_id: str, **kwargs):
    """
    Retrieve the candlestick charts of the index. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar.
    https://www.okx.com/docs-v5/en/?shell#public-data-rest-api-get-index-candlesticks
    """
    endpoint = "/api/v5/market/index-candles"
    payload = {
        "instId": inst_id,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_history_index_candles(self, inst_id: str, **kwargs):
    """
    Retrieve the candlestick charts of the index from recent years.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-index-candlesticks-history
    """
    endpoint = "/api/v5/market/history-index-candles"
    payload = {
        "instId": inst_id,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_mark_price_candles(self, inst_id: str, **kwargs):
    """
    Retrieve the candlestick charts of mark price. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar.
    https://www.okx.com/docs-v5/en/?shell#public-data-rest-api-get-mark-price-candlesticks
    """
    endpoint = "/api/v5/market/mark-price-candles"
    payload = {
        "instId": inst_id,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_history_mark_price_candles(self, inst_id: str, **kwargs):
    """
    Retrieve the candlestick charts of mark price from recent years.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-mark-price-candlesticks-history
    """
    endpoint = "/api/v5/market/history-mark-price-candles"
    payload = {
        "instId": inst_id,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_open_oracle(self):
    """
    Get the crypto price of signing using Open Oracle smart contract.
    https://www.okx.com/docs-v5/en/?shell#public-data-rest-api-get-oracle
    """
    endpoint = "/api/v5/market/open-oracle"

    raw = await self._fetch("GET", endpoint, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_exchange_rate(self):
    """
    This interface provides the average exchange rate data for 2 weeks
    https://www.okx.com/docs-v5/en/?shell#public-data-rest-api-get-exchange-rate
    """
    endpoint = "/api/v5/market/exchange-rate"

    raw = await self._fetch("GET", endpoint, signed=False)
    return orjson.loads(raw)


async def get_api_v5_market_index_components(self, index: str):
    """
    Get the index component information data on the market
    https://www.okx.com/docs-v5/en/?shell#public-data-rest-api-get-index-components
    """
    endpoint = "/api/v5/market/index-components"
    payload = {
        "index": index,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=False)
    return orjson.loads(raw)


async def get_api_v5_public_economic_calendar(self, **kwargs):
    """
    Get the macro-economic calendar data within 3 months. Historical data from 3 months ago is only available to users with trading fee tier VIP1 and above.
    https://www.okx.com/docs-v5/en/?python#public-data-rest-api-get-economic-calendar-data
    """
    endpoint = "/api/v5/public/economic-calendar"
    payload = {
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)
