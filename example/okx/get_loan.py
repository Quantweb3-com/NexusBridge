import asyncio
import time
import datetime
from nexus.okx.restapi import OkxApiClient
from nexus.okx.constants import OkxUrl
import pandas as pd


async def get_loan_rate(client: OkxApiClient, ccy: str, limit: int = None, start_time: str = None, end_time: str = None):
    """
    Get the loan rate for a given currency
    """
    end_time_ms = int(end_time) if end_time is not None else int(time.time() * 1000)
    limit = str(limit) if limit is not None else 100
    all_loan_rates = []
    while True:
        loan_rates_response = await client.get_api_v5_finance_savings_lending_rate_history(
            ccy=ccy,
            limit=limit,
            after=end_time,
            before=start_time,
        )
        loan_rates = loan_rates_response["data"]
        all_loan_rates.extend(loan_rates)
        # Update the start_time to fetch the next set of bars
        if loan_rates:
            next_start_time = int(loan_rates[0]["ts"]) + 1
        else:
            # Handle the case when klines is empty
            break
        # No more bars to fetch
        if (limit and len(loan_rates) < limit) or next_start_time >= end_time_ms:
            break
        start_time = next_start_time
    return all_loan_rates






async def main():
    try:
        client = OkxApiClient(
            url=OkxUrl.LIVE,
            max_rate=5.5/1,
        )
        
        res = await client.get_api_v5_finance_savings_lending_rate_history()
        coins = [item["ccy"] for item in res["data"]]
        
        
        
        
        # start_time = int(datetime.datetime(2023, 1, 1, 0, 0).timestamp() * 1000)
        # loan_rates = await get_loan_rate(client, "USDT", start_time=start_time)
        # df = pd.DataFrame(loan_rates)
        # df['timestamp'] = pd.to_datetime(df['ts'].astype(int), unit='ms')
        # df.sort_values(by='timestamp', inplace=True)
        # print(df)
    except Exception as e:
        print(e)
    finally:
        await client.close_session()


if __name__ == "__main__":
    asyncio.run(main())
