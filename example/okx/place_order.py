import asyncio
from nexus.okx.restapi import OkxApiClient
from nexus.okx.constants import OkxUrl
from nexus.config import settings

API_KEY = settings.OKX.DEMO.api_key
PASSPHRASE = settings.OKX.DEMO.passphrase
SECRET = settings.OKX.DEMO.secret


async def main():
    try:
        client = OkxApiClient(
            api_key=API_KEY,
            secret=SECRET,
            passphrase=PASSPHRASE,
            url=OkxUrl.DEMO,
        )
        response = await client.trade_api.post_api_v5_trade_order(
            inst_id="BTC-USDT-SWAP",
            td_mode="cross",
            side="sell",
            ord_type="market",
            sz="1",
        )
        print(response)
    except Exception as e:
        print(e)
    finally:
        await client.close_session()
    

if __name__ == "__main__":
    asyncio.run(main())
