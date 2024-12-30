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
