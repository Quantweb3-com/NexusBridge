from nexus.binance.um import UmTradingApi, UmTradingWebsocket
from nexus.binance.constants import Interval
from nexus.utils import Log
import asyncio
import pandas as pd
import datetime
import orjson
Log.setup_logger(log_path="logs", log_level="INFO")


async def get_symbol_klines(api: UmTradingApi, symbol: str, interval: Interval, startTime: int):
    res = await api.get_fapi_v1_klines(symbol=symbol, interval=interval, startTime=startTime)
    df = pd.DataFrame(res, columns=["timestamp", "open", "high", "low", "close", "volume", "close_time", "quote_volume", "count", "taker_buy_volume", "taker_buy_quote_volume", "ignore"])
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
    df['symbol'] = symbol
    return df

async def get_symbols_klines(api: UmTradingApi, symbols: list[str], interval: Interval, startTime: int):
    tasks = [get_symbol_klines(api, symbol, interval, startTime) for symbol in symbols]
    res = await asyncio.gather(*tasks)
    return pd.concat(res)


def handler(msg):
    try:
        data = orjson.loads(msg)
        if data['k']['x']:
            print(data)
    except Exception as e:
        pass


async def main():
    try:
        api = UmTradingApi()
        ws = UmTradingWebsocket(handler=handler)
        
        info = await api.get_fapi_v1_exchangeInfo()
        symbols = [symbol['symbol'] for symbol in info['symbols'] if symbol['quoteAsset'] == 'USDT']
        
        for symbol in symbols[:1]:
            await ws.kline(symbol, interval='1h')
        await ws.connect()
        
        
        
        
        
    finally:
        await api.close_session()


if __name__ == "__main__":
    asyncio.run(main())
