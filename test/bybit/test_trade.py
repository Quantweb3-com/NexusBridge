from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from nexus.bybit.restapi import BybitApiClient


class TestTradeApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "Z6EAzmd1YBLqQAgB7z"
        self.api_secret = "R2EshsY4AJ0eQUy8HotalYzi3dyCcYmN9yLW"
        self.client = BybitApiClient(self.api_key, self.api_secret)
    
    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        await self.client.close_session()

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_order_create(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trade_api.post_v5_order_create(
            category="spot",
            symbol="BTCUSDT",
            side="Sell",
            order_type="Limit",
            qty="0.1",
            price="141000",
            timeInForce="PostOnly",
            orderLinkId="spot-test-postonly",
            isLeverage=0,
            orderFilter="Order",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_order_amend(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trade_api.post_v5_order_amend(
            category="linear",
            symbol="ETHPERP",
            orderLinkId="linear-004",
            triggerPrice="1145",
            qty="0.15",
            price="1050",
            takeProfit="0",
            stopLoss="0",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_order_cancel(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trade_api.post_v5_order_cancel(
            category="linear",
            symbol="BTCPERP",
            orderId="c6f055d9-7f21-4079-913d-e6523a9cfffa",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_order_realtime(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trade_api.get_v5_order_realtime(
            category="linear",
            symbol="ETHUSDT",
            openOnly=0,
            limit=1,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_order_cancel_all(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trade_api.post_v5_order_cancel_all(
            category="linear",
            settleCoin="USDT",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_order_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trade_api.get_v5_order_history(
            category="linear",
            limit=1,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_execution_list(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trade_api.get_v5_execution_list(
            category="linear",
            limit=1,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_order_create_batch(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trade_api.post_v5_order_create_batch(
            category="spot",
            request=[
                {
                    "symbol": "BTCUSDT",
                    "side": "Buy",
                    "orderType": "Limit",
                    "isLeverage": 0,
                    "qty": "0.05",
                    "price": "30000",
                    "timeInForce": "GTC",
                    "orderLinkId": "spot-btc-03"
                },
                {
                    "symbol": "ATOMUSDT",
                    "side": "Sell",
                    "orderType": "Limit",
                    "isLeverage": 0,
                    "qty": "2",
                    "price": "12",
                    "timeInForce": "GTC",
                    "orderLinkId": "spot-atom-03"
                }
            ]
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_order_amend_batch(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trade_api.post_v5_order_amend_batch(
            category="option",
            request=[
                {
                    "category": "option",
                    "symbol": "ETH-30DEC22-500-C",
                    "orderIv": "6.8",
                    "orderId": "b551f227-7059-4fb5-a6a6-699c04dbd2f2"
                },
                {
                    "category": "option",
                    "symbol": "ETH-30DEC22-700-C",
                    "price": "650",
                    "orderId": "fa6a595f-1a57-483f-b9d3-30e9c8235a52"
                }
            ]
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_order_cancel_batch(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trade_api.post_v5_order_cancel_batch(
            category="spot",
            request=[
                {
                    "symbol": "BTCUSDT",
                    "orderId": "1666800494330512128"
                },
                {
                    "symbol": "ATOMUSDT",
                    "orderLinkId": "1666800494330512129"
                }
            ]
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_order_spot_borrow_check(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trade_api.get_v5_order_spot_borrow_check(
            category="spot",
            symbol="BTCUSDT",
            side="Buy",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_order_disconnected_cancel_all(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trade_api.post_v5_order_disconnected_cancel_all(
            time_window=40,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

