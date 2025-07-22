import orjson


# simple earn flexiable


async def get_api_v5_finance_savings_lending_rate_history(
    self,
    ccy: str | None = None,
    after: str | None = None,
    before: str | None = None,
    limit: str | None = None,
):
    """
    /api/v5/finance/savings/lending-rate-history

    https://www.okx.com/docs-v5/en/#financial-product-simple-earn-flexible-get-public-borrow-history-public
    """
    endpoint = "/api/v5/finance/savings/lending-rate-history"
    payload = {
        "ccy": ccy,
        "after": after,
        "before": before,
        "limit": limit,
    }

    payload = {k: str(v) for k, v in payload.items() if v is not None}
    raw = await self._fetch("GET", endpoint, payload=payload)
    return orjson.loads(raw)


async def get_api_v5_finance_savings_lending_rate_summary(
    self,
    ccy: str,
):
    """
    GET /api/v5/finance/savings/lending-rate-summary
    """
    endpoint = "/api/v5/finance/savings/lending-rate-summary"
    payload = {
        "ccy": ccy,
    }
    raw = await self._fetch("GET", endpoint, payload=payload)
    return orjson.loads(raw)
