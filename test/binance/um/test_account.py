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
    
    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        await self.client.close_session()

    @patch('aiohttp.ClientSession.get')
    async def test_post_fapi_v1_listen_key(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_fapi_v1_listen_key()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v3_balance(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v3_balance()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v2_balance(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v2_balance()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v3_account(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v3_account()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v2_account(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v2_account()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_commission_rate(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_commission_rate('BTCUSDT')
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_account_config(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_account_config()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_symbol_config(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_symbol_config()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_rate_limit_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_rate_limit_order()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_leverage_bracket(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_leverage_bracket()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_multi_assets_margin(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_multi_assets_margin()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_position_side_dual(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_position_side_dual()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_income(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_income()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_api_trading_status(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_api_trading_status()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_income_asyn(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_income_asyn(
            start_time=1622505600000,
            end_time=1622592000000,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_income_asyn_id(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_income_asyn_id(download_id="545923594199212032")
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_order_asyn(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_order_asyn(
            start_time=1622505600000,
            end_time=1622592000000,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_order_asyn_id(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_order_asyn_id(download_id="545923594199212032")
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_trade_asyn(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_trade_asyn(
            start_time=1622505600000,
            end_time=1622592000000,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_trade_asyn_id(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_trade_asyn_id(download_id="545923594199212032")
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_fapi_v1_fee_burn(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_fapi_v1_fee_burn("true")
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_fee_burn(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_fee_burn()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_pm_account_info(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_pm_account_info("BTC")
        print(result)
