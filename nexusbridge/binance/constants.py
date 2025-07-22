from enum import Enum


class BaseUrl:
    def __init__(
        self,
        testnet_rest_url: str | None,
        main_rest_url: str,
        main_ws_url: str | None,
        testnet_ws_url: str | None,
        main_ws_stream_url: str | None = None,
    ):
        self.testnet_rest_url = testnet_rest_url
        self.main_rest_url = main_rest_url
        self.main_ws_url = main_ws_url
        self.testnet_ws_url = testnet_ws_url
        self.main_ws_stream_url = main_ws_stream_url

    def get_url(self, url_type: "BinanceUrl") -> str:
        """根据 BinanceUrl 枚举获取对应的 URL"""
        if self.main_ws_stream_url is None and url_type == BinanceUrl.WS_STREAM:
            raise ValueError("main_ws_stream_url is not set")

        url_mapping = {
            BinanceUrl.MAIN: self.main_rest_url,
            BinanceUrl.TEST: self.testnet_rest_url,
            BinanceUrl.WS: self.main_ws_url,
            BinanceUrl.TEST_WS: self.testnet_ws_url,
            BinanceUrl.WS_STREAM: self.main_ws_stream_url,
        }
        return url_mapping[url_type]


class BinanceUrl(Enum):
    MAIN = 0
    TEST = 1
    WS = 2
    TEST_WS = 3
    WS_STREAM = 4


class KeyType(Enum):
    HMAC = 0  # "HMAC-SHA-256"
    RSA = 1  # "RSA"
    Ed = 2  # "Ed25519"


class BinanceInstrumentType(Enum):
    Derivatives_PM = "Derivatives_PM"
    Derivatives_UM = "Derivatives_UM"
    Derivatives_CM = "Derivatives_CM"
    SPOT = "SPOT"
    MARGIN = "MARGIN"


ALL_URL = {
    BinanceInstrumentType.Derivatives_UM: BaseUrl(
        testnet_rest_url="https://testnet.binancefuture.com",
        testnet_ws_url="wss://testnet.binancefuture.com/ws-fapi/v1",
        main_rest_url="https://fapi.binance.com",
        main_ws_url="wss://ws-fapi.binance.com/ws-fapi/v1",
        main_ws_stream_url="wss://fstream.binance.com/ws",
    ),
    BinanceInstrumentType.Derivatives_CM: BaseUrl(
        testnet_rest_url="https://testnet.binancefuture.com/ws",
        testnet_ws_url="wss://dstream.binancefuture.com/ws",
        main_rest_url="https://dapi.binance.com",
        main_ws_url="wss://ws-dapi.binance.com/ws-dapi/v1",
        main_ws_stream_url="wss://dstream.binance.com/ws",
    ),
    BinanceInstrumentType.SPOT: BaseUrl(
        testnet_rest_url="https://testnet.binance.vision/api",
        testnet_ws_url="wss://testnet.binance.vision/ws-api/v3",
        main_rest_url="https://api.binance.com",
        main_ws_url="wss://ws-api.binance.com:9443/ws-api/v3",
        main_ws_stream_url="wss://stream.binance.com:9443/ws",
    ),
    BinanceInstrumentType.Derivatives_PM: BaseUrl(
        testnet_rest_url=None,
        testnet_ws_url=None,
        main_rest_url="https://papi.binance.com",
        main_ws_url="wss://fstream.binance.com/pm",
    ),
    BinanceInstrumentType.MARGIN: BaseUrl(
        testnet_rest_url=None,
        testnet_ws_url=None,
        main_rest_url="https://api.binance.com",
        main_ws_url="wss://ws-api.binance.com:9443/ws-api/v3",
        main_ws_stream_url="wss://stream.binance.com:9443/ws",
    ),
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


class ContractType(Enum):
    PERPETUAL = "PERPETUAL"
    CURRENT_QUARTER = "CURRENT_QUARTER"
    NEXT_QUARTER = "NEXT_QUARTER"
    ALL = "ALL"
