from nexus.binance.base import BinanceApiClient


class DerivativesTrading(BinanceApiClient):
    def __init__(self, key=None, secret=None, testnet=False, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://api.binance.com"
        super().__init__(key, secret, testnet=testnet, **kwargs)
