from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from nexus.binance.pm import PmTradingApi


class TestGeneralClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = ""
        self.api_secret = ""
        self.client = PmTradingApi(self.api_key, self.api_secret)

    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        await self.client.close_session()

    @patch('aiohttp.ClientSession.get')
    async def test_get_papi_v1_ping(self, mock_get):
        res = await self.client.get_papi_v1_ping()
        print(res)

    @patch('aiohttp.ClientSession.post')
    async def test_post_papi_v1_listen_key(self, mock_post):
        res = await self.client.post_papi_v1_listen_key()
        print(res)

    @patch('aiohttp.ClientSession.put')
    async def test_put_papi_v1_listen_key(self, mock_put):
        res = await self.client.put_papi_v1_listen_key()
        print(res)

    @patch('aiohttp.ClientSession.delete')
    async def test_delete_papi_v1_listen_key(self, mock_delete):
        res = await self.client.delete_papi_v1_listen_key()
        print(res)
