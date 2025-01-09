from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from nexus.binance.constants import Side
from nexus.binance.pm import PmTradingApi


class TestGeneralClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = ""
        self.api_secret = ""
        self.client = PmTradingApi(self.api_key, self.api_secret)

    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        await self.client.close_session()

    @patch('aiohttp.ClientSession.get')
    async def test_get_papi_v1_ping(self, mock_get):
        res = await self.client.get_papi_v1_ping()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_um_order(self, mock_post):
        res = await self.client.post_papi_v1_um_order(
            symbol="",
            side=Side.BUY,
            _type="LIMIT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_um_conditional_order(self, mock_post):
        res = await self.client.post_papi_v1_um_conditional_order(
            symbol="",
            side=Side.BUY,
            strategy_type="STOP",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_cm_order(self, mock_post):
        res = await self.client.post_papi_v1_cm_order(
            symbol="",
            side=Side.BUY,
            _type="LIMIT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_cm_conditional_order(self, mock_post):
        res = await self.client.post_papi_v1_cm_conditional_order(
            symbol="",
            side=Side.BUY,
            strategy_type="STOP",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_margin_order(self, mock_post):
        res = await self.client.post_papi_v1_margin_order(
            symbol="",
            side=Side.BUY,
            _type="LIMIT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_margin_loan(self, mock_post):
        res = await self.client.post_papi_v1_margin_loan(
            asset="",
            amount=0,
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_repay_loan(self, mock_post):
        res = await self.client.post_papi_v1_repay_loan(
            asset="",
            amount=0,
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_margin_order_oco(self, mock_post):
        res = await self.client.post_papi_v1_margin_order_oco(
            symbol="",
            side=Side.BUY,
            quantity=0,
            price=0,
            stop_price=0,
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_delete_papi_v1_um_order(self, mock_post):
        res = await self.client.delete_papi_v1_um_order(
            symbol="",
            orderId=0,
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_delete_papi_v1_um_all_open_orders(self, mock_post):
        res = await self.client.delete_papi_v1_um_all_open_orders(
            symbol="",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_delete_papi_v1_um_conditional_order(self, mock_post):
        res = await self.client.delete_papi_v1_um_conditional_order(
            symbol="",
            orderId=0,
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_delete_papi_v1_um_conditional_all_open_orders(self, mock_post):
        res = await self.client.delete_papi_v1_um_conditional_all_open_orders(
            symbol="",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_delete_papi_v1_cm_order(self, mock_post):
        res = await self.client.delete_papi_v1_cm_order(
            symbol="",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_delete_papi_v1_cm_all_open_orders(self, mock_post):
        res = await self.client.delete_papi_v1_cm_all_open_orders(
            symbol="",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_delete_papi_v1_cm_conditional_order(self, mock_post):
        res = await self.client.delete_papi_v1_cm_conditional_order(
            symbol="",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_delete_papi_v1_cm_conditional_all_open_orders(self, mock_post):
        res = await self.client.delete_papi_v1_cm_conditional_all_open_orders(
            symbol="",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_delete_papi_v1_margin_order(self, mock_post):
        res = await self.client.delete_papi_v1_margin_order(
            symbol="",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_delete_papi_v1_margin_orderList(self, mock_post):
        res = await self.client.delete_papi_v1_margin_orderList(
            symbol="",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_delete_papi_v1_margin_all_open_orders(self, mock_post):
        res = await self.client.delete_papi_v1_margin_all_open_orders(
            symbol="",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_put_papi_v1_um_order(self, mock_post):
        res = await self.client.put_papi_v1_um_order(
            symbol="",
            side=Side.BUY,
            quantity=1
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_put_papi_v1_cm_order(self, mock_post):
        res = await self.client.put_papi_v1_cm_order(
            symbol="",
            side=Side.BUY,
            quantity=1
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_order(self, mock_post):
        res = await self.client.get_papi_v1_um_order(
            symbol="BTCUSDT",
            orderId=1
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_all_orders(self, mock_post):
        res = await self.client.get_papi_v1_um_all_orders(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_open_order(self, mock_post):
        res = await self.client.get_papi_v1_um_open_order(
            symbol="BTCUSDT",
            orderId=1
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_open_orders(self, mock_post):
        res = await self.client.get_papi_v1_um_open_orders(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_conditional_all_orders(self, mock_post):
        res = await self.client.get_papi_v1_um_conditional_all_orders(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_conditional_open_orders(self, mock_post):
        res = await self.client.get_papi_v1_um_conditional_open_orders(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_conditional_open_order(self, mock_post):
        res = await self.client.get_papi_v1_um_conditional_open_order(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_conditional_order_history(self, mock_post):
        res = await self.client.get_papi_v1_um_conditional_order_history(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_order(self, mock_post):
        res = await self.client.get_papi_v1_cm_order(
            symbol="BTCUSDT",
            orderId=1
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_all_orders(self, mock_post):
        res = await self.client.get_papi_v1_cm_all_orders(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_open_order(self, mock_post):
        res = await self.client.get_papi_v1_cm_open_order(
            symbol="BTCUSDT",
            orderId=1
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_open_orders(self, mock_post):
        res = await self.client.get_papi_v1_cm_open_orders(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_conditional_open_orders(self, mock_post):
        res = await self.client.get_papi_v1_cm_conditional_open_orders(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_conditional_open_order(self, mock_post):
        res = await self.client.get_papi_v1_cm_conditional_open_order(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_conditional_all_orders(self, mock_post):
        res = await self.client.get_papi_v1_cm_conditional_all_orders(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_conditional_order_history(self, mock_post):
        res = await self.client.get_papi_v1_cm_conditional_order_history(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_force_orders(self, mock_post):
        res = await self.client.get_papi_v1_um_force_orders(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_force_orders(self, mock_post):
        res = await self.client.get_papi_v1_cm_force_orders(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_order_amendment(self, mock_post):
        res = await self.client.get_papi_v1_um_order_amendment(
            symbol="BTCUSDT",
            orderId=1
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_order_amendment(self, mock_post):
        res = await self.client.get_papi_v1_cm_order_amendment(
            symbol="BTCUSDT",
            orderId=1
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_margin_force_orders(self, mock_post):
        res = await self.client.get_papi_v1_margin_force_orders(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_user_trades(self, mock_post):
        res = await self.client.get_papi_v1_um_user_trades(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_user_trades(self, mock_post):
        res = await self.client.get_papi_v1_cm_user_trades(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_adl_quantile(self, mock_post):
        res = await self.client.get_papi_v1_um_adl_quantile(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_adl_quantile(self, mock_post):
        res = await self.client.get_papi_v1_cm_adl_quantile(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_um_feeBurn(self, mock_post):
        res = await self.client.post_papi_v1_um_feeBurn(
            fee_burn="false"
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_feeBurn(self, mock_post):
        res = await self.client.get_papi_v1_um_feeBurn()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_margin_order(self, mock_post):
        res = await self.client.get_papi_v1_margin_order(
            symbol="BTCUSDT",
            orderId=1
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_margin_openOrders(self, mock_post):
        res = await self.client.get_papi_v1_margin_openOrders(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_margin_all_open_orders(self, mock_post):
        res = await self.client.get_papi_v1_margin_all_open_orders(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_margin_orderList(self, mock_post):
        res = await self.client.get_papi_v1_margin_orderList(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_margin_all_orderList(self, mock_post):
        res = await self.client.get_papi_v1_margin_all_orderList(
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_margin_openOrderList(self, mock_post):
        res = await self.client.get_papi_v1_margin_openOrderList(
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_margin_myTrades(self, mock_post):
        res = await self.client.get_papi_v1_margin_myTrades(
            symbol="BTCUSDT",
        )
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_margin_repay_debt(self, mock_post):
        res = await self.client.post_papi_v1_margin_repay_debt(
            asset="BTC",
            amount=1
        )
        print(res)
