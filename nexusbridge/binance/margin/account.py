async def get_sapi_v1_simpleEarn_flexible_list(
    self, asset: str | None = None, current: int | None = None, size: int | None = None
):
    """
    GET /sapi/v1/simple-earn/flexible/list

    Request Weight(IP)
    150

    Request Parameters
    Name	Type	Mandatory	Description
    asset	STRING	NO
    current	LONG	NO	Currently querying page. Start from 1. Default:1
    size	LONG	NO	Default:10, Max:100
    recvWindow	LONG	NO
    timestamp	LONG	YES
    """
    endpoint = "/sapi/v1/simple-earn/flexible/list"
    payload = {
        "asset": asset,
        "current": current,
        "size": size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_sapi_v1_simpleEarn_locked_list(
    self, asset: str | None = None, current: int | None = None, size: int | None = None
):
    """
    GET /sapi/v1/simple-earn/locked/list

    Request Weight(IP)
    150

    Request Parameters
    Name	Type	Mandatory	Description
    asset	STRING	NO
    current	LONG	NO	Currently querying page. Start from 1. Default:1
    size	LONG	NO	Default:10, Max:100
    recvWindow	LONG	NO
    timestamp	LONG	YES
    """

    endpoint = "/sapi/v1/simple-earn/locked/list"
    payload = {
        "asset": asset,
        "current": current,
        "size": size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw
