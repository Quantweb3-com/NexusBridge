import asyncio
from nexus.binance.margin import MarginTradingApi
from nexus.utils import Log
import pandas as pd

Log.setup_logger(log_level="DEBUG")


async def main():
    try:
        api = MarginTradingApi(
            key="GHt8AYIuHW6AjPLFzCsyK49yVko25Yjs6EvIXJENbC7s43dyU5NVYVau78rhaCI7",
            secret="GBea3WRwj9IsbXL5iOwiRvl1jcmQ00hdEcc1rlYNZid5BfVE3nHLPF5VnK32USXg",
        )
        res = await api.get_sapi_v1_simpleEarn_flexible_list(size=100)
        df = pd.DataFrame(res['rows'])
        print(df)
        
        res = await api.get_sapi_v1_simpleEarn_flexible_history_rateHistory(productId="SOLV001")
        print(res)
    finally:
        await api.close_session()

if __name__ == "__main__":
    asyncio.run(main())
