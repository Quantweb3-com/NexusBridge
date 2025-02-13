from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from nexus.binance.cm import CmTradingApi
from nexus.binance.constants import BinanceUrl, Interval, ContractType


class TestGeneralClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "ff61d44910aa178996c40382d77e2bb10996b4dc7df5a2a9c6e431944b500b48"
        self.api_secret = "4e93d727d6a5240e4986c997b7ec3d60a231143fa0c9c8cf4399c42ab22cfb24"
        self.client = CmTradingApi(self.api_key, self.api_secret, binance_url=BinanceUrl.TEST, )
    
    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        await self.client.close_session()

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_ping(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_ping()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_time(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_time()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_exchange_info(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_exchange_info()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_depth(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_depth(symbol="BTCUSD_PERP")
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_trades(symbol="BTCUSD_PERP")
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_historical_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_historical_trades(symbol="BTCUSD_PERP")
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_agg_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_agg_trades(symbol="BTCUSD_PERP")
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_premium_index(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_premium_index(symbol="BTCUSD_PERP")
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_funding_rate(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_funding_rate(symbol="BTCUSD_PERP")
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_funding_info(self, mock_get):
        try:
            # 执行异步 API 请求
            result = await self.client.get_dapi_v1_funding_info()
            print(result)
        except Exception as e:
            print(e)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_klines(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_klines(symbol="BTCUSD_PERP", interval=Interval.DAY_1)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_continuous_klines(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_continuous_klines(
            pair="BTCUSD_PERP",
            interval=Interval.DAY_1,
            contract_type=ContractType.CURRENT_QUARTER
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_index_price_klines(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_index_price_klines(
            pair="BTCUSD_PERP",
            interval=Interval.DAY_1)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_mark_price_klines(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_mark_price_klines(
            symbol="BTCUSD_PERP",
            interval=Interval.DAY_1)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_premium_index_klines(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_premium_index_klines(
            symbol="BTCUSD_PERP",
            interval=Interval.DAY_1)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_ticker_24hr(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_ticker_24hr()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_ticker_price(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_ticker_price(symbol="BTCUSD_PERP")
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_ticker_book_ticker(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_ticker_book_ticker(symbol="BTCUSD_PERP")
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_open_interest(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_open_interest(symbol="BTCUSD_PERP")
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_open_interest_hist(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_futures_data_open_interest_hist(
            pair="BTCUSD_PERP",
            period="1d",
            contract_type=ContractType.PERPETUAL
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_top_long_short_position_ratio(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_futures_data_top_long_short_position_ratio(
            pair="BTCUSD_PERP",
            period="1d",
            contract_type=ContractType.PERPETUAL
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_top_long_short_account_ratio(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_futures_data_top_long_short_account_ratio(
            pair="BTCUSD_PERP",
            period="1d",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_global_long_short_account_ratio(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_futures_data_global_long_short_account_ratio(
            pair="BTCUSD_PERP",
            period="1d",
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_taker_buy_sell_vol(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_futures_data_taker_buy_sell_vol(
            pair="BTCUSD_PERP",
            period="1d",
            contract_type=ContractType.ALL
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_futures_data_basis(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_futures_data_basis(
            pair="BTCUSD_PERP",
            period="1d",
            contract_type=ContractType.CURRENT_QUARTER
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_constituents(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_constituents(symbol="BTCUSD")
        print(result)
