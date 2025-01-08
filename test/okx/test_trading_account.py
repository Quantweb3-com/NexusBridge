from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from nexus.okx.restapi import OkxApiClient


class TestTradingAccountApiClient(IsolatedAsyncioTestCase):
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
    async def test_get_api_v5_account_instruments(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_instruments("SPOT")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_balance(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_balance("BTC,ETH")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_positions(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_positions(
            instId="BTC-USDT"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_positions_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_positions_history(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_position_risk(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_position_risk(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_bills(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_bills(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_bills_archive(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_bills_archive(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_account_bills_history_archive(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_bills_history_archive(
            "2024",
            "Q1"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_bills_history_archive(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_bills_history_archive(
            "2024",
            "Q1"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_config(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_config(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_account_set_position_mode(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_set_position_mode(
            "long_short_mode"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_account_set_leverage(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_set_leverage(
            "cross",
            "5",
            "SPOT",
            instId="BTC-USDT",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_max_size(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_max_size(
            "BTC-USDT",
            "isolated"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_max_avail_size(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_max_avail_size(
            "BTC-USDT",
            "cross",
            ccy="BTC"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_account_position_margin_balance(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_position_margin_balance(
            "BTC-USDT-200626",
            "short",
            "add",
            "1"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_leverage_info(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_leverage_info(
            "cross",
            instId="BTC-USDT-SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_adjust_leverage_info(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_adjust_leverage_info(
            "MARGIN",
            "isolated",
            "3",
            instId="BTC-USDT"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_max_loan(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_max_loan(
            "cross",
            instId="BTC-USDT"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_trade_fee(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_trade_fee(
            "SPOT",
            instId="BTC-USDT"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_interest_accrued(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_interest_accrued(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_interest_rate(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_interest_rate()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_account_set_greeks(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_set_greeks(
            "PA"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_account_set_isolated_mode(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_set_isolated_mode(
            "MARGIN"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_max_withdrawal(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_max_withdrawal(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_risk_state(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_risk_state(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_account_quick_margin_borrow_repay(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_quick_margin_borrow_repay(
            "BTC-USDT",
            "USDT",
            "100",
            "borrow",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_quick_margin_borrow_repay_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_quick_margin_borrow_repay_history()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_interest_limits(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_interest_limits(
            "1",
            "BTC"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_fixed_loan_borrowing_limit(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_fixed_loan_borrowing_limit(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_fixed_loan_borrowing_quote(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_fixed_loan_borrowing_quote(
            "normal",
            ccy="BTC",
            maxRate="0.1",
            amt="0.1",
            term="30D"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_account_fixed_loan_borrowing_order(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_fixed_loan_borrowing_order(
            "BTC",
            "0.1",
            "0.01",
            reborrow="True",
            reborrowRate="0.01"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_account_fixed_loan_amend_borrowing_order(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_fixed_loan_amend_borrowing_order(
            "2405162053378222",
            reborrow=True,
            renewMaxRate="0.01"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_account_fixed_loan_manual_reborrow(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_fixed_loan_manual_reborrow(
            "2405162053378222",
            "0.01"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_account_fixed_loan_repay_borrowing_order(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_fixed_loan_repay_borrowing_order(
            "2405162053378222",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_account_fixed_loan_convert_to_market_loan(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_fixed_loan_convert_to_market_loan(
            "2409141848234868",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_account_fixed_loan_reduce_liabilities(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_fixed_loan_reduce_liabilities(
            "2409141802194350",
            True
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_fixed_loan_borrowing_orders_list(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_fixed_loan_borrowing_orders_list()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_account_spot_manual_borrow_repay(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_spot_manual_borrow_repay(
            "USDT",
            "100",
            "borrow",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_account_set_auto_repay(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_set_auto_repay(
            True
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_spot_borrow_repay_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_spot_borrow_repay_history()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_account_position_builder(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_position_builder(
            inclRealPosAndEq=False,
            simPos=[
                {
                    "pos": "-10",
                    "instId": "BTC-USDT-SWAP"
                },
                {
                    "pos": "10",
                    "instId": "LTC-USDT-SWAP"
                }
            ],
            simAsset=[
                {
                    "ccy": "USDT",
                    "amt": "100"
                }
            ],
            spotOffsetType="1",
            greeksType="CASH"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_account_set_risk_offset_amt(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_set_risk_offset_amt(
            "0.5",
            "BTC"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_get_api_v5_account_greeks(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_greeks(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_position_tiers(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_position_tiers(
            "SWAP",
            uly="BTC-USDT"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_account_set_risk_offset_type(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_set_risk_offset_type(
            "1"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_account_activate_option(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_activate_option(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_account_set_auto_loan(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_set_auto_loan(
            True
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_account_account_level_switch_preset(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_account_level_switch_preset(
            "3"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_set_account_switch_precheck(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_set_account_switch_precheck(
            "3"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_account_set_account_level_switch(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_set_account_level(
            "1"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_account_mmp_reset(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_mmp_reset(
            "BTC-USD"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_account_mmp_config(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.post_api_v5_account_mmp_config(
            "BTC-USD",
            "5000",
            "2000",
            "100"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_account_mmp_config(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.trading_account_api.get_api_v5_account_mmp_config(
            "BTC-USD"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)
