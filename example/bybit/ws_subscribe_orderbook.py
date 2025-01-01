import asyncio
from nexus.bybit.wsapi import BybitWSClient
from nexus.bybit.constants import BybitAccountType


async def main():
    def handler(msg):
        print(msg)

    client = BybitWSClient(BybitAccountType.LINEAR, handler)
    await client.subscribe_order_book("BTCUSDT", 1)
    await client.connect()


if __name__ == "__main__":
    asyncio.run(main())
