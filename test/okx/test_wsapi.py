import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, AsyncMock

from nexus.okx.constants import OkxAccountType, ChannelKind
from nexus.okx.wsapi import OkxWSClient


class TestTradingAccountApiClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "305c4119-4911-4a22-8a07-2435eeac726a"
        self.api_secret = "221D78AFB68CB539865A11101D603CE7"
        self.passphrase = "@Or2452020438"

        def handler(msg):
            print(msg)

        self.client = OkxWSClient(
            OkxAccountType.DEMO,
            handler,
            secret=self.api_secret,
            api_key=self.api_key,
            passphrase=self.passphrase,
            channel_kind=ChannelKind.PUBLIC,
        )
    
    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        await self.client.disconnect()

    @patch('aiohttp.ClientSession.get')
    async def test_private_account_channel(self, mock_get):
        await self.client.private_account_channel(
            "subscribe",
            ccy="BTC",
            extraParams="{\"updateInterval\": \"1\"}"
        )
        await  self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_private_positions_channel(self, mock_get):
        await self.client.private_positions_channel(
            "subscribe",
            "FUTURES",
            instFamily="BTC-USD"
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_private_balance_and_position_channel(self, mock_get):
        await self.client.private_balance_and_position_channel(
            "subscribe",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_private_position_risk_warning(self, mock_get):
        await self.client.private_position_risk_warning(
            "subscribe",
            "ANY",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_private_account_greeks_channel(self, mock_get):
        await self.client.private_account_greeks_channel(
            "subscribe",
            ccy="BTC",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_private_order_channel(self, mock_get):
        await self.client.private_order_channel(
            "subscribe",
            "FUTURES",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_private_fills_channel(self, mock_get):
        await self.client.private_fills_channel(
            "subscribe",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_private_place_order(self, mock_get):
        await self.client.private_place_order(
            "BTC-USDT",
            "isolated",
            "buy",
            "market",
            "1",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_private_place_multiple_orders(self, mock_get):
        await self.client.private_place_multiple_orders(
            [
                {
                    "side": "buy",
                    "instId": "BTC-USDT",
                    "tdMode": "cash",
                    "ordType": "market",
                    "sz": "100"
                },
                {
                    "side": "buy",
                    "instId": "LTC-USDT",
                    "tdMode": "cash",
                    "ordType": "market",
                    "sz": "1"
                }
            ]
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_private_cancel_order(self, mock_get):
        await self.client.private_cancel_order(
            "BTC-USDT",
            "123456",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_private_cancel_multiple_orders(self, mock_get):
        await self.client.private_cancel_multiple_orders(
            [
                {
                    "instId": "BTC-USDT",
                    "ordId": "2517748157541376"
                },
                {
                    "instId": "LTC-USDT",
                    "ordId": "2517748157541376"
                }
            ]
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_private_amend_order(self, mock_get):
        await self.client.private_amend_order(
            "BTC-USDT",
            ordId="2510789768709120",
            newSz="2"
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_private_amend_multiple_orders(self, mock_get):
        await self.client.private_amend_multiple_orders(
            [
                {
                    "instId": "BTC-USDT",
                    "ordId": "2517748157541376",
                    "sz": "200"
                },
                {
                    "instId": "LTC-USDT",
                    "ordId": "2517748155771904",
                    "sz": "2"
                }
            ]
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_private_mass_cancel_orders(self, mock_get):
        await self.client.private_mass_cancel_order(
            "BTC-USDT",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_business_algo_orders_channel(self, mock_get):
        await self.client.business_algo_orders_channel(
            "subscribe",
            "FUTURES",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_business_advance_algo_orders_channel(self, mock_get):
        await self.client.business_advance_algo_orders_channel(
            "subscribe",
            "FUTURES",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_business_spot_grid_algo_orders_channel(self, mock_get):
        await self.client.business_spot_grid_algo_orders_channel(
            "subscribe",
            "SPOT",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_business_contract_grid_algo_orders_channel(self, mock_get):
        await self.client.business_contract_grid_algo_orders_channel(
            "subscribe",
            "FUTURES",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_business_grid_positions_channel(self, mock_get):
        await self.client.business_grid_positions_channel(
            "subscribe",
            "449327675342323712",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_business_grid_sub_orders_channel(self, mock_get):
        await self.client.business_grid_sub_orders_channel(
            "subscribe",
            "449327675342323712",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_business_recurring_buy_orders_channel(self, mock_get):
        await self.client.business_recurring_buy_orders_channel(
            "subscribe",
            "SPOT",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_business_copy_trading_notification_channel(self, mock_get):
        await self.client.business_copy_trading_notification_channel(
            "subscribe",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_business_lead_trading_notification_channel(self, mock_get):
        await self.client.business_lead_trading_notification_channel(
            "subscribe",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_business_candlesticks_channel(self, mock_get):
        await self.client.business_candlesticks_channel(
            "subscribe",
            "BTC-USDT",
            "candle1D",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_business_all_trades_channel(self, mock_get):
        await self.client.business_all_trades_channel(
            "subscribe",
            "BTC-USDT",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_business_mark_price_candlesticks_channel(self, mock_get):
        await self.client.business_mark_price_candlesticks_channel(
            "subscribe",
            "BTC-USD-190628",
            "mark-price-candle1D",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_business_index_candlesticks_channel(self, mock_get):
        await self.client.business_index_candlesticks_channel(
            "subscribe",
            "BTC-USD",
            "index-candle3M",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_business_economic_calendar_channel(self, mock_get):
        await self.client.business_economic_calendar_channel(
            "subscribe",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_tickers_channel(self, mock_get):
        await self.client.public_tickers_channel(
            "subscribe",
            "BTC-USDT",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_trades_channel(self, mock_get):
        await self.client.public_trades_channel(
            "subscribe",
            "BTC-USDT",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_order_book_channel(self, mock_get):
        await self.client.public_order_book_channel(
            "subscribe",
            "BTC-USDT",
            channel="books",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_option_trades_channel(self, mock_get):
        await self.client.public_option_trades_channel(
            "subscribe",
            instFamily="BTC-USD",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_call_auction_details_channel(self, mock_get):
        await self.client.public_call_auction_details_channel(
            "subscribe",
            "BTC-USDT",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_instruments_channel(self, mock_get):
        await self.client.public_instruments_channel(
            "subscribe",
            "SPOT",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_open_interest_channel(self, mock_get):
        await self.client.public_open_interest_channel(
            "subscribe",
            "LTC-USD-SWAP",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_funding_rate_channel(self, mock_get):
        await self.client.public_funding_rate_channel(
            "subscribe",
            "BTC-USD-SWAP",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_price_limit_channel(self, mock_get):
        await self.client.public_price_limit_channel(
            "subscribe",
            "BTC-USD-SWAP",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_option_summary_channel(self, mock_get):
        await self.client.public_option_summary_channel(
            "subscribe",
            "BTC-USD",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_public_estimated_delivery_price_channel(self, mock_get):
        await self.client.public_estimated_delivery_price_channel(
            "subscribe",
            "FUTURES",
            instFamily="BTC-USD",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_mark_price_channel(self, mock_get):
        await self.client.public_mark_price_channel(
            "subscribe",
            "LTC-USD-190628",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_index_tickers_channel(self, mock_get):
        await self.client.public_index_tickers_channel(
            "subscribe",
            "BTC-USD",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_liquidation_orders_channel(self, mock_get):
        await self.client.public_liquidation_orders_channel(
            "subscribe",
            "SWAP",
        )
        await self.client.connect()

    @patch('aiohttp.ClientSession.get')
    async def test_public_adl_warning_channel(self, mock_get):
        await self.client.public_adl_warning_channel(
            "subscribe",
            "SWAP",
            inst_family="BTC-USD",
        )
        await self.client.connect()
