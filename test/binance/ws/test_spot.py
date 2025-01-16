import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.binance.constants import BinanceUrl, Interval, KeyType, OrderType
from nexus.binance.spot import BinanceSpotWSClient


class TestTradingAccountApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""

        def handler(msg):
            print(msg)

        self.api_key = "xRYAmLMJYZlUxmgEo3fAvVyWDFpRtx3YTXoY2bDNs3yvKmv2kt1eCjToKY0dTkJm"
        self.api_secret = "H49uCZ9tM67m8QfkNwzsaDfg05zwstuvbfdlrTGVmn7iE5FEzqj3F5lhPbbFwFcj"
        self.client = BinanceSpotWSClient(
            binance_url=BinanceUrl.WS,
            handler=handler,
            key=self.api_key,
            key_type=KeyType.HMAC,
            secret=self.api_secret,
            listen_key="E3vcnJBJGnDnNn4wjvQmM0BPBIipBH34Lh4Wl7dEakXM2CsLTUe20ibEZkLI",
            private_key_passphrase="your-secure-password",
            private_key="""
-----BEGIN ENCRYPTED PRIVATE KEY-----
MIGjMF8GCSqGSIb3DQEFDTBSMDEGCSqGSIb3DQEFDDAkBBCdhRl9oHlXZHyHeSdc
NkZ3AgIIADAMBggqhkiG9w0CCQUAMB0GCWCGSAFlAwQBKgQQma5Nvb9IAFcNOteb
EYRmsARABq2pMe4StSq6dAtgZrSq2V4vdFsU7GCxBjTcY1XbjJ7A84b5hSi6jmhG
Oo8PfGbOXze9/x756HgtuzEgrX9X2A==
-----END ENCRYPTED PRIVATE KEY-----
            """.strip()
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
        await self.client.order_book_api(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_recent_trades(self, mock_get):
        await self.client.recent_trades_api(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_historical_trades(self, mock_get):
        await self.client.historical_trades_api(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_get_api_v3_agg_trades(self, mock_get):
        await self.client.agg_trades_api(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_klines(self, mock_get):
        await self.client.klines_api(
            "BTCUSDT",
            Interval.MINUTE_1,
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_ui_klines(self, mock_get):
        await self.client.ui_klines_api(
            "BTCUSDT",
            Interval.MINUTE_1,
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_avg_price_api(self, mock_get):
        await self.client.avg_price_api(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_ticker_24hr_api(self, mock_get):
        await self.client.ticker_24hr_api(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_ticker_trading_day_api(self, mock_get):
        await self.client.ticker_trading_day_api(
            ["BTCUSDT", "BNBBTC"],
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_ticker_api(self, mock_get):
        await self.client.ticker_api(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_ticker_price_api(self, mock_get):
        await self.client.ticker_price_api(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_ticker_book_api(self, mock_get):
        await self.client.ticker_book_api(
            "BTCUSDT",
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_session_logon_api(self, mock_get):
        await self.client.session_logon_api(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_session_status_api(self, mock_get):
        await self.client.session_status_api(
            _id=1
        )
        await self.client.session_logon_api(
            _id=1
        )
        await self.client.session_status_api(
            _id=1
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_session_logout_api(self, mock_get):
        await self.client.session_status_api(
            _id=1
        )
        await self.client.session_logon_api(
            _id=2
        )
        await self.client.session_status_api(
            _id=3
        )
        await self.client.session_logout_api(
            _id=4
        )
        await self.client.session_status_api(
            _id=5
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_order_place_api(self, mock_get):
        await self.client.order_place_api(
            "BTCUSDT",
            "BUY",
            OrderType.LIMIT,
            price=0.1,
            quantity=10000,
            _id=1,
            sign=True,
            timeInForce="GTC"
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_order_test_api(self, mock_get):
        await self.client.order_test_api(
            "BTCUSDT",
            "BUY",
            OrderType.LIMIT,
            price=23416.10000000,
            quantity=0.00847000,
            _id=1,
            sign=True,
            timeInForce="GTC"
        )
        await self.client.connect()

    async def test_order_status_api(self):
        await self.client.order_status_api(
            "BTCUSDT",
            order_id=12569099453,
            sign=True
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_order_cancel_api(self, mock_get):
        await self.client.order_cancel_api(
            "BTCUSDT",
            order_id=12569099453,
            sign=True
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_order_cancel_replace_api(self, mock_get):
        await self.client.order_cancel_replace_api(
            "BTCUSDT",
            order_id=12569099453,
            price=23416.10000000,
            quantity=0.00847000,
            sign=True,
            timeInForce="GTC"
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_open_orders_status_api(self, mock_get):
        await self.client.open_orders_status_api(
            "BTCUSDT",
            sign=True
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_open_orders_cancel_all_api(self, mock_get):
        await self.client.open_orders_cancel_all_api(
            "BTCUSDT",
            sign=True
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_order_list_place_api(self, mock_get):
        await self.client.order_list_place_api(
            "BTCUSDT",
            "BUY",
            OrderType.LIMIT,
            price=0.1,
            quantity=10000,
            _id=1,
            sign=True,
            timeInForce="GTC"
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_order_place(self, mock_get):
        await self.client.order_place(
            "BTCUSDT",
            "BUY",
            OrderType.LIMIT,
            price=0.1,
            quantity=10000,
            _id=1,
            sign=True,
            timeInForce="GTC"
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_account_status_api(self, mock_get):
        await self.client.account_status_api(
            sign=True
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_rate_limit_order_api(self, mock_get):
        await self.client.rate_limit_order_api(
            sign=True
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_all_orders_api(self, mock_get):
        await self.client.all_orders_api(
            "BTCUSDT",
            sign=True
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_all_order_lists_api(self, mock_get):
        await self.client.all_order_lists_api(
            sign=True
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_my_trades_api(self, mock_get):
        await self.client.my_trades_api(
            "BTCUSDT",
            sign=True
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_my_prevented_matches_api(self, mock_get):
        await self.client.my_prevented_matches_api(
            "BTCUSDT",
            sign=True,
            orderId=35,
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_my_allocations_api(self, mock_get):
        await self.client.my_allocations_api(
            "BTCUSDT",
            sign=True,
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_account_commission_api(self, mock_get):
        await self.client.account_commission_api(
            "BTCUSDT",
            sign=True,
        )
        await self.client.connect()
