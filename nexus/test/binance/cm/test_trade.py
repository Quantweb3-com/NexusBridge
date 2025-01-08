import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.binance.cm import CmTradingApi
from nexus.binance.constants import BinanceUrl, Interval, ContractType, Side, OrderType
from nexus.binance.spot import SpotTradingApi
from nexus.binance.um import UmTradingApi


class TestGeneralClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "ff61d44910aa178996c40382d77e2bb10996b4dc7df5a2a9c6e431944b500b48"
        self.api_secret = "4e93d727d6a5240e4986c997b7ec3d60a231143fa0c9c8cf4399c42ab22cfb24"
        self.client = CmTradingApi(self.api_key, self.api_secret, binance_url=BinanceUrl.TEST, )

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_ping(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_ping()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_dapi_v1_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_dapi_v1_order(
            symbol='BTCUSD_200925',
            side=Side.BUY,
            _type=OrderType.MARKET,
            quantity=1,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_dapi_v1_batch_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_dapi_v1_batch_order(
            batch_orders=[
                {
                    "symbol": "BTCUSD_200925",
                    "side": "BUY",
                    "type": "MARKET",
                    "quantity": "1"
                },
            ]
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_put_dapi_v1_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.put_dapi_v1_order(
            symbol='BTCUSD_200925',
            side=Side.BUY,
            orderId=123456789,
            newClientOrderId='newClientOrderId',
            quantity=1,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_put_dapi_v1_batch_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.put_dapi_v1_batch_order(
            batch_orders=[
                {
                    "symbol": "BTCUSD_200925",
                    "orderId": "123456789",
                    "newClientOrderId": "newClientOrderId",
                    "quantity": "1"
                },
            ]
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_order_amendment(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_order_amendment(
            symbol='BTCUSD_200925',
            orderId=123456789,
            origClientOrderId='origClientOrderId',
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_delete_dapi_v1_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.delete_dapi_v1_order(
            symbol='BTCUSD_200925',
            orderId=123456789,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_delete_dapi_v1_batch_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.delete_dapi_v1_batch_order(
            symbol='BTCUSD_200925',
            order_id_list=[4076377858]
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_delete_dapi_v1_all_open_orders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.delete_dapi_v1_all_open_orders(
            symbol='BTCUSD_200925'
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_dapi_v1_countdown_cancel_all(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_dapi_v1_countdown_cancel_all(
            symbol='BTCUSD_200925',
            countdown_time=5000
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_order(
            symbol='BTCUSD_200925',
            orderId=123456789,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_all_orders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_all_orders(
            symbol='BTCUSD_200925',
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_open_orders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_open_orders(
            symbol='BTCUSD_200925',
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_open_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_open_order(
            symbol='BTCUSD_200925',
            orderId=123456789,
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_force_orders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_force_orders(
            symbol='BTCUSD_200925',
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_user_trades(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_user_trades(
            symbol='BTCUSD_200925',
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_position_risk(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_position_risk()
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_dapi_v1_position_side_dual(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_dapi_v1_position_side_dual(
            dual_side_position="false"
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_dapi_v1_margin_type(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_dapi_v1_margin_type(
            symbol='BTCUSD_200925',
            margin_type='ISOLATED'
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_dapi_v1_leverage(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_dapi_v1_leverage(
            symbol='BTCUSD_200925',
            leverage=10
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_adl_quantile(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_adl_quantile(
            symbol='BTCUSD_200925',
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_dapi_v1_position_margin(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_dapi_v1_position_margin(
            symbol='BTCUSD_200925',
            amount=1,
            _type=1
        )
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_dapi_v1_position_margin_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_dapi_v1_position_margin_history(
            symbol='BTCUSD_200925',
        )
        print(result)
