from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from nexus.bybit.restapi import BybitApiClient


class TestPositionApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "Z6EAzmd1YBLqQAgB7z"
        self.api_secret = "R2EshsY4AJ0eQUy8HotalYzi3dyCcYmN9yLW"
        self.client = BybitApiClient(self.api_key, self.api_secret)
    
    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        await self.client.close_session()

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_position_list(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.position_api.get_v5_position_list(
            category="inverse",
            symbol="BTCUSD",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_position_set_leverage(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.position_api.post_v5_position_set_leverage(
            category="linear",
            symbol="BTCUSDT",
            buy_leverage="6",
            sell_leverage="6",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_position_switch_isolated(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.position_api.post_v5_position_switch_isolated(
            category="linear",
            symbol="ETHUSDT",
            trade_mode=1,
            buy_leverage="10",
            sell_leverage="10",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_position_switch_mode(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.position_api.post_v5_position_switch_mode(
            category="inverse",
            symbol="BTCUSDH23",
            mode=0,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_position_trading_stop(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.position_api.post_v5_position_trading_stop(
            category="linear",
            symbol="XRPUSDT",
            takeProfit="0.6",
            stopLoss="0.2",
            tpTriggerBy="MarkPrice",
            slTriggerB="IndexPrice",
            tpslMode="Partial",
            tpOrderType="Limit",
            slOrderType="Limit",
            tpSize="50",
            slSize="50",
            tpLimitPrice="0.57",
            slLimitPrice="0.21",
            position_idx=0,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_position_set_auto_add_margin(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.position_api.post_v5_position_set_auto_add_margin(
            category="linear",
            symbol="BTCUSDT",
            auto_add_margin=1,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_position_add_margin(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.position_api.post_v5_position_add_margin(
            category="linear",
            symbol="BTCUSDT",
            margin="10"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_position_closed_pnl(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.position_api.get_v5_position_closed_pnl(
            category="linear",
            limit=1,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_position_move_positions(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.position_api.post_v5_position_move_positions(
            "100307601",
            "592324",
            [
                {
                    "category": "spot",
                    "symbol": "BTCUSDT",
                    "price": "100",
                    "side": "Sell",
                    "qty": "0.01"
                }
            ]
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.get')
    async def test_get_v5_position_move_history(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.position_api.get_v5_position_move_history(
            limit="1",
            status="Filled"
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_position_confirm_pending_mmr(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.position_api.post_v5_position_confirm_pending_mmr(
            symbol="BTCUSDT",
            category="linear",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_position_set_tpsl_mode(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.position_api.post_v5_position_set_tpsl_mode(
            symbol="XRPUSDT",
            category="linear",
            tp_sl_mode="Full",
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)

    @patch('aiohttp.ClientSession.post')
    async def test_post_v5_position_set_risk_limit(self, mock_post):
        # 执行异步 API 请求
        result = await self.client.position_api.post_v5_position_set_risk_limit(
            category="linear",
            symbol="BTCUSDT",
            risk_id=4,
        )
        # 断言返回值
        self.assertIsInstance(result, dict)
        print(result)
