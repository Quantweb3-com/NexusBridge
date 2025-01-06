import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.binance.constants import BinanceUrl, Interval, Side, OrderType
from nexus.binance.spot import SpotTradingApi


class TestGeneralClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "Z6EAzmd1YBLqQAgB7z"
        self.api_secret = "R2EshsY4AJ0eQUy8HotalYzi3dyCcYmN9yLW"
        self.client = SpotTradingApi(self.api_key, self.api_secret, binance_url=BinanceUrl.TEST, )

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_depth(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_depth(
            symbol="BNBBTC"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v3_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_api_v3_order(
            symbol="BNBBTC",
            side=Side.BUY,
            _type=OrderType.MARKET,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)
