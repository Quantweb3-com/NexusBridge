import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.binance.constants import BinanceUrl
from nexus.binance.spot import SpotTradingApi


class TestGeneralClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "xRYAmLMJYZlUxmgEo3fAvVyWDFpRtx3YTXoY2bDNs3yvKmv2kt1eCjToKY0dTkJm"
        self.api_secret = "H49uCZ9tM67m8QfkNwzsaDfg05zwstuvbfdlrTGVmn7iE5FEzqj3F5lhPbbFwFcj"
        self.client = SpotTradingApi(self.api_key, self.api_secret, binance_url=BinanceUrl.TEST, )

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_account(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_account()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_my_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_my_trades(
            "BNBBTC"
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_rateLimit_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_rate_limit_order()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_my_prevented_matches(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_my_prevented_matches(
            symbol="BTCUSDT",
            orderId=5862574
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_my_allocations(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_my_allocations(
            symbol="BTCUSDT",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_account_commission(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_account_commission(
            symbol="BTCUSDT",
        )
        print(result)
