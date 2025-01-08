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
    async def test_post_fapi_v1_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_fapi_v1_order(
            symbol='BTCUSDT',
            side=Side.BUY,
            _type=OrderType.MARKET,
            quantity=0.01,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_fapi_v1_batch_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_fapi_v1_batch_order(
            batch_orders=[
                {"type": "LIMIT", "timeInForce": "GTC",
                 "symbol": "BTCUSDT", "side": "BUY", "price": "20000", "quantity": "1"}],
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_put_fapi_v1_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.put_fapi_v1_order(
            symbol='BTCUSDT',
            side=Side.BUY,
            quantity=0.01,
            price=20000,
            orderId=4076377858
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_put_fapi_v1_batch_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.put_fapi_v1_batch_order(
            batch_orders=[
                {"symbol": "BTCUSDT", "orderId": "4076377858", "price": "20001", "quantity": "1", "side": "BUY"}],
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_order_amendment(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_order_amendment(
            symbol='BTCUSDT',
            orderId=4076377858
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_delete_fapi_v1_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.delete_fapi_v1_order(
            symbol='BTCUSDT',
            orderId=4076377858
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_delete_fapi_v1_batch_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.delete_fapi_v1_batch_order(
            symbol='BTCUSDT',
            order_id_list=[4076377858]
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_delete_fapi_v1_all_open_orders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.delete_fapi_v1_all_open_orders(
            symbol='BTCUSDT'
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_fapi_v1_countdown_cancel_all(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_fapi_v1_countdown_cancel_all(
            symbol='BTCUSDT',
            countdown_time=5000
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_order(
            symbol='BTCUSDT',
            orderId=4076377858
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_all_orders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_all_orders(
            symbol='BTCUSDT',
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_open_orders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_open_orders(
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_open_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_open_order(
            symbol='BTCUSDT',
            orderId=4076377858
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_force_orders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_force_orders(
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_user_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_user_trades(
            symbol='BTCUSDT',
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_fapi_v1_margin_type(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_fapi_v1_margin_type(
            symbol='BTCUSDT',
            margin_type='ISOLATED'
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_fapi_v1_position_side_dual(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_fapi_v1_position_side_dual(
            dual_side_position="true"
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_fapi_v1_leverage(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_fapi_v1_leverage(
            symbol='BTCUSDT',
            leverage=10
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_fapi_v1_multi_assets_margin(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_fapi_v1_multi_assets_margin(
            multi_assets_margin="false"
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_fapi_v1_position_margin(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_fapi_v1_position_margin(
            symbol='BTCUSDT',
            amount=0.1,
            _type=1
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v2_position_risk(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v2_position_risk(
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v3_position_risk(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v3_position_risk(
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_adl_quantile(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_adl_quantile(
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_fapi_v1_position_margin_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_fapi_v1_position_margin_history(
            symbol='BTCUSDT',
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_fapi_v1_order_test(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_fapi_v1_order_test(
            symbol='BTCUSDT',
            side=Side.BUY,
            _type=OrderType.MARKET,
            quantity=0.01,
        )
        print(result)
