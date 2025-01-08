from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from nexus.bybit.restapi import BybitApiClient


class TestAssetApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "Z6EAzmd1YBLqQAgB7z"
        self.api_secret = "R2EshsY4AJ0eQUy8HotalYzi3dyCcYmN9yLW"
        self.client = BybitApiClient(self.api_key, self.api_secret)
    
    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        await self.client.close_session()

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_delivery_record(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_delivery_record(
            category="option",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_settlement_record(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_settlement_record(
            category="linear",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_exchange_order_record(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_exchange_order_record(
            limit=10,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_coin_query_info(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_coin_query_info(
            coin="ETH",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_transfer_query_sub_member_list(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_transfer_query_sub_member_list()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_transfer_query_asset_info(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_transfer_query_asset_info(
            account_type="FUND",
            coin="USDC",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_transfer_query_account_coins_balance(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_transfer_query_account_coins_balance(
            account_type="FUND",
            coin="USDC",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_transfer_query_account_coin_balance(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_transfer_query_account_coin_balance(
            account_type="UNIFIED",
            coin="BTC",
            memberId=592324,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_withdraw_withdrawable_amount(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_withdraw_withdrawable_amount(
            coin="BTC",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_transfer_query_transfer_coin_list(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_transfer_query_transfer_coin_list(
            from_account_type="UNIFIED",
            to_account_type="CONTRACT",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_v5_asset_transfer_inter_transfer(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.post_v5_asset_transfer_inter_transfer(
            transfer_id="42c0cfb0-6bca-c242-bc76-4e6df6cbcb16",
            coin="BTC",
            amount="0.05",
            from_account_type="UNIFIED",
            to_account_type="CONTRACT",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_transfer_query_inter_transfer_list(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_transfer_query_inter_transfer_list(
            coin="USDT",
            limit=1,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_asset_transfer_universal_transfer(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.asset_api.post_v5_asset_transfer_universal_transfer(
            transfer_id="be7a2462-1138-4e27-80b1-62653f24925e",
            coin="ETH",
            amount="0.5",
            from_member_id=592334,
            to_member_id=691355,
            from_account_type="CONTRACT",
            to_account_type="UNIFIED",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_transfer_query_universal_transfer_list(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_transfer_query_universal_transfer_list(
            limit=1,
            cursor="eyJtaW5JRCI6MTc5NjU3OCwibWF4SUQiOjE3OTY1Nzh9",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_deposit_query_allowed_list(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_deposit_query_allowed_list(
            coin="ETH",
            chain="ETH",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_asset_deposit_to_account(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.asset_api.post_v5_asset_deposit_to_account(
            account_type="CONTRACT",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_deposit_query_record(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_deposit_query_record(
            coin="USDT",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_deposit_query_sub_member_record(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_deposit_query_sub_member_record(
            coin="USDT",
            limit=1,
            sub_member_id=592334,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_deposit_query_internal_record(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_deposit_query_internal_record(
            startTime=1667260800000,
            endTime=1667347200000,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_deposit_query_address(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_deposit_query_address(
            coin="USDT",
            chain_type="ETH",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_deposit_query_sub_member_address(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_deposit_query_sub_member_address(
            coin="USDT",
            chain_type="TRX",
            sub_member_id=592334,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_withdraw_query_record(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_withdraw_query_record(
            coin="USDT",
            withdrawType=2,
            limit=2,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_withdraw_query_vasp_list(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_withdraw_query_vasp_list(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_asset_withdraw_create(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.asset_api.post_v5_asset_withdraw_create(
            coin="USDT",
            chain="ETH",
            address="0x99ced129603abc771c0dabe935c326ff6c86645d",
            amount="24",
            timestamp=1672196561407,
            forceChain=0,
            accountType="FUND",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_asset_withdraw_cancel(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.asset_api.post_v5_asset_withdraw_cancel(
            _id="10197",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_exchange_query_coin_list(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_exchange_query_coin_list(
            account_type="eb_convert_funding",
            size=0,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_asset_exchange_quote_apply(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.asset_api.post_v5_asset_exchange_quote_apply(
            from_coin="ETH",
            to_coin="BTC",
            request_amount="0.1",
            account_type="eb_convert_funding",
            request_coin="ETH",
            requestId="test-00002",
            paramType="opFrom",
            paramValue="broker-id-001"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_asset_exchange_convert_execute(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.asset_api.post_v5_asset_exchange_convert_execute(
            "10100108106409343501030232064"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_exchange_convert_result_query(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_exchange_convert_result_query(
            "10100108106409343501030232064",
            "eb_convert_funding"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_asset_exchange_query_convert_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.asset_api.get_v5_asset_exchange_query_convert_history(
            account_type="eb_convert_uta,eb_convert_funding",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)
