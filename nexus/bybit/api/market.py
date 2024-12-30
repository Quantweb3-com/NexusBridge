import orjson
from typing import Any, Dict, Callable

class MarketApi:
    def __init__(self, fetch_func: Callable):
        self._fetch = fetch_func
    
    async def get_v5_market_time(self) -> Dict[str, Any]:
        """
        https://bybit-exchange.github.io/docs/v5/market/time
        """
        endpoint = "/v5/market/time"
        raw = await self._fetch("GET", endpoint)
        return orjson.loads(raw)
