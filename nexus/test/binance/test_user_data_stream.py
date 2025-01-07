import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.binance.constants import BinanceUrl, Interval, Side, OrderType
from nexus.binance.spot import SpotTradingApi


class TestGeneralClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "xRYAmLMJYZlUxmgEo3fAvVyWDFpRtx3YTXoY2bDNs3yvKmv2kt1eCjToKY0dTkJm"
        self.api_secret = "H49uCZ9tM67m8QfkNwzsaDfg05zwstuvbfdlrTGVmn7iE5FEzqj3F5lhPbbFwFcj"
        self.client = SpotTradingApi(self.api_key, self.api_secret, binance_url=BinanceUrl.TEST, )

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v3_user_data_stream(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_api_v3_user_data_stream(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.put')
    async def test_put_api_v3_user_data_stream(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.put_api_v3_user_data_stream(
            listen_key="nhpPloQAxZX4Kr2U4hs7K1DBKHCuIswrs9M4TBu7FZxUgibKQkn2ZfVB8k6m"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.delete')
    async def test_delete_api_v3_user_data_stream(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.delete_api_v3_user_data_stream(
            listen_key="nhpPloQAxZX4Kr2U4hs7K1DBKHCuIswrs9M4TBu7FZxUgibKQkn2ZfVB8k6m"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)
