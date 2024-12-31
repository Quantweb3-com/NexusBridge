import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.bybit.restapi import BybitApiClient


class TestMarketApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "Z6EAzmd1YBLqQAgB7z"
        self.api_secret = "R2EshsY4AJ0eQUy8HotalYzi3dyCcYmN9yLW"
        self.client = BybitApiClient(self.api_key, self.api_secret)

    @patch('aiohttp.ClientSession.post')
    async def test_get_v5_market_time(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_time()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_kline(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_kline(
            "BTCUSD",
            "60",
            category="inverse",
            start=1670601600000,
            end=1670608800000,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_mark_price_kline(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_mark_price_kline(
            category="linear",
            symbol="BTCUSDT",
            interval=15,
            start=1670601600000,
            end=1670608800000,
            limit=1,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_index_price_kline(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_index_price_kline(
            category="inverse",
            symbol="BTCUSDZ22",
            interval=1,
            start=1670601600000,
            end=1670608800000,
            limit=2,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_premium_index_price_kline(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_premium_index_price_kline(
            category="linear",
            symbol="BTCUSDT",
            interval="D",
            start=1652112000000,
            end=1652544000000,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_instruments_info(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_instruments_info(
            category="linear",
            symbol="BTCUSDT",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_orderbook(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_orderbook(
            category="linear",
            symbol="BTCUSDT",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_tickers(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_tickers(
            category="inverse",
            symbol="BTCUSD",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_funding_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_funding_history(
            category="linear",
            symbol="ETHPERP",
            limit=1,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_recent_trade(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_recent_trade(
            category="spot",
            symbol="BTCUSDT",
            limit=1,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_open_interest(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_open_interest(
            category="inverse",
            symbol="BTCUSD",
            interval_time="5min",
            startTime=1669571100000,
            endTime=1669571400000,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_historical_volatility(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_historical_volatility(
            category="option",
            baseCoin="ETH",
            period=30,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_insurance(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_insurance(
            coin="ETH",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_risk_limit(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_risk_limit(
            category="inverse",
            symbol="BTCUSD",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_delivery_price(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_delivery_price(
            category="option",
            symbol="ETH-26DEC22-1400-C",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_market_account_ratio(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.market_api.get_v5_market_account_ratio(
            "linear",
            "BTCUSDT",
            "1h",
            limit=2,
            startTime="1696089600000",
            endTime="1696262400000"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)
