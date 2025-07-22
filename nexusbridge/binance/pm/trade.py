from typing import Literal

from nexusbridge.binance.constants import Side


async def post_papi_v1_um_order(
    self, symbol: str, side: Side, _type: Literal["LIMIT", "MARKET"], **kwargs
):
    endpoint = "/papi/v1/um/order"
    """
    Place new UM order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade
    """
    payload = {"symbol": symbol, "side": side.value, "type": _type, **kwargs}
    raw = await self._fetch(
        "POST",
        endpoint,
        payload=payload,
        signed=True,
    )
    return raw


async def post_papi_v1_um_conditional_order(
    self,
    symbol: str,
    side: Side,
    strategy_type: Literal[
        "STOP",
        "STOP_MARKET",
        "TAKE_PROFIT",
        "TAKE_PROFIT_MARKET",
        "TRAILING_STOP_MARKET",
    ],
    **kwargs,
):
    endpoint = "/papi/v1/um/conditional/order"
    """
    Place new UM conditional order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-UM-Conditional-Order
    """
    payload = {
        "symbol": symbol,
        "side": side.value,
        "strategyType": strategy_type,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_papi_v1_cm_order(
    self, symbol: str, side: Side, _type: Literal["LIMIT", "MARKET"], **kwargs
):
    endpoint = "/papi/v1/cm/order"
    """
    Place new CM order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-CM-Order
    """
    payload = {"symbol": symbol, "side": side.value, "type": _type, **kwargs}
    raw = await self._fetch(
        "POST",
        endpoint,
        payload=payload,
        signed=True,
    )
    return raw


async def post_papi_v1_cm_conditional_order(
    self,
    symbol: str,
    side: Side,
    strategy_type: Literal[
        "STOP",
        "STOP_MARKET",
        "TAKE_PROFIT",
        "TAKE_PROFIT_MARKET",
        "TRAILING_STOP_MARKET",
    ],
    **kwargs,
):
    endpoint = "/papi/v1/cm/conditional/order"
    """
    New CM Conditional Order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-CM-Conditional-Order
    """
    payload = {
        "symbol": symbol,
        "side": side.value,
        "strategyType": strategy_type,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def post_papi_v1_margin_order(
    self, symbol: str, side: Side, _type: Literal["LIMIT", "MARKET"], **kwargs
):
    endpoint = "/papi/v1/margin/order"
    """
    New Margin Order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-Margin-Order
    """
    payload = {"symbol": symbol, "side": side.value, "type": _type, **kwargs}
    raw = await self._fetch(
        "POST",
        endpoint,
        payload=payload,
        signed=True,
    )
    return raw


async def post_papi_v1_margin_loan(self, asset: str, amount: float, **kwargs):
    endpoint = "/papi/v1/marginLoan"
    """
    Apply for a loan
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-Borrow
    """
    payload = {"asset": asset, "amount": amount, **kwargs}
    raw = await self._fetch(
        "POST",
        endpoint,
        payload=payload,
        signed=True,
    )
    return raw


async def post_papi_v1_repay_loan(self, asset: str, amount: float, **kwargs):
    endpoint = "/papi/v1/repayLoan"
    """
    Repay for a margin loan.
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay
    """
    payload = {"asset": asset, "amount": amount, **kwargs}
    raw = await self._fetch(
        "POST",
        endpoint,
        payload=payload,
        signed=True,
    )
    return raw


async def post_papi_v1_margin_order_oco(
    self,
    symbol: str,
    side: Side,
    quantity: float,
    price: float,
    stop_price: float,
    **kwargs,
):
    endpoint = "/papi/v1/margin/order/oco"
    """
    New Margin OCO Order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-New-OCO
    """
    payload = {
        "symbol": symbol,
        "side": side.value,
        "quantity": quantity,
        "price": price,
        "stopPrice": stop_price,
        **kwargs,
    }
    raw = await self._fetch(
        "POST",
        endpoint,
        payload=payload,
        signed=True,
    )
    return raw


async def delete_papi_v1_um_order(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/um/order"
    """
    Cancel an active UM LIMIT order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-UM-Order
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_papi_v1_um_all_open_orders(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/um/allOpenOrders"
    """
    Cancel all active LIMIT orders on specific symbol
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Orders
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_papi_v1_um_conditional_order(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/um/conditional/order"
    """
    Cancel UM Conditional Order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_papi_v1_um_conditional_all_open_orders(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/um/conditional/allOpenOrders"
    """
    Cancel All UM Open Conditional Orders
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_papi_v1_cm_order(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/cm/order"
    """
    Cancel an active LIMIT order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-CM-Order
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_papi_v1_cm_all_open_orders(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/cm/allOpenOrders"
    """
    Cancel all active LIMIT orders on specific symbol
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Orders
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_papi_v1_cm_conditional_order(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/cm/conditional/order"
    """
    Cancel CM Conditional Order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-CM-Conditional-Order
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_papi_v1_cm_conditional_all_open_orders(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/cm/conditional/allOpenOrders"
    """
    Cancel All CM Open Conditional Orders
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Conditional-Orders
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_papi_v1_margin_order(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/margin/order"
    """
    Cancel Margin Account Order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-Margin-Account-Order
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_papi_v1_margin_orderList(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/margin/orderList"
    """
    Cancel Margin Account OCO Orders
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-Margin-Account-OCO-Orders
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def delete_papi_v1_margin_all_open_orders(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/margin/allOpenOrders"
    """
    Cancel Margin Account All Open Orders on a Symbol
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("DELETE", endpoint, payload=payload, signed=True)
    return raw


async def put_papi_v1_um_order(
    self, side: Side, symbol: str, quantity: float, **kwargs
):
    endpoint = "/papi/v1/um/order"
    """
    Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Modify-UM-Order
    """
    payload = {"symbol": symbol, "side": side.value, "quantity": quantity, **kwargs}
    raw = await self._fetch("PUT", endpoint, payload=payload, signed=True)
    return raw


async def put_papi_v1_cm_order(
    self, side: Side, symbol: str, quantity: float, price: float, **kwargs
):
    endpoint = "/papi/v1/cm/order"
    """
    Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Modify-CM-Order
    """
    payload = {
        "symbol": symbol,
        "side": side.value,
        "quantity": quantity,
        "price": price,
        **kwargs,
    }
    raw = await self._fetch("PUT", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_order(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/um/order"
    """
    Check an UM order's status.
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-UM-Order
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_all_orders(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/um/allOrders"
    """
    Get all account UM orders; active, canceled, or filled.
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_open_order(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/um/openOrder"
    """
    Query current UM open order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_open_orders(self, **kwargs):
    endpoint = "/papi/v1/um/openOrders"
    """
    Get all open orders on a symbol.
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_conditional_all_orders(self, **kwargs):
    endpoint = "/papi/v1/um/conditional/allOrders"
    """
    Query All UM Conditional Orders
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_conditional_open_orders(self, **kwargs):
    endpoint = "/papi/v1/um/conditional/openOrders"
    """
    Get all open conditional orders on a symbol.
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_conditional_open_order(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/um/conditional/openOrder"
    """
    Query Current UM Open Conditional Order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_conditional_order_history(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/um/conditional/orderHistory"
    """
    Query UM Conditional Order History
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-UM-Conditional-Order-History
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_order(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/cm/order"
    """
    Check an CM order's status.
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-CM-Order
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_all_orders(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/cm/allOrders"
    """
    Get all account CM orders; active, canceled, or filled.
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_open_order(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/cm/openOrder"
    """
    Query current CM open order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Order
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_open_orders(self, **kwargs):
    endpoint = "/papi/v1/cm/openOrders"
    """
    Get all open orders on a symbol.
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Current-CM-Open-Orders
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_conditional_open_orders(self, **kwargs):
    endpoint = "/papi/v1/cm/conditional/openOrders"
    """
    Get all open conditional orders on a symbol. Careful when accessing this with no symbol.
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Current-CM-Open-Conditional-Orders
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_conditional_open_order(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/cm/conditional/openOrder"
    """
    Query Current CM Open Conditional Order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Conditional-Order
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_conditional_all_orders(self, **kwargs):
    endpoint = "/papi/v1/cm/conditional/allOrders"
    """
    Query All CM Conditional Orders
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_conditional_order_history(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/cm/conditional/orderHistory"
    """
    Query CM Conditional Order History
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-CM-Conditional-Order-History
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_force_orders(self, **kwargs):
    endpoint = "/papi/v1/um/forceOrders"
    """
    Query User's UM Force Orders
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_force_orders(self, **kwargs):
    endpoint = "/papi/v1/cm/forceOrders"
    """
    Query User's CM Force Orders
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_order_amendment(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/um/orderAmendment"
    """
    Get order modification history
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-UM-Modify-Order-History
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_order_amendment(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/cm/orderAmendment"
    """
    Get order modification history
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-CM-Modify-Order-History
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_margin_force_orders(self, **kwargs):
    endpoint = "/papi/v1/margin/forceOrders"
    """
    Query user's margin force orders
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_user_trades(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/um/userTrades"
    """
    Get trades for a specific account and UM symbol.
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/UM-Account-Trade-List
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_user_trades(self, **kwargs):
    endpoint = "/papi/v1/cm/userTrades"
    """
    Get trades for a specific account and CM symbol.
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/CM-Account-Trade-List
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_adl_quantile(self, **kwargs):
    endpoint = "/papi/v1/um/adlQuantile"
    """
    Query UM Position ADL Quantile Estimation
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_cm_adl_quantile(self, **kwargs):
    endpoint = "/papi/v1/cm/adlQuantile"
    """
    Query CM Position ADL Quantile Estimation
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/CM-Position-ADL-Quantile-Estimation
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def post_papi_v1_um_feeBurn(self, fee_burn: Literal["true", "false"], **kwargs):
    endpoint = "/papi/v1/um/feeBurn"
    """
    Change user's BNB Fee Discount for UM Futures (Fee Discount On or Fee Discount Off ) on EVERY symbol
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade
    """
    payload = {"feeBurn": fee_burn, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_um_feeBurn(self, **kwargs):
    endpoint = "/papi/v1/um/feeBurn"
    """
    Get user's BNB Fee Discount for UM Futures (Fee Discount On or Fee Discount Off )
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_margin_order(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/margin/order"
    """
    Query Margin Account Order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-Order
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_margin_openOrders(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/margin/openOrders"
    """
    Query Current Margin Open Order
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-Margin-Open-Order
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_margin_all_open_orders(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/margin/allOrders"
    """
    Query All Margin Account Orders
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_margin_orderList(self, **kwargs):
    endpoint = "/papi/v1/margin/orderList"
    """
    Retrieves a specific OCO based on provided optional parameters
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_margin_all_orderList(self, **kwargs):
    endpoint = "/papi/v1/margin/allOrderList"
    """
    Query all OCO for a specific margin account based on provided optional parameters
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-all-OCO
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_margin_openOrderList(self, **kwargs):
    endpoint = "/papi/v1/margin/openOrderList"
    """
    Query Margin Account's Open OCO
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-Open-OCO
    """
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def get_papi_v1_margin_myTrades(self, symbol: str, **kwargs):
    endpoint = "/papi/v1/margin/myTrades"
    """
    Margin Account Trade List
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-Trade-List
    """
    payload = {"symbol": symbol, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return raw


async def post_papi_v1_margin_repay_debt(self, asset: str, **kwargs):
    endpoint = "/papi/v1/margin/repay-debt"
    """
    Repay debt for a margin loan.
    https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt
    """
    payload = {"asset": asset, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return raw
