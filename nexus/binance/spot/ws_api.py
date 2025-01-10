

async def subscribe_agg_trade(self, symbol: str):
    subscription_id = f"agg_trade.{symbol}"
    params = f"{symbol.lower()}@aggTrade"
    await self._subscribe(params, subscription_id)

async def subscribe_trade(self, symbol: str):
    subscription_id = f"trade.{symbol}"
    params = f"{symbol.lower()}@trade"
    await self._subscribe(params, subscription_id)
