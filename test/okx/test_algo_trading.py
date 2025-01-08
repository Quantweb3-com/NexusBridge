import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.okx.restapi import OkxApiClient


class TestAlgoTradingApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "305c4119-4911-4a22-8a07-2435eeac726a"
        self.api_secret = "221D78AFB68CB539865A11101D603CE7"
        self.passphrase = "@Or2452020438"
        self.client = OkxApiClient(self.api_key, self.api_secret, self.passphrase)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_order_precheck(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_order_algo(
            "BTC-USDT",
            "cross",
            "buy",
            "conditional",
            sz="2",
            tpTriggerPx="15",
            tpOrdPx="18"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_cancel_algos(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_cancel_algos(
            [
                {
                    "algoId": "590919993110396111",
                    "instId": "BTC-USDT"
                },
                {
                    "algoId": "590920138287841222",
                    "instId": "BTC-USDT"
                }
            ]
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_amend_algos(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_amend_algos(
            algo_id="2510789768709120",
            newSz="2",
            instId="BTC-USDT"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_cancel_advance_algos(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_cancel_advance_algos(
            [
                {
                    "algoId": "590920768125665111",
                    "instId": "BTC-USDT"
                },
                {
                    "algoId": "590920799650058222",
                    "instId": "BTC-USDT"
                }
            ]
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trade_order_algo(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_trade_order_algo(
            algo_id="1753184812254216192"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trade_orders_algo_pending(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_trade_orders_algo_pending(
            "conditional"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trade_orders_algo_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_trade_orders_algo_history(
            "conditional",
            state="effective"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)
