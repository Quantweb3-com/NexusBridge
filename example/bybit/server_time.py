from nexus.bybit.restapi import BybitApiClient
import asyncio

async def main():
    try:
        client = BybitApiClient()
        time = await client.get_v5_market_time()
        
        print(time)
    except Exception as e:
        print(e)
    finally:
        await client.close_session()


if __name__ == "__main__":
    asyncio.run(main())
    


