import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.binance.constants import BinanceUrl, Interval, KeyType, OrderType
from nexus.binance.spot import BinanceSpotWSClient
from nexus.binance.um import UmTradingWebsocket


class TestUMWebsocketClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""

        def handler(msg):
            print(msg)

        self.api_key = "ff61d44910aa178996c40382d77e2bb10996b4dc7df5a2a9c6e431944b500b48"
        self.api_secret = "4e93d727d6a5240e4986c997b7ec3d60a231143fa0c9c8cf4399c42ab22cfb24"
        self.client = UmTradingWebsocket(
            binance_url=BinanceUrl.TEST_WS,
            handler=handler,
            key=self.api_key,
            key_type=KeyType.HMAC,
            secret=self.api_secret,
            # listen_key="XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh",
            base_url="wss://fstream.binance.com/ws"
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
    async def test_ticker_price(self, mock_get):
        await self.client.ticker_price(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_ticker_book(self, mock_get):
        await self.client.ticker_book(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_order_place(self, mock_get):
        await self.client.order_place(
            "BTCUSDT",
            "BUY",
            OrderType.LIMIT,
            _id=1,
            positionSide="BOTH",
            price="43187.00",
            quantity=0.1,
            timeInForce="GTC",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_order_modify(self, mock_get):
        await self.client.order_modify(
            "BTCUSDT",
            "BUY",
            OrderType.LIMIT,
            0.1,
            43187.00,
            orderId=12
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_order_cancel(self, mock_get):
        await self.client.order_cancel(
            "BTCUSDT",
            "BUY",
            orderId=12
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_order_status(self, mock_get):
        await self.client.order_status(
            "BTCUSDT",
            orderId=12
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_account_position_v2(self, mock_get):
        await self.client.account_position_v2(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_account_position(self, mock_get):
        await self.client.account_position(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_user_data_stream_start(self, mock_get):
        await self.client.user_data_stream_start(
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_user_data_stream_ping(self, mock_get):
        await self.client.user_data_stream_ping(
            "UqZRbOrZnHhFq9zQHwQf8RWvpSOekk8N36BFDhujpOX6QHxAeV58HAHVdXZQh5yS"
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_user_data_stream_stop(self, mock_get):
        await self.client.user_data_stream_stop(
            "UqZRbOrZnHhFq9zQHwQf8RWvpSOekk8N36BFDhujpOX6QHxAeV58HAHVdXZQh5yS"
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_account_balance_v2(self, mock_get):
        await self.client.account_balance_v2(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_account_balance(self, mock_get):
        await self.client.account_balance(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_account_status_v2(self, mock_get):
        await self.client.account_status_v2(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_account_status(self, mock_get):
        await self.client.account_status(
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
    async def test_mark_price(self, mock_get):
        await self.client.mark_price(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_mark_price_arr(self, mock_get):
        await self.client.mark_price_arr(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_kline(self, mock_get):
        await self.client.kline(
            "BTCUSDT",
            Interval.DAY_1,
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_continuous_kline(self, mock_get):
        await self.client.continuous_kline(
            "BTCUSDT",
            "perpetual",
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
    async def test_ticker_arr(self, mock_get):
        await self.client.ticker_arr(
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
    async def test_book_ticker(self, mock_get):
        await self.client.book_ticker(
            "BTCUSDT",
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
            "BTCUSDT",
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
    async def test_depth_levels(self, mock_get):
        await self.client.depth_levels(
            "BTCUSDT",
            5,
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
    async def test_composite_index(self, mock_get):
        await self.client.composite_index(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_contract_info(self, mock_get):
        await self.client.contract_info(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_asset_index(self, mock_get):
        await self.client.asset_index(
            _id=1
        )
        await self.client.connect()