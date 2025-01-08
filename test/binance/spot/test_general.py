import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.binance.constants import BinanceUrl
from nexus.binance.spot import SpotTradingApi


class TestGeneralClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "Z6EAzmd1YBLqQAgB7z"
        self.api_secret = "R2EshsY4AJ0eQUy8HotalYzi3dyCcYmN9yLW"
        self.client = SpotTradingApi(self.api_key, self.api_secret, binance_url=BinanceUrl.TEST, )
    
    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        await self.client.close_session()

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_ping(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_ping()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_time(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_time()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_exchangeInfo(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_exchangeInfo(
            symbol="BNBBTC"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)
