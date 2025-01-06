from typing import Literal

from nexus.binance.base import BinanceApiClient
from nexus.binance.constants import BinanceUrl, ALL_URL, BinanceInstrumentType


class SpotTradingApi(BinanceApiClient):
    def __init__(
            self,
            key=None,
            secret=None,
            binance_url: Literal[BinanceUrl.MAIN, BinanceUrl.TEST] = BinanceUrl.MAIN,
            **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = ALL_URL[BinanceInstrumentType.SPOT].get_url(binance_url)
        super().__init__(key=key, secret=secret, **kwargs)

    # General endpoints
    from nexus.binance.spot.general import get_api_v3_ping
    from nexus.binance.spot.general import get_api_v3_time
    from nexus.binance.spot.general import get_api_v3_exchangeInfo

    # Market Data endpoints
    from nexus.binance.spot.market_data import get_api_v3_depth
    from nexus.binance.spot.market_data import get_api_v3_trades
    from nexus.binance.spot.market_data import get_api_v3_historical_trades
    from nexus.binance.spot.market_data import get_api_v3_klines
    from nexus.binance.spot.market_data import get_api_v3_ui_klines
    from nexus.binance.spot.market_data import get_api_v3_avgPrice
    from nexus.binance.spot.market_data import get_api_v3_ticker_24hr
    from nexus.binance.spot.market_data import get_api_v3_ticker_tradingDay
    from nexus.binance.spot.market_data import get_api_v3_ticker_price
    from nexus.binance.spot.market_data import get_api_v3_ticker_bookTicker
    from nexus.binance.spot.market_data import get_api_v3_ticker

    # Trading endpoints
    from nexus.binance.spot.trading import post_api_v3_order
