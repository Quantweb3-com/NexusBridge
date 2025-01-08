from unittest import IsolatedAsyncioTestCase

import orjson
from unittest.mock import patch
from nexus.bybit.constants import BybitAccountType
from nexus.bybit.wsapi import BybitWSClient, generate_topic


class TestPositionApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "Z6EAzmd1YBLqQAgB7z"
        self.api_secret = "R2EshsY4AJ0eQUy8HotalYzi3dyCcYmN9yLW"

        def handler(msg):
            print(orjson.loads(msg))

        self.client = BybitWSClient(BybitAccountType.LINEAR_TESTNET, handler, self.api_key, self.api_secret)
    
    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        self.client.disconnect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_order_book(self, mock_get):
        await self.client.subscribe_order_book("BTCUSDT", 1)
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_multiple(self, mock_get):
        await self.client.subscribe_multiple([
            generate_topic("orderbook", "BTCUSDT", 1),
            generate_topic("publicTrade", "BTCUSDT")
        ], False)
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_trade(self, mock_get):
        await self.client.subscribe_trade("BTCUSDT")
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_ticker(self, mock_get):
        await self.client.subscribe_ticker("BTCUSDT")
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_kline(self, mock_get):
        await self.client.subscribe_kline("BTCUSDT", "5")
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_liquidation(self, mock_get):
        await self.client.subscribe_liquidation("BTCUSDT")
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_lt_kline(self, mock_get):
        await self.client.subscribe_lt_kline("BTC3SUSDT", "30")
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_lt_ticker(self, mock_get):
        await self.client.subscribe_lt_ticker("BTC3SUSDT")
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_lt_nav(self, mock_get):
        await self.client.subscribe_lt_nav("BTC3SUSDT")
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_order(self, mock_get):
        await self.client.subscribe_order("order")
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_position(self, mock_get):
        await self.client.subscribe_position("position")
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_wallet(self, mock_get):
        await self.client.subscribe_wallet("wallet")
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_execution(self, mock_get):
        await self.client.subscribe_execution("execution")
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_fast_execution(self, mock_get):
        await self.client.subscribe_fast_execution("execution.fast")
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_greek(self, mock_get):
        await self.client.subscribe_greek("greeks")
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_subscribe_dcp(self, mock_get):
        await self.client.subscribe_dcp("dcp.future")
        await self.client.connect()
