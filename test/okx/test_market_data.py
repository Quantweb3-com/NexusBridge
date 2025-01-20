import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.okx.restapi import OkxApiClient


class TestMarketDataApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "305c4119-4911-4a22-8a07-2435eeac726a"
        self.api_secret = "221D78AFB68CB539865A11101D603CE7"
        self.passphrase = "@Or2452020438"
        self.client = OkxApiClient(self.api_key, self.api_secret, self.passphrase)
    
    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        await self.client.close_session()

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_tickers(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_market_tickers("SWAP")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_ticker(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_market_ticker("BTC-USD-SWAP")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_books(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_market_books("BTC-USDT")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_books_full(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_market_books_full("BTC-USDT")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_candles(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_market_candles("BTC-USDT")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_history_candles(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_market_history_candles("BTC-USDT")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_market_trades("BTC-USDT")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_history_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_market_history_trades("BTC-USDT")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_option_instrument_family_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_market_option_instrument_family_trades("BTC-USD")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_option_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_public_option_trades(instFamily="BTC-USD")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_platform_24_volume(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_market_platform_24_volume()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_call_auction_details(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_market_call_auction_details("BTC-USD")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)
