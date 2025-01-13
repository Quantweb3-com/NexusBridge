import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.binance.constants import BinanceUrl, Interval
from nexus.binance.spot import BinanceSpotWSClient


class TestTradingAccountApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""

        def handler(msg):
            print(msg)

        self.client = BinanceSpotWSClient(
            binance_url=BinanceUrl.WS,
            handler=handler,
            base_url="wss://ws-api.binance.com:443/ws-api/v3"
        )

    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        self.client.disconnect()

    @patch('aiohttp.ClientSession.get')
    async def test_agg_trade(self, mock_get):
        await self.client.agg_trade(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_trade(self, mock_get):
        await self.client.trade(
            "BTCUSDT",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_kline(self, mock_get):
        await self.client.kline(
            "BTCUSDT",
            "1m",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_ui_kline(self, mock_get):
        await self.client.ui_kline(
            "BTCUSDT",
            "1m",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_mini_ticker(self, mock_get):
        await self.client.mini_ticker(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_mini_ticker_array(self, mock_get):
        await self.client.mini_ticker_arr(
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_ticker(self, mock_get):
        await self.client.ticker(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_ticker_arr(self, mock_get):
        await self.client.ticker_arr(
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_ticker_windows(self, mock_get):
        await self.client.ticker_window(
            "BTCUSDT",
            "1d",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_ticker_window_arr(self, mock_get):
        await self.client.ticker_window_arr(
            window_size="1d"
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_book_ticker(self, mock_get):
        await self.client.book_ticker(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_avg_price(self, mock_get):
        await self.client.avg_price(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_depth(self, mock_get):
        await self.client.depth(
            "BTCUSDT",
            levels=10,
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_diff_depth(self, mock_get):
        await self.client.diff_depth(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_order_book(self, mock_get):
        await self.client.order_book(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_recent_trades(self, mock_get):
        await self.client.recent_trades(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_historical_trades(self, mock_get):
        await self.client.historical_trades(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_agg_trades(self, mock_get):
        await self.client.agg_trades(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_klines(self, mock_get):
        await self.client.klines(
            "BTCUSDT",
            Interval.MINUTE_1,
            _id=1
        )
        await self.client.connect()
