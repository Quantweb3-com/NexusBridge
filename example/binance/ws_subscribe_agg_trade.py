import asyncio
import orjson
from nexus.binance.spot import BinanceSpotWSClient

def handler(msg):
    print(orjson.loads(msg))
    
async def main():
   

    client = BinanceSpotWSClient(handler=handler)
    await client.subscribe_trade("BTCUSDT")
    await client.connect()


if __name__ == "__main__":
    asyncio.run(main())
