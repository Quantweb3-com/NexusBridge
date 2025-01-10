import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.binance.constants import BinanceUrl
from nexus.binance.spot import SpotTradingWebsocket


class TestTradingAccountApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""

        def handler(msg):
            print(msg)

        self.client = SpotTradingWebsocket(
            handler,
            binance_url=BinanceUrl.WS
        )

    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        self.client.disconnect()

    @patch('aiohttp.ClientSession.get')
    async def test_agg_trade(self, mock_get):
        await self.client.agg_trade(
            "btcusd_perp",
            _id=1
        )
        await self.client.connect()
