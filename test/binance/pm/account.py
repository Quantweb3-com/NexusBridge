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

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_balance(self, mock_post):
        res = await self.client.get_papi_v1_balance()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_account(self, mock_post):
        res = await self.client.get_papi_v1_account()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_margin_maxBorrowable(self, mock_post):
        res = await self.client.get_papi_v1_margin_max_borrowable("BTC")
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_margin_max_withdraw(self, mock_post):
        res = await self.client.get_papi_v1_margin_max_withdraw("BTC")
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_positionRisk(self, mock_post):
        res = await self.client.get_papi_v1_um_position_risk()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_position_risk(self, mock_post):
        res = await self.client.get_papi_v1_cm_position_risk()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_um_leverage(self, mock_post):
        res = await self.client.post_papi_v1_um_leverage("BTCUSDT", 10)
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_cm_leverage(self, mock_post):
        res = await self.client.post_papi_v1_cm_leverage("BTCUSDT", 10)
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_um_positionSide_dual(self, mock_post):
        res = await self.client.post_papi_v1_um_position_side_dual("false")
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_cm_positionSide_dual(self, mock_post):
        res = await self.client.post_papi_v1_cm_position_side_dual("false")
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_positionSide_dual(self, mock_post):
        res = await self.client.get_papi_v1_um_position_side_dual()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_positionSide_dual(self, mock_post):
        res = await self.client.get_papi_v1_cm_position_side_dual()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_leverage_bracket(self, mock_post):
        res = await self.client.get_papi_v1_um_leverage_bracket()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_leverage_bracket(self, mock_post):
        res = await self.client.get_papi_v1_cm_leverage_bracket()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_api_trading_status(self, mock_post):
        res = await self.client.get_papi_v1_um_api_trading_status()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_commission_rate(self, mock_post):
        res = await self.client.get_papi_v1_um_commission_rate("BTCUSDT")
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_commission_rate(self, mock_post):
        res = await self.client.get_papi_v1_cm_commission_rate("BTCUSDT")
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_force_orders(self, mock_post):
        res = await self.client.get_papi_v1_margin_margin_loan("BNB")
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_margin_repay_loan(self, mock_post):
        res = await self.client.get_papi_v1_margin_repay_loan("BNB")
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_repay_futures_switch(self, mock_post):
        res = await self.client.get_papi_v1_repay_futures_switch()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_repay_futures_switch(self, mock_post):
        res = await self.client.post_papi_v1_repay_futures_switch("true")
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_margin_margin_interest_history(self, mock_post):
        res = await self.client.get_papi_v1_margin_margin_interest_history()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_repay_futures_negative_balance(self, mock_post):
        res = await self.client.post_papi_v1_repay_futures_negative_balance()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_portfolio_interest_history(self, mock_post):
        res = await self.client.get_papi_v1_portfolio_interest_history()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_auto_collection(self, mock_post):
        res = await self.client.post_papi_v1_auto_collection("true")
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_asset_collection(self, mock_post):
        res = await self.client.post_papi_v1_asset_collection("BNB")
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_bnb_transfer(self, mock_post):
        res = await self.client.post_papi_v1_bnb_transfer("FROM_UM", 10)
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_income(self, mock_post):
        res = await self.client.get_papi_v1_um_income()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_income(self, mock_post):
        res = await self.client.get_papi_v1_cm_income()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_account_trades(self, mock_post):
        res = await self.client.get_papi_v1_um_account()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_cm_account_trades(self, mock_post):
        res = await self.client.get_papi_v1_cm_account()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_account_config(self, mock_post):
        res = await self.client.get_papi_v1_um_account_config()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_symbol_config(self, mock_post):
        res = await self.client.get_papi_v1_um_symbol_config()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v2_um_account(self, mock_post):
        res = await self.client.get_papi_v2_um_account()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_trade_asyn(self, mock_post):
        res = await self.client.get_papi_v1_um_trade_asyn(1, 10)
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_trade_asyn_id(self, mock_post):
        res = await self.client.get_papi_v1_um_trade_asyn_id("929653413502410752")
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_order_asyn(self, mock_post):
        res = await self.client.get_papi_v1_um_order_asyn(1, 10)
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_order_asyn_id(self, mock_post):
        res = await self.client.get_papi_v1_um_order_asyn_id("929654194686119936")
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_income_asyn(self, mock_post):
        res = await self.client.get_papi_v1_um_income_asyn(1, 10)
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_um_income_asyn_id(self, mock_post):
        res = await self.client.get_papi_v1_um_income_asyn_id("929654690994765824")
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_get_papi_v1_rateLimit_order(self, mock_post):
        res = await self.client.get_papi_v1_rate_limit_order()
        print(res)
