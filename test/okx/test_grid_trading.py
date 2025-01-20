import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from nexus.okx.restapi import OkxApiClient


class TestGridTradeApiClient(IsolatedAsyncioTestCase):
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
    async def test_post_api_v5_trading_bot_grid_order_algo(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trading_bot_grid_order_algo(
            "BTC-USDT",
            "grid",
            "5000",
            "400",
            "10",
            [
                {
                    "triggerAction": "start",
                    "triggerStrategy": "rsi",
                    "timeframe": "30m",
                    "thold": "10",
                    "triggerCond": "cross",
                    "timePeriod": "14"
                },
                {
                    "triggerAction": "stop",
                    "triggerStrategy": "price",
                    "triggerPx": "1000",
                    "stopType": "2"
                }
            ],
            quote_sz="25",
            runType="1",
            sz="200",
            direction="long",
            lever="2",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_grid_amend_order_algo(self, mock_post):
        result = await self.client.post_api_v5_trading_bot_grid_amend_order_algo(
            "BTC-USDT-SWAP",
            "448965992920907776",
            [
                {
                    "triggerAction": "stop",
                    "triggerStrategy": "price",
                    "triggerPx": "1000"
                }
            ]
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_grid_stop_order_algo(self, mock_post):
        result = await self.client.post_api_v5_trading_bot_grid_stop_order_algo(
            [
                {
                    "algoId": "448965992920907776",
                    "instId": "BTC-USDT",
                    "stopType": "1",
                    "algoOrdType": "grid"
                }
            ]
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_grid_close_position(self, mock_post):
        result = await self.client.post_api_v5_trading_bot_grid_close_position(
            "448965992920907776",
            True
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_grid_cancel_close_order(self, mock_post):
        result = await self.client.post_api_v5_trading_bot_grid_cancel_close_order(
            "448965992920907776",
            "570627699870375936"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_grid_order_instant_trigger(self, mock_post):
        result = await self.client.post_api_v5_trading_bot_grid_order_instant_trigger(
            "561564133246894080"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_grid_orders_algo_pending(self, mock_get):
        result = await self.client.get_api_v5_trading_bot_grid_orders_algo_pending(
            "grid",
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_grid_orders_algo_history(self, mock_get):
        result = await self.client.get_api_v5_trading_bot_grid_orders_algo_history(
            "grid",
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_grid_orders_algo_details(self, mock_get):
        result = await self.client.get_api_v5_trading_bot_grid_orders_algo_details(
            "448965992920907776",
            "grid"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_grid_sub_orders(self, mock_get):
        result = await self.client.get_api_v5_trading_bot_grid_sub_orders(
            "123456",
            "grid",
            "live",
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_grid_positions(self, mock_get):
        result = await self.client.get_api_v5_trading_bot_grid_positions(
            "448965992920907776",
            "contract_grid"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_trading_bot_grid_withdraw_income(self, mock_get):
        result = await self.client.post_api_v5_trading_bot_grid_withdraw_income(
            "448965992920907776"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_grid_compute_margin_balance(self, mock_post):
        result = await self.client.post_api_v5_trading_bot_grid_compute_margin_balance(
            "448965992920907776",
            "add",
            "10"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_grid_margin_balance(self, mock_post):
        result = await self.client.post_api_v5_trading_bot_grid_margin_balance(
            "123456",
            "add",
            amt="10"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trading_bot_grid_adjust_investment(self, mock_post):
        result = await self.client.post_api_v5_trading_bot_grid_adjust_investment(
            "448965992920907776",
            "12"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_grid_ai_params(self, mock_get):
        result = await self.client.get_api_v5_trading_bot_grid_ai_param(
            "grid",
            "BTC-USDT"
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_trading_bot_grid_min_investment(self, mock_get):
        result = await self.client.post_api_v5_trading_bot_grid_min_investment(
            "ETH-USDT",
            "grid",
            "5000",
            "3000",
            "50",
            "1",
            investment_data=[
                {
                    "amt": "0.01",
                    "ccy": "ETH"
                },
                {
                    "amt": "100",
                    "ccy": "USDT"
                }
            ]
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_rsi_back_testing(self, mock_get):
        result = await self.client.get_api_v5_trading_bot_rsi_back_testing(
            "BTC-USDT",
            "3m",
            "30",
            "14",
        )
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trading_bot_grid_quantity(self, mock_get):
        result = await self.client.get_api_v5_trading_bot_grid_quantity(
            "BTC-USDT-SWAP",
            "1",
            "contract_grid",
            "70000",
            "50000",
            lever="5"
        )
        self.assertIsInstance(result, dict)
        print(result)
