# NexusBridge

![License](https://img.shields.io/badge/license-MIT-blue.svg)![Python](https://img.shields.io/badge/python-3.10%2B-blue)![Version](https://img.shields.io/badge/version-1.0.0-blue)
<img width="944" alt="nexus_bridge" src="https://github.com/user-attachments/assets/41d53b57-cc94-4946-a589-a0057f59bd65" />
- **Support**: [quantweb3.ai@gmail.com](mailto:quantweb3.ai@gmail.com)


## Introduction

NexusBridge is a professional-grade development toolthat provides **deep optimization** for **exchange API and WebSocket
interfaces**, offering **high-performance**, **highly stable SDK encapsulation**, making it an **ideal choice for
real-world trading**.

## Overview

### Core Advantages

1. **Professional Performance Optimization：** Comprehensive optimization of major exchanges' underlying API and
   WebSocket interfaces, delivering performance and stability significantly superior to official exchange SDKs, meeting
   demanding real-world requirements.
2. **Lightweight Encapsulation Strategy：** Following minimal encapsulation principles to avoid complexity issues from
   over-encapsulation. The system stably supports simultaneous WebSocket subscription for hundreds of trading pairs,
   providing efficient and stable order data streaming.
3. **Precise Debugging Support：** Preserves complete error messages returned by exchanges, enabling users to quickly
   locate and resolve issues, significantly improving development efficiency.

### Why NexusBridge Is More Efficient?

- **Efficient Data Processing**: Utilizing [orjson](https://github.com/ijl/orjson) for JSON serialization and
  deserialization, NexusBridge achieves unmatched efficiency, being 10 times faster than the standard json library while
  maintaining a lower memory footprint.

- **High-Performance WebSocket Framework**: Built with [picows](https://github.com/tarasko/picows), a Cython-based
  WebSocket library that matches the speed of C++'s Boost.Beast, significantly outperforming Python alternatives like
  websockets and aiohttp.

- **Smart Memory Management**: Employing object pool technology for object reuse, NexusBridge reduces garbage collection
  pressure and minimizes memory fragmentation, ensuring efficient resource utilization.

- **Advanced Concurrency Control**: Orders are managed efficiently using `asyncio.Queue`, with intelligent rate limiting
  and an optimized task scheduler to handle high volumes seamlessly.

- **Modular Architecture**: NexusBridge's flexible framework allows for easy integration of new exchanges, instruments,
  or custom strategies, ensuring scalability and adaptability to changing market conditions.

### Features

- 🌐 Multi-Exchange Support: Seamlessly integrate with Binance, OKX, and Bybit through a unified API interface, with
  extensible architecture for more exchanges.

- ⚡ Real-Time Processing: High-performance WebSocket implementation supporting 1000+ simultaneous trading pair
  subscriptions with minimal latency.

- 📊 Market Data Streaming: Efficient handling of orderbook updates, trades, and klines using optimized data structures
  and memory management.

- 💼 Advanced Trading: Complete order management system supporting various order types, position tracking, and risk
  control mechanisms.

- 🛡️ Reliability Focus: Comprehensive error handling, detailed logging, and production-validated stability for
  mission-critical operations.

- 🔄 Smart Concurrency: Intelligent rate limiting and request batching to optimize API usage while maintaining high
  throughput.

- 📈 Scalable Architecture: Modular design supporting easy integration of new features and custom trading strategies.

- 🔍 Debug Friendly: Preserves complete exchange error messages and provides detailed tracking for efficient
  troubleshooting.

- 🧪 Quality Assured: Extensive unit test coverage and production environment validation for enterprise-grade
  reliability.

### Supported Exchanges

| OKX                                                                                  | **Binance**                                                                    | BYBIT                                                                                                                     |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| <img src="https://www.okx.com/cdn/assets/imgs/226/EB771F0EE8994DD5.png" width="100"> | <img src="https://cryptologos.cc/logos/binance-coin-bnb-logo.png" width="100"> | <img src="https://raw.githubusercontent.com/bybit-web3/bybit-web3.github.io/main/docs/images/bybit-logo.png" width="100"> |

## Getting Started

### Installation (From PyPI)

We recommend using the latest supported version of Python and setting
up [nexus](https://pypi.org/project/nexus/) in a virtual environment to isolate dependencies

To install the latest binary wheel (or sdist package) from PyPI using Pythons pip package manager:

    pip install -U nexusbridge

### Jupiter Python SDK Usage

```py
import base58
import base64
import json

from solders import message
from solders.pubkey import Pubkey
from solders.keypair import Keypair
from solders.transaction import VersionedTransaction

from solana.rpc.types import TxOpts
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Processed

from jupiter_python_sdk.jupiter import Jupiter, Jupiter_DCA


private_key = Keypair.from_bytes(base58.b58decode(os.getenv("PRIVATE-KEY"))) # Replace PRIVATE-KEY with your private key as string
async_client = AsyncClient("SOLANA-RPC-ENDPOINT-URL") # Replace SOLANA-RPC-ENDPOINT-URL with your Solana RPC Endpoint URL
jupiter = Jupiter(
    async_client=async_client,
    keypair=private_key,
    quote_api_url="https://quote-api.jup.ag/v6/quote?",
    swap_api_url="https://quote-api.jup.ag/v6/swap",
    open_order_api_url="https://jup.ag/api/limit/v1/createOrder",
    cancel_orders_api_url="https://jup.ag/api/limit/v1/cancelOrders",
    query_open_orders_api_url="https://jup.ag/api/limit/v1/openOrders?wallet=",
    query_order_history_api_url="https://jup.ag/api/limit/v1/orderHistory",
    query_trade_history_api_url="https://jup.ag/api/limit/v1/tradeHistory"
)


"""
EXECUTE A SWAP
"""
transaction_data = await jupiter.swap(
    input_mint="So11111111111111111111111111111111111111112",
    output_mint="EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
    amount=5_000_000,
    slippage_bps=1,
)
# Returns str: serialized transactions to execute the swap.

raw_transaction = VersionedTransaction.from_bytes(base64.b64decode(transaction_data))
signature = private_key.sign_message(message.to_bytes_versioned(raw_transaction.message))
signed_txn = VersionedTransaction.populate(raw_transaction.message, [signature])
opts = TxOpts(skip_preflight=False, preflight_commitment=Processed)
result = await async_client.send_raw_transaction(txn=bytes(signed_txn), opts=opts)
transaction_id = json.loads(result.to_json())['result']
print(f"Transaction sent: https://explorer.solana.com/tx/{transaction_id}")


"""
OPEN LIMIT ORDER
"""
transaction_data = await jupiter.open_order(
    input_mint=So11111111111111111111111111111111111111112",
    output_mint=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
    in_amount=5_000_000,
    out_amount=100_000,
)
# Returns dict: {'transaction_data': serialized transactions to create the limit order, 'signature2': signature of the account that will be opened}

raw_transaction = VersionedTransaction.from_bytes(base64.b64decode(transaction_data['transaction_data']))
signature = private_key.sign_message(message.to_bytes_versioned(raw_transaction.message))
signed_txn = VersionedTransaction.populate(raw_transaction.message, [signature, transaction_data['signature2']])
opts = TxOpts(skip_preflight=False, preflight_commitment=Processed)
result = await async_client.send_raw_transaction(txn=bytes(signed_txn), opts=opts)
transaction_id = json.loads(result.to_json())['result']
print(f"Transaction sent: https://explorer.solana.com/tx/{transaction_id}")


"""
CREATE DCA ACCOUNT
"""
create_dca_account = await jupiter.dca.create_dca(
    input_mint=Pubkey.from_string("So11111111111111111111111111111111111111112"),
    output_mint=Pubkey.from_string("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"),
    total_in_amount=5_000_000,
    in_amount_per_cycle=100_000,
    cycle_frequency=60,
    min_out_amount_per_cycle=0,
    max_out_amount_per_cycle=0,
    start=0
)
# Returns DCA Account Pubkey and transaction hash.


"""
CLOSE DCA ACCOUNT
"""
close_dca_account = await jupiter.dca.close_dca(
    dca_pubkey=Pubkey.from_string("45iYdjmFUHSJCQHnNpWNFF9AjvzRcsQUP9FDBvJCiNS1")
)
# Returns transaction hash.
```

### Available Jupiter SDK Methods
```py
- quote
- swap
- open_order
- cancel_orders
- create_dca
- close_dca
- fetch_user_dca_accounts
- fetch_dca_account_fills_history
- get_available_dca_tokens
- fetch_dca_data
- query_open_orders
- query_orders_history
- query_trades_history
- get_jupiter_stats
- get_token_price
- get_indexed_route_map
- get_tokens_list
- get_all_tickers
- get_all_swap_pairs
- get_swap_pairs
- get_token_stats_by_date
- program_id_to_label
```

### Quick Start

This is a basic example of how to use nexus, demonstrating how to submit an order using the OKX API。

```python
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
        response = await client.post_api_v5_trade_order(
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

```

Submit orders using OKX websocket

```python
import asyncio
from nexus.okx.restapi import OkxApiClient
from nexus.okx.constants import OkxUrl, OkxAccountType, ChannelKind
from nexus.config import settings
from nexus.okx.wsapi import OkxWSClient


async def main():
    try:
        def handler(msg):
            print(msg)

        client = OkxWSClient(
            OkxAccountType.DEMO,
            handler,
            secret="",
            api_key="",
            passphrase="",
            channel_kind=ChannelKind.PUBLIC,
        )
        await client.private_place_order(
            "BTC-USDT",
            "isolated",
            "buy",
            "market",
            "1",
        )
        await client.connect()
    except Exception as e:
        print(e)
    finally:
        await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

```

#### Function Names and API Endpoint Mapping

Below are some commonly used function names and their corresponding API endpoints and methods:

##### OKX

- **Function Name:** `post_api_v5_trade_order`
- **Corresponding API:** `POST /api/v5/trade/order`
- **Example:**

  ```python
  order_response = okx_client.post_api_v5_trade_order({
      'symbol': 'BTCUSD',
      'side': 'Buy',
      'order_type': 'Limit',
      'qty': 0.01,
      'price': 30000
  })
  print(order_response)

API parameters may vary between exchanges. Refer to their official documentation for detailed information.

## Contributing

Thank you for considering contributing to nexus! We greatly appreciate any effort to help improve the project. If
you have an idea for an enhancement or a bug fix, the first step is to open
an [issue](https://github.com/Quantweb3-ai/nexus/issues) on GitHub. This allows us to discuss your proposal and
ensure it aligns with the project's goals, while also helping to avoid duplicate efforts.

When you're ready to start working on your contribution, please review the guidelines in
the [CONTRIBUTING.md](CONTRIBUTING.md) file. Depending on the nature of your contribution, you may also need to sign a
Contributor License Agreement (CLA) to ensure it can be included in the project.

> **Note**
> Pull requests should be directed to the `main` branch (the default branch), where new features and improvements are
> integrated before release.

Thank you again for your interest in nexus! We look forward to reviewing your contributions and collaborating with
you to make the project even better.

## VIP Privileges

Trading on our platform is free. Become a VIP customer to enjoy exclusive technical support privileges for $499 per
month ([Subscription Here](https://quantweb3.ai/subscribe/ ))—or get VIP status at no cost by opening an account through
our partnership links.

Our partners include global leading trading platforms like Bybit, OKX, ZFX, Bison and others. By opening an account
through our referral links, you'll enjoy these benefits:

Instant Account Benefits

1. Trading Fee Discounts: Exclusive discounts to lower your trading costs.
2. VIP Service Support: Contact us after opening your account to become our VIP customer. Enjoy exclusive events and
   benefits for the ultimate VIP experience.

Act now and join our VIP program!

> Click the links below to register

- [Bybit](https://partner.bybit.com/b/90899)
- [OKX](http://www.okx.com/join/80353297)
- [ZFX](https://zfx.link/46dFByp)
- [Bison](https://m.bison.com/#/register?invitationCode=1002)

## Social

Connect with us on your favorite platforms:

[![X (Twitter)](https://img.shields.io/badge/X_(Twitter)-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/quantweb3_ai)
Stay updated with our latest news, features, and announcements.

[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/BR8VGRrXFr)
Join our community to discuss ideas, get support, and connect with other users.

[![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/+6e2MtXxoibM2Yzlk)
Receive instant updates and engage in real-time discussions.

## See Also

We recommend exploring related tools and projects that can enhance your trading workflows:

- [NexusTrader](https://github.com/RiverTrading/NexusTrader): The Most Professional Open-Source Quantitative Trading
  Platform for Large-Scale Capital

## License

NexusBridge is available on GitHub under the MIT License. Contributions to the project are welcome and require the
completion of a Contributor License Agreement (CLA). Please review the contribution guidelines and submit a pull
request. See the [LICENSE](LICENSE) file for details.
