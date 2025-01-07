import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.binance.constants import BinanceUrl, Interval
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

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_trades(
            symbol="BNBBTC"
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_historical_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_historical_trades(
            symbol="BNBBTC"
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_klines(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_klines(
            symbol="BNBBTC",
            interval=Interval.DAY_1
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_ui_klines(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_ui_klines(
            symbol="BNBBTC",
            interval=Interval.DAY_1
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_avgPrice(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_avgPrice(
            symbol="BNBBTC"
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_ticker_24hr(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_ticker_24hr(
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_ticker_tradingDay(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_ticker_tradingDay(
            "BTCUSDT"
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_ticker_price(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_ticker_price(
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_ticker_bookTicker(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_ticker_bookTicker(
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_ticker(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_ticker(
            ["BTCUSDT", "BNBUSDT"]
        )
        print(result)
