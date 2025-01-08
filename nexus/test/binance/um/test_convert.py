import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.binance.constants import BinanceUrl, Interval, ContractType, Side, OrderType
from nexus.binance.spot import SpotTradingApi
from nexus.binance.um import UmTradingApi


class TestGeneralClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "ff61d44910aa178996c40382d77e2bb10996b4dc7df5a2a9c6e431944b500b48"
        self.api_secret = "4e93d727d6a5240e4986c997b7ec3d60a231143fa0c9c8cf4399c42ab22cfb24"
        self.client = UmTradingApi(self.api_key, self.api_secret, binance_url=BinanceUrl.TEST, )

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_convert_exchange_info(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_convert_exchange_info(from_asset="BTC", to_asset="USDT")
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_fapi_v1_convert_get_quote(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_fapi_v1_convert_get_quote(
            from_asset="BTC",
            to_asset="USDT",
            fromAmount=1
        )
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_fapi_v1_convert_accept_quote(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_fapi_v1_convert_accept_quote(quote_id="123456")
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_convert_order_status(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_convert_order_status(
            quoteid="123456"
        )
        print(result)