import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.bybit.restapi import BybitApiClient


class TestAccountApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "Z6EAzmd1YBLqQAgB7z"
        self.api_secret = "R2EshsY4AJ0eQUy8HotalYzi3dyCcYmN9yLW"
        self.client = BybitApiClient(self.api_key, self.api_secret)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_account_wallet_balance(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.get_v5_account_wallet_balance(
            account_type="UNIFIED",
            coin="BTC",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_account_withdrawal(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.get_v5_account_withdrawal(
            coin_name="USDT",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_account_upgrade_to_uta(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.account_api.post_v5_account_upgrade_to_uta()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_account_borrow_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.get_v5_account_borrow_history(
            currency="BTC",
            limit=1,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_account_quick_repayment(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.account_api.post_v5_account_quick_repayment(
            "USDT"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_account_set_collateral_switch(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.account_api.post_v5_account_set_collateral_switch(
            coin="BTC",
            collateral_switch="ON"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_account_set_collateral_switch_batch(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.account_api.post_v5_account_set_collateral_switch_batch(
            [
                {
                    "coin": "BTC",
                    "collateralSwitch": "ON",
                },
                {
                    "coin": "ETH",
                    "collateralSwitch": "ON",
                }
            ]
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_account_collateral_info(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.get_v5_account_collateral_info(
            currency="BTC",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_coin_greeks(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.get_v5_asset_coin_greeks(
            base_coin="BTC",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_account_fee_rate(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.get_v5_account_fee_rate(
            symbol="ETHUSDT",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_account_info(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.get_v5_account_info()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_account_query_dcp_info(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.get_v5_account_query_dcp_info()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_account_transaction_log(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.get_v5_account_transaction_log(
            accountType="UNIFIED",
            category="linear",
            currency="USDT",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_account_contract_transaction_log(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.get_v5_account_contract_transaction_log(
            limit=1,
            symbol="BTCUSD"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_account_smp_group(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.get_v5_account_smp_group(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_v5_account_set_margin_mode(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.post_v5_account_set_margin_mode(
            "PORTFOLIO_MARGIN"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_account_set_hedging_mode(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.account_api.post_v5_account_set_hedging_mode(
            "OFF"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_v5_account_mmp_modify(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.post_v5_account_mmp_modify(
            base_coin="ETH",
            window="5000",
            frozen_period="100000",
            qty_limit="50",
            delta_limit="20"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_v5_account_mmp_reset(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.post_v5_account_mmp_reset(
            base_coin="ETH",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_account_mmp_state(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.account_api.get_v5_account_mmp_state(
            base_coin="ETH",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)