import asyncio
import orjson
from nexus.binance.um import UmTradingWebsocket
from nexus.binance.spot import BinanceSpotWSClient
from nexus.utils import Log

Log.setup_logger(log_level="INFO")


def handler(msg):
    try:
        data = orjson.loads(msg)
        # if data['k']['x']:
        print(data)
    except Exception as e:
        pass


async def main():
    client = UmTradingWebsocket(handler=handler)
    await client.kline("BTCUSDT", "1m")
    await client.connect()


if __name__ == "__main__":
    asyncio.run(main())
