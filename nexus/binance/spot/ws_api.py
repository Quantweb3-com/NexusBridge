

async def subscribe_agg_trade(self, symbol: str):
    subscription_id = f"agg_trade.{symbol}"
    params = f"{symbol.lower()}@aggTrade"
    await self._subscribe(params, subscription_id)
