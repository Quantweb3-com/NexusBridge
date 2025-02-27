from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from nexus.binance.constants import BinanceUrl
from nexus.binance.um import UmTradingApi


class TestGeneralClient(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """测试初始化，asyncSetUp 用于异步的初始化"""
        self.api_key = "ff61d44910aa178996c40382d77e2bb10996b4dc7df5a2a9c6e431944b500b48"
        self.api_secret = "4e93d727d6a5240e4986c997b7ec3d60a231143fa0c9c8cf4399c42ab22cfb24"
        self.client = UmTradingApi(self.api_key, self.api_secret, binance_url=BinanceUrl.TEST, )
        
    async def asyncTearDown(self):
        """测试结束，asyncTearDown 用于异步的结束"""
        await self.client.close_session()

    @patch('aiohttp.ClientSession.get')
    async def test_post_fapi_v1_listen_key(self, mock_get):
        # 执行异步 API 请求
        result = await self.client.post_fapi_v1_listen_key()
        print(result)

    @patch('aiohttp.ClientSession.put')
    async def test_put_fapi_v1_listen_key(self, mock_put):
        # 执行异步 API 请求
        result = await self.client.put_fapi_v1_listen_key()
        print(result)

    @patch('aiohttp.ClientSession.delete')
    async def test_delete_fapi_v1_listen_key(self, mock_delete):
        # 执行异步 API 请求
        result = await self.client.delete_fapi_v1_listen_key()
        print(result)
