from enum import Enum



class OkxUrl(Enum):
    LIVE = 0
    AWS = 1
    DEMO = 2
    
    @property
    def base_url(self):
        return STREAM_URLS[self]
    
    @property
    def is_testnet(self):
        return self == OkxUrl.DEMO


STREAM_URLS = {
    OkxUrl.LIVE: "wss://ws.okx.com:8443/ws",
    OkxUrl.AWS: "wss://wsaws.okx.com:8443/ws",
    OkxUrl.DEMO: "wss://wspap.okx.com:8443/ws",
}
