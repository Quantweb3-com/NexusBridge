import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.binance.constants import BinanceUrl, Interval, ContractType
from nexus.binance.spot import SpotTradingApi
from nexus.binance.um import UmTradingApi


class TestGeneralClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "ff61d44910aa178996c40382d77e2bb10996b4dc7df5a2a9c6e431944b500b48"
        self.api_secret = "4e93d727d6a5240e4986c997b7ec3d60a231143fa0c9c8cf4399c42ab22cfb24"
        self.client = UmTradingApi(self.api_key, self.api_secret, binance_url=BinanceUrl.TEST, )

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_ping(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_ping()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_time(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_time()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_exchange_info(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_exchange_info()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_depth(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_depth(
            "BTCUSDT",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_trades(
            "BTCUSDT",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_historical_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_historical_trades(
            symbol="BTCUSDT",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_agg_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_agg_trades(
            symbol="BTCUSDT",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_klines(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_klines(
            symbol="BTCUSDT",
            interval=Interval.DAY_1,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_continuous_klines(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_continuous_klines(
            pair="BTCUSD",
            contract_type=ContractType.CURRENT_QUARTER,
            interval=Interval.DAY_1,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_index_price_klines(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_index_price_klines(
            pair="BTCUSDT",
            interval=Interval.DAY_1,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_mark_price_klines(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_mark_price_klines(
            symbol="BTCUSDT",
            interval=Interval.DAY_1,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_premium_index_klines(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_premium_index_klines(
            symbol="BTCUSDT",
            interval=Interval.DAY_1,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_premium_index(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_premium_index(
            symbol="BTCUSDT",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_funding_rate(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_funding_rate(
            symbol="BTCUSDT",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_funding_info(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_funding_info(
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_ticker_24hr(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_ticker_24hr(
            symbol="BTCUSDT",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_ticker_price(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_ticker_price(
            symbol="BTCUSDT",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v2_ticker_price(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v2_ticker_price(
            symbol="BTCUSDT",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_book_ticker(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_book_ticker(
            symbol="BTCUSDT",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_delivery_price(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_delivery_price(
            pair="BTCUSDT",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_open_interest(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_open_interest(
            symbol="BTCUSDT",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_open_interest_hist(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_open_interest_hist(
            symbol="BTCUSDT",
            period="1d"
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_top_long_short_position_ratio(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_futures_data_top_long_short_position_ratio(
            symbol="BTCUSDT",
            period="1d"
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_futures_data_top_long_short_account_ratio(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_futures_data_top_long_short_account_ratio(
            symbol="BTCUSDT",
            period="1d"
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_futures_data_global_long_short_account_ratio(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_futures_data_global_long_short_account_ratio(
            symbol="BTCUSDT",
            period="1d"
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_futures_data_taker_long_short_ratio(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_futures_data_taker_long_short_ratio(
            symbol="BTCUSDT",
            period="1d"
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_lvt_klines(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_lvt_klines(
            symbol="BTCUSDT",
            interval=Interval.DAY_1,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_index_info(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_index_info(
            symbol="DEFIUSDT",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_asset_index(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_asset_index(

        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_constituents(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_constituents(
            symbol="BTCUSDT",
        )
        print(result)
