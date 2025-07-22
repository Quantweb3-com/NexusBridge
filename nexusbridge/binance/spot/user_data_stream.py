async def post_api_v3_user_data_stream(self):
    endpoint = "/api/v3/userDataStream"

    raw = await self._fetch("POST", endpoint, signed=False)
    return raw


async def put_api_v3_user_data_stream(self, listen_key: str):
    endpoint = "/api/v3/userDataStream"
    payload = {"listenKey": listen_key}

    raw = await self._fetch("PUT", endpoint, payload=payload, signed=False)
    return raw


async def delete_api_v3_user_data_stream(self, listen_key: str):
    endpoint = "/api/v3/userDataStream"
    payload = {"listenKey": listen_key}

    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=False)
    return raw
