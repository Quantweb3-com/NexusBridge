import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from nexus.okx.restapi import OkxApiClient


class TestSignalBotTradingApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "305c4119-4911-4a22-8a07-2435eeac726a"
        self.api_secret = "221D78AFB68CB539865A11101D603CE7"
        self.passphrase = "@Or2452020438"
        self.client = OkxApiClient(self.api_key, self.api_secret, self.passphrase)
    
    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        await self.client.close_session()

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_signal_create_signal(self, mock_post):
        result = await self.client.signal_bot_trading_api.post_api_v5_trading_bot_signal_create_signal(
            "long short",
            "this is the first version"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_signal_signals(self, mock_get):
        result = await self.client.signal_bot_trading_api.get_api_v5_trading_bot_signal_signals(
            "1"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_signal_order_algo(self, mock_post):
        result = await self.client.signal_bot_trading_api.post_api_v5_trading_bot_signal_order_algo(
            "2106674643045191680",
            "10",
            "100",
            "9",
            instIds=[
                "BTC-USDT-SWAP",
                "ETH-USDT-SWAP",
                "LTC-USDT-SWAP"
            ],
            entrySettingParam={
                "allowMultipleEntry": True,
                "entryType": "1",
                "amt": "",
                "ratio": ""
            },
            exitSettingParam={
                "tpSlType": "2",
                "tpPct": "",
                "slPct": ""
            }
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_signal_stop_order_algo(self, mock_post):
        result = await self.client.signal_bot_trading_api.post_api_v5_trading_bot_signal_stop_order_algo(
            ["2106674643045191680"],
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_signal_margin_balance(self, mock_post):
        result = await self.client.signal_bot_trading_api.post_api_v5_trading_bot_signal_margin_balance(
            "123456",
            "add",
            "10"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_signal_amend_tp_sl(self, mock_post):
        result = await self.client.signal_bot_trading_api.post_api_v5_trading_bot_signal_amend_tp_sl(
            "637039348240277504",
            {
                "tpSlType": "pnl",
                "tpPct": "0.01",
                "slPct": "0.01"
            }
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_signal_set_instruments(self, mock_post):
        result = await self.client.signal_bot_trading_api.post_api_v5_trading_bot_signal_set_instruments(
            "637039348240277504",
            [
                "SHIB-USDT-SWAP",
                "ETH-USDT-SWAP"
            ]
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_signal_orders_algo_details(self, mock_get):
        result = await self.client.signal_bot_trading_api.get_api_v5_trading_bot_signal_orders_algo_details(
            "637039348240277504",
            "contract"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_signal_orders_algo_pending(self, mock_get):
        result = await self.client.signal_bot_trading_api.get_api_v5_trading_bot_signal_orders_algo_pending(

        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_signal_orders_algo_history(self, mock_get):
        result = await self.client.signal_bot_trading_api.get_api_v5_trading_bot_signal_orders_algo_history(
            "637039348240277504"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_signal_positions(self, mock_get):
        result = await self.client.signal_bot_trading_api.get_api_v5_trading_bot_signal_positions(
            "623833708424069120",
            "contract"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_signal_positions_history(self, mock_post):
        result = await self.client.signal_bot_trading_api.get_api_v5_trading_bot_signal_positions_history(
            "1234",
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_signal_close_position(self, mock_post):
        result = await self.client.signal_bot_trading_api.post_api_v5_trading_bot_signal_close_position(
            "448965992920907776",
            "BTC-USDT-SWAP",
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_signal_sub_orders(self, mock_post):
        result = await self.client.signal_bot_trading_api.post_api_v5_trading_bot_signal_sub_order(
            "1222",
            "BTC-USDT-SWAP",
            "buy",
            "limit",
            "2",
            px="2.15"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_signal_cancel_sub_order(self, mock_post):
        result = await self.client.signal_bot_trading_api.post_api_v5_trading_bot_signal_cancel_sub_order(
            "91664",
            "BTC-USDT-SWAP",
            "590908157585625111"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_get_api_v5_trading_bot_signal_sub_orders(self, mock_post):
        result = await self.client.signal_bot_trading_api.get_api_v5_trading_bot_signal_sub_orders(
            "623833708424069120",
            "contract",
            signalOrdId="O632302662327996418"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_signal_event_history(self, mock_get):
        result = await self.client.signal_bot_trading_api.get_api_v5_trading_bot_signal_event_history(
            "623833708424069120",
        )
        self.assertIsInstance(result, dict)
        print(result)
