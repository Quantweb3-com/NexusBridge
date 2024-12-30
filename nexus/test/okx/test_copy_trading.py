import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.okx.restapi import OkxApiClient


class TestCopyTradingApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "305c4119-4911-4a22-8a07-2435eeac726a"
        self.api_secret = "221D78AFB68CB539865A11101D603CE7"
        self.passphrase = "@Or2452020438"
        self.client = OkxApiClient(self.api_key, self.api_secret, self.passphrase)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_current_subpositions(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_current_subpositions()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_subpositions_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_subpositions_history()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_copytrading_algo_order(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.post_api_v5_copytrading_algo_order(
            "518541406042591232",
            tpTriggerPx="10000",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_copytrading_close_subposition(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.post_api_v5_copytrading_close_subposition("518541406042591232")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_instruments(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_instruments()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_copytrading_set_instruments(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.post_api_v5_copytrading_set_instruments(
            "BTC-USDT-SWAP,ETH-USDT-SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_profit_sharing_details(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_profit_sharing_details(
            limit="2"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_total_profit_sharing(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_total_profit_sharing()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_unrealized_profit_sharing_details(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_unrealized_profit_sharing_details()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_total_unrealized_profit_sharing(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_total_unrealized_profit_sharing()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_copytrading_apply_lead_trading(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.post_api_v5_copytrading_apply_lead_trading(
            "BTC-USDT-SWAP",
            inst_type="SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_copytrading_stop_lead_trading(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.post_api_v5_copytrading_stop_lead_trading(
            "SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_post_api_v5_copytrading_amend_profit_sharing_ratio(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.post_api_v5_copytrading_amend_profit_sharing_ratio(
            "0.1",
            "SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_config(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_config()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_copytrading_first_copy_settings(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.post_api_v5_copytrading_first_copy_settings(
            "25CD5A80241D6FE6",
            "cross",
            "copy",
            "500",
            "copy_close",
            copyRatio="1",
            instType="SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_copytrading_amend_copy_settings(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.post_api_v5_copytrading_amend_copy_settings(
            "25CD5A80241D6FE6",
            "cross",
            "copy",
            "500",
            "copy_close",
            copyRatio="1",
            instType="SWAP",
            copyMode="ratio_copy"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_copytrading_stop_copy_trading(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.post_api_v5_copytrading_stop_copy_trading(
            "25CD5A80241D6FE6",
            "manual_close",
            "SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_copy_settings(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_copy_settings(
            "25CD5A80241D6FE6",
            "SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_current_lead_traders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_current_lead_traders(
            "SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_public_config(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_public_config("SWAP")
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_public_lead_traders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_public_lead_traders(
            instType="SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_public_weekly_pnl(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_public_weekly_pnl(
            "D9ADEAB33AE9EABD",
            "SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_public_pnl(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_public_pnl(
            "D9ADEAB33AE9EABD",
            "1",
            "SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_public_stats(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_public_stats(
            "D9ADEAB33AE9EABD",
            "1",
            "SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_public_preference_currency(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_public_preference_currency(
            "CB4594A3BB5D3538",
            "SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_public_current_subpositions(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_public_current_subpositions(
            "D9ADEAB33AE9EABD",
            instType="SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_public_subpositions_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_public_subpositions_history(
            "9A8534AB09862774",
            instType="SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_public_copy_traders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_public_copy_traders(
            "D9ADEAB33AE9EABD",
            instType="SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_lead_traders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_lead_traders(
            instType="SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_weekly_pnl(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_weekly_pnl(
            "D9ADEAB33AE9EABD",
            "SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_pnl(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_pnl(
            "D9ADEAB33AE9EABD",
            "1",
            "SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_stats(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_stats(
            "D9ADEAB33AE9EABD",
            "1",
            "SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_preference_currency(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_preference_currency(
            "CB4594A3BB5D3538",
            "SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_performance_current_subpositions(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_performance_current_subpositions(
            "D9ADEAB33AE9EABD",
            instType="SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_performance_subpositions_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_performance_subpositions_history(
            "9A8534AB09862774",
            instType="SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_copytrading_copy_traders(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.copy_trading_api.get_api_v5_copytrading_copy_traders(
            "D9ADEAB33AE9EABD",
            instType="SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)
