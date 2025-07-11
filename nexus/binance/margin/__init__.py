from typing import Literal

from nexus.binance.base import BinanceApiClient
from nexus.binance.constants import BinanceUrl, ALL_URL, BinanceInstrumentType


class MarginTradingApi(BinanceApiClient):
    def __init__(
            self,
            key=None,
            secret=None,
            binance_url: Literal[BinanceUrl.MAIN, BinanceUrl.TEST] = BinanceUrl.MAIN,
            **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = ALL_URL[BinanceInstrumentType.MARGIN].get_url(binance_url)
        super().__init__(key=key, secret=secret, **kwargs)
    
    from nexus.binance.margin.account import get_sapi_v1_simpleEarn_flexible_list
    from nexus.binance.margin.account import get_sapi_v1_simpleEarn_locked_list
    from nexus.binance.margin.history import get_sapi_v1_simpleEarn_flexible_history_rateHistory
    from nexus.binance.margin.history import get_sapi_v1_simpleEarn_flexible_history_rewardsRecord
    from nexus.binance.margin.history import get_sapi_v1_simpleEarn_locked_history_rewardsRecord
