import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from nexus.okx.restapi import OkxApiClient


class TestTradeApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "305c4119-4911-4a22-8a07-2435eeac726a"
        self.api_secret = "221D78AFB68CB539865A11101D603CE7"
        self.passphrase = "@Or2452020438"
        self.client = OkxApiClient(self.api_key, self.api_secret, self.passphrase)

    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        await self.client.close_session()

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_order(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_order(
            "BTC-USDT",
            "cash",
            "buy",
            "limit",
            "2",
            px="10",
            clOrdId="b26"
        )
        # 断言返回值
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_cancel_order(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_cancel_order(
            "BTC-USD-190927",
            "590908157585625111")
        # 断言返回值
        self.assertIsInstance(result, dict)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_batch_orders(self, mock_post):
        json_data = '''
        [
            {
                "instId":"BTC-USDT",
                "tdMode":"cash",
                "clOrdId":"b34",
                "side":"buy",
                "ordType":"limit",
                "px":"2.15",
                "sz":"2"
            },
            {
                "instId":"BTC-USDT",
                "tdMode":"cash",
                "clOrdId":"b43",
                "side":"buy",
                "ordType":"limit",
                "px":"2.15",
                "sz":"2"
            }
        ]
        '''

        # Parse the JSON data
        data = json.loads(json_data)

        # Ensure the data is a list of dictionaries with string keys and values
        list_of_dicts = [dict((k, str(v)) for k, v in item.items()) for item in data]

        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_batch_orders(
            list_of_dicts
        )
        # 断言返回值
        self.assertIsInstance(result, dict)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_cancel_batch_orders(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_cancel_batch_orders(
            [
                {
                    "instId": "BTC-USDT",
                    "ordId": "590908157585625111"
                },
                {
                    "instId": "BTC-USDT",
                    "ordId": "590908544950571222"
                }
            ]
        )
        # 断言返回值
        self.assertIsInstance(result, dict)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_amend_order(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_amend_order(
            "BTC-USDT",
            ord_id="590909145319051111",
            newSz="2"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_amend_batch_orders(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_amend_batch_orders(
            [
                {
                    "ordId": "590909308792049444",
                    "newSz": "2",
                    "instId": "BTC-USDT"
                },
                {
                    "ordId": "590909308792049555",
                    "newSz": "2",
                    "instId": "BTC-USDT"
                }
            ]
        )
        # 断言返回值
        self.assertIsInstance(result, dict)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_close_position(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_close_position(
            "TC-USDT-SWAP",
            "cross",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trade_order(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_trade_order(
            "BTC-USDT",
            ord_id="1753197687182819328"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trade_orders_pending(self, mock_get):
        # 执行异步 API 请求
        # GET /api/v5/trade/orders-pending?ordType=post_only,fok,ioc&instType=SPOT
        result = await self.client.get_api_v5_trade_orders_pending(
            ordType="post_only,fok,ioc",
            instType="SPOT"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trade_orders_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_trade_orders_history(
            "SPOT",
            ordType="post_only,fok,ioc",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trade_orders_history_archive(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_trade_orders_history_archive(
            "SPOT",
            ordType="post_only,fok,ioc",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trade_fills(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_trade_fills(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trade_fills_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_trade_fills_history(
            "SPOT",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trade_easy_convert_currency_list(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_trade_easy_convert_currency_list()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_easy_convert(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_easy_convert(
            from_ccy=["ADA", "USDC"],
            to_ccy="OKB"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trade_easy_convert_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_trade_easy_convert_history()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trade_one_click_repay_currency_list(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_trade_one_click_repay_currency_list()
        # 断言返回值
        self.assertIsInstance(result, dict)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_one_click_repay(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_one_click_repay(
            debt_ccy=["BTC", "ETH"],
            repay_ccy="USDT"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trade_one_click_repay_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_trade_one_click_repay_history()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_mass_cancel(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_mass_cancel(
            "OPTION",
            "BTC-USD"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_mass_cancel_all(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_cancel_all_after(
            "60"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_trade_account_rate_limit(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.get_api_v5_trade_account_rate_limit(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_api_v5_trade_account_leverage(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.post_api_v5_trade_order_precheck(
            "BTC-USDT",
            "cash",
            "buy",
            "limit",
            "2",
            px="2.15",
            clOrdId="b15",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)
