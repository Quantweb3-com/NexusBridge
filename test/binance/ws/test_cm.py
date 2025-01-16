import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.binance.cm import CmTradingWebsocket
from nexus.binance.constants import BinanceUrl, Interval, KeyType, OrderType
from nexus.binance.spot import BinanceSpotWSClient
from nexus.binance.um import UmTradingWebsocket


class TestCMWebsocketClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""

        def handler(msg):
            print(msg)

        self.api_key = "ff61d44910aa178996c40382d77e2bb10996b4dc7df5a2a9c6e431944b500b48"
        self.api_secret = "4e93d727d6a5240e4986c997b7ec3d60a231143fa0c9c8cf4399c42ab22cfb24"
        self.client = CmTradingWebsocket(
            binance_url=BinanceUrl.WS,
            handler=handler,
            key=self.api_key,
            key_type=KeyType.HMAC,
            secret=self.api_secret,
            # listen_key="XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh",
            # base_url="wss://fstream.binance.com/ws"
        )

    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        self.client.disconnect()

    @patch('aiohttp.ClientSession.get')
    async def test_depth(self, mock_get):
        await self.client.depth(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_agg_trade(self, mock_get):
        await self.client.agg_trade(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_index_price(self, mock_get):
        await self.client.index_price(
            "BTCUSD",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_mark_price(self, mock_get):
        await self.client.mark_price(
            "BTCUSD",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_kline(self, mock_get):
        await self.client.kline(
            "BTCUSD",
            Interval.DAY_3,
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_continuous_kline(self, mock_get):
        await self.client.continuous_kline(
            "BTCUSD",
            "perpetual",
            Interval.DAY_3,
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_pair_mark_price(self, mock_get):
        await self.client.pair_mark_price(
            "BTCUSD",
            _id=99
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_index_price_kline(self, mock_get):
        await self.client.index_price_kline(
            "BTCUSD",
            Interval.DAY_3,
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_mark_price_kline(self, mock_get):
        await self.client.mark_price_kline(
            "BTCUSD",
            Interval.DAY_3,
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_mini_ticker(self, mock_get):
        await self.client.mini_ticker(
            "BTCUSD",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_mini_ticker_arr(self, mock_get):
        await self.client.mini_ticker_arr(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_ticker(self, mock_get):
        await self.client.ticker(
            "BTCUSD",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_ticker_arr(self, mock_get):
        await self.client.ticker_arr(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_book_ticker(self, mock_get):
        await self.client.book_ticker(
            "BTCUSD",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_book_ticker_arr(self, mock_get):
        await self.client.book_ticker_arr(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_force_orders(self, mock_get):
        await self.client.force_orders(
            "BTCUSD",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_force_orders_arr(self, mock_get):
        await self.client.force_orders_arr(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_contract_info(self, mock_get):
        await self.client.contract_info(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_depth_levels(self, mock_get):
        await self.client.depth_levels(
            "BTCUSD",
            5,
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_diff_depth(self, mock_get):
        await self.client.diff_depth(
            "BTCUSD",
            _id=1
        )
        await self.client.connect()