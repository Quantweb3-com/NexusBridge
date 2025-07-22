import orjson
from typing import Any, Dict, Literal


async def get_v5_position_list(
    self, category: Literal["linear", "inverse", "option"], **kwargs
):
    """
    Get Position Info
    https://bybit-exchange.github.io/docs/v5/position
    """
    endpoint = "/v5/position/list"
    payload = {
        "category": category,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_position_set_leverage(
    self,
    category: Literal["linear", "inverse"],
    symbol: str,
    buy_leverage: str,
    sell_leverage: str,
):
    """
    Set Leverage
    https://bybit-exchange.github.io/docs/v5/position/leverage
    """
    endpoint = "/v5/position/set-leverage"
    payload = {
        "category": category,
        "symbol": symbol,
        "buyLeverage": buy_leverage,
        "sellLeverage": sell_leverage,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_position_switch_isolated(
    self,
    symbol: str,
    category: Literal["inverse", "linear"],
    trade_mode: Literal[0, 1],
    buy_leverage: str,
    sell_leverage: str,
):
    """
    Switch Cross/Isolated Margin
    https://bybit-exchange.github.io/docs/v5/position/cross-isolate
    """
    endpoint = "/v5/position/switch-isolated"
    payload = {
        "symbol": symbol,
        "category": category,
        "tradeMode": trade_mode,
        "buyLeverage": buy_leverage,
        "sellLeverage": sell_leverage,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_position_switch_mode(
    self, category: Literal["inverse", "linear"], mode: Literal[0, 3], **kwargs
):
    """
    Switch Position Mode
    https://bybit-exchange.github.io/docs/v5/position/position-mode
    """
    endpoint = "/v5/position/switch-mode"
    payload = {
        "category": category,
        "mode": mode,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_position_trading_stop(
    self,
    category: Literal["linear", "inverse"],
    symbol: str,
    position_idx: Literal[0, 1, 2],
    **kwargs,
):
    """
    Set Trading-Stop
    https://bybit-exchange.github.io/docs/v5/position/trading-stop
    """
    endpoint = "/v5/position/trading-stop"
    payload = {
        "category": category,
        "symbol": symbol,
        "positionIdx": position_idx,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_position_set_auto_add_margin(
    self,
    symbol: str,
    auto_add_margin: Literal[0, 1],
    position_idx: Literal[0, 1, 2] | None = None,
    category: str = "linear",
):
    """
    Set Auto Add Margin
    https://bybit-exchange.github.io/docs/v5/position/auto-add-margin
    """
    endpoint = "/v5/position/set-auto-add-margin"
    payload = {
        "symbol": symbol,
        "autoAddMargin": auto_add_margin,
        "category": category,
    }
    if position_idx:
        payload["positionIdx"] = position_idx
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_position_add_margin(
    self,
    category: Literal["linear", "inverse"],
    symbol: str,
    margin: str,
    position_idx: Literal[0, 1, 2] | None = None,
):
    """
    Add Or Reduce Margin
    https://bybit-exchange.github.io/docs/v5/position/manual-add-margin
    """
    endpoint = "/v5/position/add-margin"
    payload = {
        "symbol": symbol,
        "margin": margin,
        "category": category,
    }
    if position_idx:
        payload["positionIdx"] = position_idx
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def get_v5_position_closed_pnl(
    self, category: Literal["linear", "inverse"], **kwargs
):
    """
    Get Closed PnL
    https://bybit-exchange.github.io/docs/v5/position/close-pnl
    """
    endpoint = "/v5/position/closed-pnl"
    payload = {
        "category": category,
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_position_move_positions(
    self, from_uid: str, to_uid: str, _list: list[dict[str, Any]]
):
    """
    Move Position
    https://bybit-exchange.github.io/docs/v5/position/move-position
    """
    endpoint = "/v5/position/move-positions"
    payload = {
        "fromUid": from_uid,
        "toUid": to_uid,
        "list": _list,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def get_v5_position_move_history(self, **kwargs):
    """
    Get Move Position History
    https://bybit-exchange.github.io/docs/v5/position/move-position-history
    """
    endpoint = "/v5/position/move-history"
    payload = {
        **kwargs,
    }
    raw = await self._fetch("GET", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_position_confirm_pending_mmr(
    self,
    symbol: str,
    category: Literal["linear", "inverse"],
):
    """
    Confirm New Risk Limit
    https://bybit-exchange.github.io/docs/v5/position/confirm-mmr
    """
    endpoint = "/v5/position/confirm-pending-mmr"
    payload = {
        "symbol": symbol,
        "category": category,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_position_set_tpsl_mode(
    self,
    symbol: str,
    category: Literal["linear", "inverse"],
    tp_sl_mode: Literal["Full", "Partial"],
):
    """
    Set TP/SL Mode
    https://bybit-exchange.github.io/docs/v5/position/tpsl-mode
    """
    endpoint = "/v5/position/set-tpsl-mode"
    payload = {
        "symbol": symbol,
        "category": category,
        "tpSlMode": tp_sl_mode,
    }
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def post_v5_position_set_risk_limit(
    self,
    symbol: str,
    category: Literal["linear", "inverse"],
    risk_id: int,
    position_idx: Literal[0, 1, 2] | None = None,
):
    """
    Set Risk Limit
    https://bybit-exchange.github.io/docs/v5/position/set-risk-limit
    """
    endpoint = "/v5/position/set-risk-limit"
    payload = {
        "symbol": symbol,
        "category": category,
        "riskId": risk_id,
    }
    if position_idx:
        payload["positionIdx"] = position_idx
    raw = await self._fetch("POST", endpoint, payload, signed=True)
    return orjson.loads(raw)
