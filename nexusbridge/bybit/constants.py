from enum import Enum


class BybitUrl(Enum):
    MAINNET_1 = "MAINNET_1"
    MAINNET_2 = "MAINNET_2"
    TESTNET = "TESTNET"
    NETHERLAND = "NETHERLAND"
    HONGKONG = "HONGKONG"
    TURKEY = "TURKEY"
    HAZAKHSTAN = "HAZAKHSTAN"

    @property
    def base_url(self):
        return BASE_URLS[self]

    @property
    def is_testnet(self):
        return self == BybitUrl.TESTNET


BASE_URLS = {
    BybitUrl.MAINNET_1: "https://api.bybit.com",
    BybitUrl.MAINNET_2: "https://api.bytick.com",
    BybitUrl.TESTNET: "https://api-testnet.bybit.com",
    BybitUrl.NETHERLAND: "https://api.bybit.nl",
    BybitUrl.HONGKONG: "https://api.byhkbit.com",
    BybitUrl.TURKEY: "https://api.bybit-tr.com",
    BybitUrl.HAZAKHSTAN: "https://api.bybit.kz",
}


class BybitAccountType(Enum):
    SPOT = "SPOT"
    LINEAR = "LINEAR"
    INVERSE = "INVERSE"
    OPTION = "OPTION"
    SPOT_TESTNET = "SPOT_TESTNET"
    LINEAR_TESTNET = "LINEAR_TESTNET"
    INVERSE_TESTNET = "INVERSE_TESTNET"
    OPTION_TESTNET = "OPTION_TESTNET"
    UNIFIED = "UNIFIED"
    UNIFIED_TESTNET = "UNIFIED_TESTNET"

    @property
    def exchange_id(self):
        return "bybit"

    @property
    def is_testnet(self):
        return self in {
            self.SPOT_TESTNET,
            self.LINEAR_TESTNET,
            self.INVERSE_TESTNET,
            self.OPTION_TESTNET,
            self.UNIFIED_TESTNET,
        }

    @property
    def ws_public_url(self):
        return WS_PUBLIC_URL[self]

    @property
    def ws_private_url(self):
        if self.is_testnet:
            return "wss://stream-testnet.bybit.com/v5/private"
        return "wss://stream.bybit.com/v5/private"

    @property
    def is_spot(self):
        return self in {self.SPOT, self.SPOT_TESTNET}

    @property
    def is_linear(self):
        return self in {self.LINEAR, self.LINEAR_TESTNET}

    @property
    def is_inverse(self):
        return self in {self.INVERSE, self.INVERSE_TESTNET}


WS_PUBLIC_URL = {
    BybitAccountType.SPOT: "wss://stream.bybit.com/v5/public/spot",
    BybitAccountType.LINEAR: "wss://stream.bybit.com/v5/public/linear",
    BybitAccountType.INVERSE: "wss://stream.bybit.com/v5/public/inverse",
    BybitAccountType.OPTION: "wss://stream.bybit.com/v5/public/option",
    BybitAccountType.SPOT_TESTNET: "wss://stream-testnet.bybit.com/v5/public/spot",
    BybitAccountType.LINEAR_TESTNET: "wss://stream-testnet.bybit.com/v5/public/linear",
    BybitAccountType.INVERSE_TESTNET: "wss://stream-testnet.bybit.com/v5/public/inverse",
    BybitAccountType.OPTION_TESTNET: "wss://stream-testnet.bybit.com/v5/public/option",
}
