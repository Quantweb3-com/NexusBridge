import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.okx.restapi import OkxApiClient


class TestPublicDataApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "305c4119-4911-4a22-8a07-2435eeac726a"
        self.api_secret = "221D78AFB68CB539865A11101D603CE7"
        self.passphrase = "@Or2452020438"
        self.client = OkxApiClient(self.api_key, self.api_secret, self.passphrase)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_instruments(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_instruments(
            inst_type="SPOT"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_delivery_exercise_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_delivery_exercise_history(
            inst_type="FUTURES",
            uly="BTC-USD"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_open_interest(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_open_interest(
            inst_type="SWAP",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_funding_rate(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_funding_rate(
            inst_id="BTC-USD-SWAP",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_funding_rate_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_funding_rate_history(
            inst_id="BTC-USD-SWAP",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_price_limit(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_price_limit(
            inst_id="BTC-USD-SWAP",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_opt_summary(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_opt_summary(
            uly="BTC-USD",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_estimated_price(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_estimated_price(
            inst_id="BTC-USDT-220916",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_discount_rate_interest_free_quota(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_discount_rate_interest_free_quota(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_time(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_time()
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_mark_price(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_mark_price(
            inst_id="SWAP",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_position_tiers(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_position_tiers(
            inst_type="SWAP",
            td_mode="cross",
            uly="BTC-USD"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_interest_rate_loan_quota(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_interest_rate_loan_quota(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_underlying(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_underlying(
            inst_type="FUTURES"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_insurance_fund(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_insurance_fund(
            inst_type="SWAP",
            uly="BTC-USD"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_convert_contract_coin(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_convert_contract_coin(
            inst_id="BTC-USD-SWAP",
            px="35000",
            sz="0.888"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_instrument_tick_bands(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_instrument_tick_bands(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_premium_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_premium_history(
            inst_id="BTC-USDT-SWAP",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_index_tickers(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_market_index_tickers(
            instId="BTC-USDT"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_index_candles(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_market_index_candles(
            inst_id="BTC-USD"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_history_index_candles(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_market_history_index_candles(
            inst_id="BTC-USD",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_mark_price_candles(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_market_mark_price_candles(
            inst_id="BTC-USD-SWAP"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_history_mark_price_candles(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_market_history_mark_price_candles(
            inst_id="BTC-USD-SWAP",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_open_oracle(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_market_open_oracle(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_exchange_rate(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_market_exchange_rate(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_market_index_components(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_market_index_components(
            index="BTC-USD"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v5_public_economic_calendar(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.public_data_api.get_api_v5_public_economic_calendar(
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)
