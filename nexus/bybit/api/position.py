import orjson
from typing import Any, Dict



class PositionApi:
    
    def __init__(self, fetch_func: callable):
        self._fetch = fetch_func

    async def get_v5_position_list(
        self, category: str, **kwargs
    ) -> Dict[str, Any]:
        endpoint = "/v5/position/list"
        payload = {
            "category": category,
            **kwargs,
        }
        raw = await self._fetch("GET", self._base_url, endpoint, payload, signed=True)
        return orjson.loads(raw)
