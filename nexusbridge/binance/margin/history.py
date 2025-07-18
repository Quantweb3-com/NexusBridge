from typing import Literal


async def get_sapi_v1_simpleEarn_flexible_history_rateHistory(
    self,
    productId: str,
    aprPeriod: str | None = None,
    startTime: int | None = None,
    endTime: int | None = None,
    current: int | None = None,
    size: int | None = None,
):
    """
    https://developers.binance.com/docs/simple_earn/history/Get-Rate-History
    """
    endpoint = "/sapi/v1/simple-earn/flexible/history/rateHistory"
    payload = {
        "productId": productId,
        "aprPeriod": aprPeriod,
        "startTime": startTime,
        "endTime": endTime,
        "current": current,
        "size": size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_sapi_v1_simpleEarn_flexible_history_rewardsRecord(
    self,
    type: Literal["Bonus", "REALTIME", "ALL"],
    productId: str | None = None,
    asset: str | None = None,
    startTime: int | None = None,
    endTime: int | None = None,
):
    """
    /sapi/v1/simple-earn/flexible/history/rewardsRecord
    """
    endpoint = "/sapi/v1/simple-earn/flexible/history/rewardsRecord"
    payload = {
        "type": type,
        "productId": productId,
        "asset": asset,
        "startTime": startTime,
        "endTime": endTime,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_sapi_v1_simpleEarn_locked_history_rewardsRecord(
    self,
    positionId: int | None = None,
    asset: str | None = None,
    startTime: int | None = None,
    endTime: int | None = None,
    current: int | None = None,
    size: int | None = None,
):
    """
    /sapi/v1/simple-earn/locked/history/rewardsRecord

    Request Weight(IP)
    150

    Request Parameters
    Name	Type	Mandatory	Description
    positionId	INT	NO
    asset	STRING	NO
    startTime	LONG	NO
    endTime	LONG	NO
    current	LONG	NO	Currently querying the page. Start from 1, Default:1, Max: 1,000
    size	LONG	NO	Default:10, Max:100
    recvWindow	LONG	NO
    timestamp	LONG	YES

    """
    endpoint = "/sapi/v1/simple-earn/locked/history/rewardsRecord"
    payload = {
        "positionId": positionId,
        "asset": asset,
        "startTime": startTime,
        "endTime": endTime,
        "current": current,
        "size": size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw
