from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from nexus.okx.restapi import OkxApiClient


class TestRecurringBuyApiClient(IsolatedAsyncioTestCase):
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
    async def test_post_api_v5_trading_bot_recurring_order_algo(self, mock_post):
        result = await self.client.recurring_buy_api.post_api_v5_trading_bot_recurring_order_algo(
            "BTC|ETH recurring buy monthly",
            [
                {
                    "ccy": "BTC",
                    "ratio": "0.2"
                },
                {
                    "ccy": "ETH",
                    "ratio": "0.8"
                }
            ],
            "monthly",
            "0",
            "8",
            "100",
            "USDT",
            "cross",
            recurringDay="1"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_recurring_amend_order_algo(self, mock_post):
        result = await self.client.recurring_buy_api.post_api_v5_trading_bot_recurring_amend_order_algo(
            "448965992920907776",
            "stg1"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_recurring_stop_order_algo(self, mock_post):
        result = await self.client.recurring_buy_api.post_api_v5_trading_bot_recurring_stop_order_algo(
            ["448965992920907776"]
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_recurring_orders_algo_pending(self, mock_post):
        result = await self.client.recurring_buy_api.get_api_v5_trading_bot_recurring_orders_algo_pending()
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_recurring_orders_algo_history(self, mock_post):
        result = await self.client.recurring_buy_api.get_api_v5_trading_bot_recurring_orders_algo_history()
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_recurring_orders_algo_details(self, mock_post):
        result = await self.client.recurring_buy_api.get_api_v5_trading_bot_recurring_orders_algo_details(
            "448965992920907776")
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_recurring_sub_orders(self, mock_post):
        result = await self.client.recurring_buy_api.get_api_v5_trading_bot_recurring_sub_orders(
            "560516615079727104")
        self.assertIsInstance(result, dict)
        print(result)
