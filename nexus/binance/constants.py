from enum import Enum


class BaseUrl:
    def __init__(self, testnet_rest_url: str, main_rest_url: str, main_ws_url: str, testnet_ws_url: str):
        self.testnet_rest_url = testnet_rest_url
        self.main_rest_url = main_rest_url
        self.main_ws_url = main_ws_url
        self.testnet_ws_url = testnet_ws_url

    def get_url(self, url_type: 'BinanceUrl') -> str:
        """根据 BinanceUrl 枚举获取对应的 URL"""
        url_mapping = {
            BinanceUrl.MAIN: self.main_rest_url,
            BinanceUrl.TEST: self.testnet_rest_url,
            BinanceUrl.WS: self.main_ws_url,
            BinanceUrl.TEST_WS: self.testnet_ws_url
        }
        return url_mapping[url_type]


class BinanceUrl(Enum):
    MAIN = 0
    TEST = 1
    WS = 2
    TEST_WS = 3


class BinanceInstrumentType(Enum):
    Derivatives_UM = "Derivatives_UM"
    Derivatives_CM = "Derivatives_CM"
    SPOT = "SPOT"


ALL_URL = {
    BinanceInstrumentType.Derivatives_UM: BaseUrl(
        testnet_rest_url="https://testnet.binancefuture.com",
        testnet_ws_url="wss://testnet.binancefuture.com/ws-fapi/v1",
        main_rest_url="https://fapi.binance.com",
        main_ws_url="wss://ws-fapi.binance.com/ws-fapi/v1",
    ),
    BinanceInstrumentType.Derivatives_CM: BaseUrl(
        testnet_rest_url="https://testnet.binancefuture.com",
        testnet_ws_url="wss://dstream.binancefuture.com",
        main_rest_url="https://dapi.binance.com",
        main_ws_url="wss://dstream.binance.com",
    ),
    BinanceInstrumentType.SPOT: BaseUrl(
        testnet_rest_url="https://testnet.binance.vision/api",
        testnet_ws_url="wss://testnet.binance.vision/ws-api/v3",
        main_rest_url="https://api.binance.com",
        main_ws_url="wss://ws-api.binance.com:443/ws-api/v3",
    )
}


class Interval(Enum):
    MINUTE_1 = "1m"
    MINUTE_3 = "3m"
    MINUTE_5 = "5m"
    MINUTE_15 = "15m"
    MINUTE_30 = "30m"
    HOUR_1 = "1h"
    HOUR_2 = "2h"
    HOUR_4 = "4h"
    HOUR_6 = "6h"
    HOUR_8 = "8h"
    HOUR_12 = "12h"
    DAY_1 = "1d"
    DAY_3 = "3d"
    WEEK_1 = "1w"
    MONTH_1 = "1M"


class Side(Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"
    STOP_LOSS = "STOP_LOSS"
    STOP_LOSS_LIMIT = "STOP_LOSS_LIMIT"
    TAKE_PROFIT = "TAKE_PROFIT"
    TAKE_PROFIT_LIMIT = "TAKE_PROFIT_LIMIT"
    LIMIT_MAKER = "LIMIT_MAKER"