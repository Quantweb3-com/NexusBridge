import msgspec
from typing import List
from nexus.okx.constants import (
    OkxInstrumentType,
    OkxInstrumentFamily,
    OkxOrderType,
    OkxOrderSide,
    OkxPositionSide,
    OkxTdMode,
    OkxOrderStatus,
)


class OkxWsArgMsg(msgspec.Struct):
    channel: str | None = None
    instType: OkxInstrumentType | None = None
    instFamily: OkxInstrumentFamily | None = None
    instId: str | None = None
    uid: str | None = None


class OkxWsGeneralMsg(msgspec.Struct):
    event: str | None = None
    msg: str | None = None
    code: str | None = None
    connId: str | None = None
    channel: str | None = None
    arg: OkxWsArgMsg | None = None

    @property
    def is_event_msg(self) -> bool:
        return self.event is not None


class OkxWsBboTbtData(msgspec.Struct):
    ts: str
    seqId: int
    asks: list[list[str]]
    bids: list[list[str]]


class OkxWsBboTbtMsg(msgspec.Struct):
    """
    {
        "arg": {
            "channel": "bbo-tbt",
            "instId": "BCH-USDT-SWAP"
        },
        "data": [
            {
            "asks": [
                [
                "111.06","55154","0","2"
                ]
            ],
            "bids": [
                [
                "111.05","57745","0","2"
                ]
            ],
            "ts": "1670324386802",
            "seqId": 363996337
            }
        ]
    }
    """

    arg: OkxWsArgMsg
    data: list[OkxWsBboTbtData]


class OkxWsCandleMsg(msgspec.Struct):
    arg: OkxWsArgMsg
    data: list[list[str]]


class OkxWsTradeData(msgspec.Struct):
    instId: str
    tradeId: str
    px: str
    sz: str
    side: str
    ts: str
    count: str


class OkxWsTradeMsg(msgspec.Struct):
    arg: OkxWsArgMsg
    data: list[OkxWsTradeData]

class OkxWsOrderData(msgspec.Struct):
    instType: OkxInstrumentType
    instId: str
    tgtCcy: str
    ccy: str
    ordId: str
    clOrdId: str
    tag: str
    px: str
    pxUsd: str
    pxVol: str
    pxType: str
    sz: str
    notionalUsd: str
    ordType: OkxOrderType
    side: OkxOrderSide
    posSide: OkxPositionSide
    tdMode: OkxTdMode
    fillPx: str # last fill price
    tradeId: str # last trade id
    fillSz: str  # last filled quantity
    fillPnl: str  # last filled profit and loss
    fillTime: str  # last filled time
    fillFee: str  # last filled fee
    fillFeeCcy: str  # last filled fee currency
    fillPxVol: str  # last filled price volume
    fillPxUsd: str  # last filled price in USD
    fillMarkVol: str  # last filled mark volume
    fillFwdPx: str  # last filled forward price
    fillMarkPx: str  # last filled mark price
    execType: str  # last execution type
    accFillSz: str  # accumulated filled quantity
    fillNotionalUsd: str  # accumulated filled notional in USD
    avgPx: str  # average price
    state: OkxOrderStatus
    lever: str  # leverage
    attachAlgoClOrdId: str  # attached algo order id
    tpTriggerPx: str  # take profit trigger price
    tpTriggerPxType: str  # take profit trigger price type
    tpOrdPx: str  # take profit order price
    slTriggerPx: str  # stop loss trigger price
    slTriggerPxType: str  # stop loss trigger price type
    slOrdPx: str  # stop loss order price
    stpMode: str  # stop loss mode
    feeCcy: str  # fee currency
    fee: str  # fee
    rebateCcy: str  # rebate currency
    rebate: str  # rebate
    pnl: str
    source: str
    cancelSource: str
    amendSource: str
    category: str
    isTpLimit: bool
    uTime: int
    cTime: int
    reqId: str
    amendResult: str
    reduceOnly: bool
    quickMgnType: str
    algoClOrdId: str
    algoId: str
    lastPx: str  # last price
    code: str
    msg: str
    
    
class OkxWsOrderMsg(msgspec.Struct):
    arg: OkxWsArgMsg
    data: List[OkxWsOrderData]


################################################################################
# Place Order: POST /api/v5/trade/order
################################################################################


class OkxPlaceOrderData(msgspec.Struct):
    ordId: str
    clOrdId: str
    tag: str
    ts: str  # milliseconds when OKX finished order request processing
    sCode: str  # event code, "0" means success
    sMsg: str  # rejection or success message of event execution


class OkxPlaceOrderResponse(msgspec.Struct):
    code: str
    msg: str
    data: list[OkxPlaceOrderData]
    inTime: str  # milliseconds when request hit REST gateway
    outTime: str  # milliseconds when response leaves REST gateway


################################################################################
# Cancel order: POST /api/v5/trade/cancel-order
################################################################################


class OkxGeneralResponse(msgspec.Struct):
    code: str
    msg: str


class OkxCancelOrderData(msgspec.Struct):
    ordId: str
    clOrdId: str
    ts: str  # milliseconds when OKX finished order request processing
    sCode: str  # event code, "0" means success
    sMsg: str  # rejection or success message of event execution


class OkxCancelOrderResponse(msgspec.Struct):
    code: str
    msg: str
    data: list[OkxCancelOrderData]
    inTime: str  # milliseconds when request hit REST gateway
    outTime: str  # milliseconds when response leaves REST gateway


class OkxErrorData(msgspec.Struct):
    sCode: str
    sMsg: str

class OkxErrorResponse(msgspec.Struct):
    code: str
    data: list[OkxErrorData]
    msg: str
