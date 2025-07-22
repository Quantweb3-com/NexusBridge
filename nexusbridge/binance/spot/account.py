async def get_api_v3_account(self, **kwargs):
    """
    Get current account information.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/account-endpoints
    """
    endpoint = "/api/v3/account"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_api_v3_my_trades(self, symbol: str, **kwargs):
    """
    Get trades for a specific account and symbol.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/account-endpoints#account-trade-list-user_data
    """
    endpoint = "/api/v3/myTrades"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_api_v3_rate_limit_order(self, **kwargs):
    """
    Displays the user's unfilled order count for all intervals.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/account-endpoints#query-unfilled-order-count-user_data
    """
    endpoint = "/api/v3/rateLimit/order"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_api_v3_my_prevented_matches(self, symbol: str, **kwargs):
    """
    Displays the list of orders that were expired due to STP.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/account-endpoints#query-prevented-matches-user_data
    """
    endpoint = "/api/v3/myPreventedMatches"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_api_v3_my_allocations(self, symbol: str, **kwargs):
    """
    Retrieves allocations resulting from SOR order placement.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/account-endpoints#query-allocations-user_data
    """
    endpoint = "/api/v3/myAllocations"
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_api_v3_account_commission(self, symbol: str):
    """
    Get current account commission rates.
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/account-endpoints#query-commission-rates-user_data
    """
    endpoint = "/api/v3/account/commission"
    payload = {
        "symbol": symbol,
    }
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw
