from typing import Literal

from nexus.binance.base import BinanceApiClient
from nexus.binance.constants import BinanceUrl, ALL_URL, BinanceInstrumentType


class UsdmTradingApi(BinanceApiClient):
    def __init__(
            self,
            key=None,
            secret=None,
            binance_url: Literal[BinanceUrl.MAIN, BinanceUrl.TEST] = BinanceUrl.MAIN,
            **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = ALL_URL[BinanceInstrumentType.Derivatives_UM].get_url(binance_url)
        super().__init__(key=key, secret=secret, **kwargs)

    # Market Data endpoints
    from nexus.binance.um.market_data import get_fapi_v1_ping
    from nexus.binance.um.market_data import get_fapi_v1_time

    # Trading endpoints
    from nexus.binance.um.trade import fapi_v1_order
