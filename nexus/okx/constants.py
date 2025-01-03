from enum import Enum, unique


class OkxUrl(Enum):
    LIVE = 0
    AWS = 1
    DEMO = 2

    @property
    def base_url(self):
        return REST_URLS[self]

    @property
    def is_testnet(self):
        return self == OkxUrl.DEMO


REST_URLS = {
    OkxUrl.LIVE: "https://www.okx.com",
    OkxUrl.AWS: "https://aws.okx.com",
    OkxUrl.DEMO: "https://www.okx.com",
}


class OkxInstrumentType(Enum):
    SPOT = "SPOT"
    MARGIN = "MARGIN"
    SWAP = "SWAP"
    FUTURES = "FUTURES"
    OPTION = "OPTION"
    ANY = "ANY"


class OkxInstrumentFamily(Enum):
    FUTURES = "FUTURES"
    SWAP = "SWAP"
    OPTION = "OPTION"


@unique
class OkxTdMode(Enum):
    CASH = "cash"  # 现货
    CROSS = "cross"  # 全仓
    ISOLATED = "isolated"  # 逐仓
    SPOT_ISOLATED = "spot_isolated"  # 现货逐仓


@unique
class OkxPositionSide(Enum):
    LONG = "long"
    SHORT = "short"
    NET = "net"
    NONE = ""


@unique
class OkxOrderSide(Enum):
    BUY = "buy"
    SELL = "sell"


class OkxTimeInForce(Enum):
    IOC = "ioc"
    GTC = "gtc"
    FOK = "fok"


@unique
class OkxOrderType(Enum):
    MARKET = "market"
    LIMIT = "limit"
    POST_ONLY = "post_only"  # limit only, requires "px" to be provided
    FOK = "fok"  # market order if "px" is not provided, otherwise limit order
    IOC = "ioc"  # market order if "px" is not provided, otherwise limit order
    OPTIMAL_LIMIT_IOC = (
        "optimal_limit_ioc"  # Market order with immediate-or-cancel order
    )
    MMP = "mmp"  # Market Maker Protection (only applicable to Option in Portfolio Margin mode)
    MMP_AND_POST_ONLY = "mmp_and_post_only"  # Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode)


@unique
class OkxOrderStatus(Enum):  # "state"
    CANCELED = "canceled"
    LIVE = "live"
    PARTIALLY_FILLED = "partially_filled"
    FILLED = "filled"
    MMP_CANCELED = "mmp_canceled"


class OkxAccountType(Enum):
    LIVE = 0
    AWS = 1
    DEMO = 2

    @property
    def exchange_id(self):
        return "okx"

    @property
    def is_testnet(self):
        return self == OkxAccountType.DEMO

    @property
    def stream_url(self):
        return STREAM_URLS[self]


class ChannelKind(Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    BUSINESS = "business"


STREAM_URLS = {
    OkxAccountType.LIVE: "wss://ws.okx.com:8443/ws",
    OkxAccountType.AWS: "wss://wsaws.okx.com:8443/ws",
    OkxAccountType.DEMO: "wss://wspap.okx.com:8443/ws",
}
