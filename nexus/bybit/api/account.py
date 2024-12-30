import orjson
from typing import Any, Dict


class AccountApi:
    def __init__(self, fetch_func: callable):
        self._fetch = fetch_func

    async def get_v5_account_wallet_balance(
        self, account_type: str, **kwargs
    ) -> Dict[str, Any]:
        endpoint = "/v5/account/wallet-balance"
        payload = {
            "accountType": account_type,
            **kwargs,
        }
        raw = await self._fetch("GET", self._base_url, endpoint, payload, signed=True)
        return orjson.loads(raw)
