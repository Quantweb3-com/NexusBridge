import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.binance.constants import BinanceUrl, Interval, Side, OrderType
from nexus.binance.spot import SpotTradingApi


class TestGeneralClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "xRYAmLMJYZlUxmgEo3fAvVyWDFpRtx3YTXoY2bDNs3yvKmv2kt1eCjToKY0dTkJm"
        self.api_secret = "H49uCZ9tM67m8QfkNwzsaDfg05zwstuvbfdlrTGVmn7iE5FEzqj3F5lhPbbFwFcj"
        self.client = SpotTradingApi(self.api_key, self.api_secret, binance_url=BinanceUrl.TEST, )

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v3_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_api_v3_order(
            symbol="BNBBTC",
            side=Side.BUY,
            _type=OrderType.MARKET,
            quantity=1
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    # {'symbol': 'BNBBTC', 'orderId': 5862574, 'orderListId': -1, 'clientOrderId': '0Q8mkQsPEdEEpkXNpdTL57', 'transactTime': 1736222545959, 'price': '0.00000000', 'origQty': '1.00000000', 'executedQty': '1.00000000', 'origQuoteOrderQty': '0.00000000', 'cummulativeQuoteQty': '0.00716713', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 'side': 'BUY', 'workingTime': 1736222545959, 'fills': [{'price': '0.00716700', 'qty': '0.86600000', 'commission': '0.00000000', 'commissionAsset': 'BNB', 'tradeId': 1457419}, {'price': '0.00716800', 'qty': '0.13400000', 'commission': '0.00000000', 'commissionAsset': 'BNB', 'tradeId': 1457420}], 'selfTradePreventionMode': 'EXPIRE_MAKER'}

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v3_order_test(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_api_v3_order_test(
            symbol="BNBBTC",
            side=Side.BUY,
            _type=OrderType.MARKET,
            quantity=1
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_order(
            symbol="BNBBTC",
            orderId=5862574
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.delete')
    async def test_delete_api_v3_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.delete_api_v3_order(
            symbol="BNBBTC",
            orderId=5862574
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.delete')
    async def test_delete_api_v3_open_orders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.delete_api_v3_open_orders(
            symbol="BNBBTC",
        )
        print(result)

    @patch('aiohttp.ClientSession.delete')
    async def test_post_api_v3_order_cancel_replace(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_api_v3_order_cancel_replace(
            symbol="BNBBTC",
            side=Side.BUY,
            _type=OrderType.LIMIT,
            cancel_replace_mode="STOP_ON_FAILURE",
            quantity=1,
            timeInForce="GTC",
            price=10
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.delete')
    async def test_get_api_v3_open_orders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_open_orders(
            symbol="BNBBTC",
        )
        print(result)

    @patch('aiohttp.ClientSession.delete')
    async def test_get_api_v3_all_orders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v3_all_orders(
            symbol="BNBBTC",
        )
        print(result)

    @patch('aiohttp.ClientSession.delete')
    async def test_get_api_v3_account(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_api_v3_order_oco(
            symbol="BNBBTC",
            side=Side.BUY,
            quantity=10,
            price=10,
            stop_price=20,
        )
        print(result)

    @patch('aiohttp.ClientSession.delete')
    async def test_post_api_v3_sor_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_api_v3_sor_order(
            symbol="BNBBTC",
            side=Side.BUY,
            quantity=10,
            _type=OrderType.LIMIT,
            timeInForce="GTC",
            price=10,
        )
        print(result)
