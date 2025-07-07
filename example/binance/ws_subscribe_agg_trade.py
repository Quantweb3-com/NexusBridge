import asyncio
import cysimdjson
from nexus.binance.um import UmTradingWebsocket
from nexus.utils import Log
import sys
Log.setup_logger(log_level="INFO")

parser = cysimdjson.JSONParser()


# Access using JSON Pointer

import pickle

DATA =[]

def handler(msg):
    try:
        # data = parser.parse(msg)
        # """
        # {'e': 'bookTicker', 'u': 7069332112744, 's': 'BTCUSDT', 'b': '85806.70', 'B': '6.335', 'a': '85806.80', 'A': '10.645', 'T': 1742442709758, 'E': 1742442709758}
        # """
        # # e = data.at_pointer('/e')
        # # s = data.at_pointer('/s')
        # # b = data.at_pointer('/b')
        # # B = data.at_pointer('/B')
        # # a = data.at_pointer('/a')
        # # A = data.at_pointer('/A')
        # # T = data.at_pointer('/T')
        # # E = data.at_pointer('/E')
        # # print(e, s, b, B, a, A, T, E, msg)
        # # print(sys.sizeof(msg))
        # print(msg)
        # print(sys.getsizeof(msg))
        # DATA.append(msg)
        print(msg)
    except Exception as e:
        pass


async def main():
    client = UmTradingWebsocket(handler=handler)
    await client.depth_levels("BTCUSDT", 5)
    await client.connect()
    
    with open("data.pkl", "wb") as f:
        pickle.dump(DATA, f)


if __name__ == "__main__":
    asyncio.run(main())
