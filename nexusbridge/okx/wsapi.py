import time
import hmac
import base64
import asyncio

from typing import Literal
from typing import Any
from typing import Callable
from typing import Dict
from aiolimiter import AsyncLimiter

from nexusbridge.base import WSClient
from nexusbridge.okx.constants import OkxAccountType, ChannelKind


class OkxWSClient(WSClient):
    def __init__(
        self,
        account_type: OkxAccountType,
        handler: Callable[..., Any],
        api_key: str = None,
        secret: str = None,
        passphrase: str = None,
        channel_kind: ChannelKind = ChannelKind.PUBLIC,
    ):
        self._api_key = api_key
        self._secret = secret
        self._passphrase = passphrase
        self._account_type = account_type
        self._channel_kind = channel_kind
        self._authed = False
        if channel_kind == ChannelKind.PRIVATE:
            url = f"{account_type.stream_url}/v5/private"
        elif channel_kind == ChannelKind.BUSINESS:
            url = f"{account_type.stream_url}/v5/business"
        else:
            url = f"{account_type.stream_url}/v5/public"

        super().__init__(
            url,
            limiter=AsyncLimiter(max_rate=2, time_period=1),
            handler=handler,
            specific_ping_msg=b"ping",
            ping_idle_timeout=5,
            ping_reply_timeout=2,
        )

    def _get_auth_payload(self):
        timestamp = int(time.time())
        message = str(timestamp) + "GET" + "/users/self/verify"
        mac = hmac.new(
            bytes(self._secret, encoding="utf8"),
            bytes(message, encoding="utf-8"),
            digestmod="sha256",
        )
        d = mac.digest()
        sign = base64.b64encode(d)
        if self._api_key is None or self._passphrase is None or self._secret is None:
            raise ValueError("API Key, Passphrase, or Secret is missing.")
        arg = {
            "apiKey": self._api_key,
            "passphrase": self._passphrase,
            "timestamp": timestamp,
            "sign": sign.decode("utf-8"),
        }
        payload = {"op": "login", "args": [arg]}
        return payload

    async def _auth(self):
        if not self._authed:
            await self._send(self._get_auth_payload())
            self._authed = True
            await asyncio.sleep(5)

    async def _submit(self, op: str, params: Dict[str, Any] | list[Dict[str, Any]]):
        await self._connect()
        await self._auth()

        payload = {
            "id": self._clock.timestamp_ms(),
            "op": op,
            "args": [params] if isinstance(params, dict) else params,
        }
        await self._send(payload)

    async def _subscribe(
        self, params: Dict[str, Any], subscription_id: str, auth: bool = False
    ):
        if subscription_id not in self._subscriptions:
            await self._connect()

            if auth:
                await self._auth()

            payload = {
                "op": "subscribe",
                "args": [params],
            }

            self._subscriptions[subscription_id] = payload
            await self._send(payload)
        else:
            print(f"Already subscribed to {subscription_id}")

    async def _unsubscribe(
        self, params: Dict[str, Any], subscription_id: str, auth: bool = False
    ):
        if subscription_id in self._subscriptions:
            await self.connect()

            if auth:
                await self._auth()

            payload = {
                "op": "unsubscribe",
                "args": [params],
            }

            del self._subscriptions[subscription_id]
            await self._send(payload)
        else:
            print(f"Subscription {subscription_id} not found")

    async def _resubscribe(self):
        if self._channel_kind == ChannelKind.PRIVATE:
            self._authed = False
            await self._auth()
        for _, payload in self._subscriptions.items():
            await self._send(payload)

    def check_channel_allowed(self, channel: ChannelKind):
        if not self._channel_kind == channel:
            raise ValueError(
                f"The method need {channel},but the client is set to {self._channel_kind}"
            )

    """
    Private Channels
    /ws/v5/private (required login)
    """

    async def private_account_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        channel: str = "account",
        **kwargs,
    ):
        self.check_channel_allowed(ChannelKind.PRIVATE)
        params = {
            "channel": channel,
            **kwargs,
        }
        if op == "subscribe":
            await self._subscribe(params, "account", auth=True)
        else:
            await self._unsubscribe(params, "account", auth=True)

    async def private_positions_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_type: Literal["MARGIN", "SWAP", "FUTURES", "OPTION", "ANY"],
        channel: str = "positions",
        **kwargs,
    ):
        self.check_channel_allowed(ChannelKind.PRIVATE)
        params = {
            "channel": channel,
            "instType": inst_type,
            **kwargs,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def private_balance_and_position_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        channel: str = "balance_and_position",
    ):
        self.check_channel_allowed(ChannelKind.PRIVATE)
        params = {
            "channel": channel,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def private_position_risk_warning(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_type: Literal["MARGIN", "SWAP", "FUTURES", "OPTION", "ANY"],
        channel: str = "liquidation-warning",
        **kwargs,
    ):
        self.check_channel_allowed(ChannelKind.PRIVATE)
        params = {
            "channel": channel,
            "instType": inst_type,
            **kwargs,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def private_account_greeks_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        channel: str = "account-greeks",
        ccy: str | None = None,
    ):
        self.check_channel_allowed(ChannelKind.PRIVATE)
        params = {
            "channel": channel,
        }
        if ccy:
            params["ccy"] = ccy
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def private_order_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_type: Literal["SPOT", "MARGIN", "SWAP", "FUTURES", "OPTION", "ANY"],
        channel: str = "orders",
        **kwargs,
    ):
        self.check_channel_allowed(ChannelKind.PRIVATE)
        params = {
            "channel": channel,
            "instType": inst_type,
            **kwargs,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, True)
        else:
            await self._unsubscribe(params, channel, True)

    async def private_fills_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        channel: str = "fills",
        inst_id: str | None = None,
    ):
        self.check_channel_allowed(ChannelKind.PRIVATE)
        params = {
            "channel": channel,
        }
        if inst_id:
            params["instId"] = inst_id
        if op == "subscribe":
            await self._subscribe(params, channel, True)
        else:
            await self._unsubscribe(params, channel, True)

    async def private_place_order(
        self,
        inst_id: str,
        td_mode: Literal["isolated", "cross", "cash", "spot_isolated"],
        side: Literal["buy", "sell"],
        ord_type: Literal[
            "market",
            "limit",
            "post_only",
            "fok",
            "ioc",
            "optimal_limit_ioc",
            "mmp",
            "mmp_and_post_only",
        ],
        sz: str,
        **kwargs,
    ):
        self.check_channel_allowed(ChannelKind.PRIVATE)
        params = {
            "instId": inst_id,
            "tdMode": td_mode,
            "side": side,
            "ordType": ord_type,
            "sz": sz,
            **kwargs,
        }
        await self._submit("order", params)

    async def private_place_multiple_orders(
        self, args: list[Dict[str, Any]], op: str = "batch-orders"
    ):
        self.check_channel_allowed(ChannelKind.PRIVATE)
        await self._submit(op, args)

    async def private_cancel_order(
        self, inst_id: str, ord_id: str | None = None, cl_ord_id: str | None = None
    ):
        self.check_channel_allowed(ChannelKind.PRIVATE)
        params = {
            "instId": inst_id,
        }
        if ord_id:
            params["ordId"] = ord_id
        if cl_ord_id:
            params["clOrdId"] = cl_ord_id
        await self._submit("cancel-order", params)

    async def private_cancel_multiple_orders(
        self,
        args: list[Dict[str, Any]],
        op: str = "batch-cancel-orders",
    ):
        self.check_channel_allowed(ChannelKind.PRIVATE)
        await self._submit(op, args)

    async def private_amend_order(
        self, inst_id: str, op: str = "amend-order", **kwargs
    ):
        self.check_channel_allowed(ChannelKind.PRIVATE)
        params = {
            "instId": inst_id,
            **kwargs,
        }
        await self._submit(op, params)

    async def private_amend_multiple_orders(
        self,
        args: list[Dict[str, Any]],
    ):
        self.check_channel_allowed(ChannelKind.PRIVATE)
        await self._submit("batch-amend-orders", args)

    async def private_mass_cancel_order(
        self,
        inst_family: str,
        inst_type: str = "OPTION",
        lock_interval: str | None = None,
    ):
        self.check_channel_allowed(ChannelKind.PRIVATE)
        params = {
            "instType": inst_type,
            "instFamily": inst_family,
        }
        if lock_interval:
            params["lockInterval"] = lock_interval
        await self._submit("mass-cancel", params)

    """
    Business Channels
    /ws/v5/business (required login)
    """

    async def business_algo_orders_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_type: Literal["MARGIN", "SWAP", "FUTURES", "OPTION", "ANY"],
        channel: str = "orders-algo",
        **kwargs,
    ):
        self.check_channel_allowed(ChannelKind.BUSINESS)
        params = {
            "channel": channel,
            "instType": inst_type,
            **kwargs,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def business_advance_algo_orders_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_type: Literal["MARGIN", "SWAP", "FUTURES", "OPTION", "ANY"],
        channel: str = "algo-advance",
        **kwargs,
    ):
        self.check_channel_allowed(ChannelKind.BUSINESS)
        params = {
            "channel": channel,
            "instType": inst_type,
            **kwargs,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def business_spot_grid_algo_orders_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_type: Literal["SPOT", "ANY"],
        channel: str = "grid-orders-spot",
        **kwargs,
    ):
        self.check_channel_allowed(ChannelKind.BUSINESS)
        params = {
            "channel": channel,
            "instType": inst_type,
            **kwargs,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def business_contract_grid_algo_orders_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_type: Literal["FUTURES", "SWAP", "ANY"],
        channel: str = "grid-orders-contract",
        **kwargs,
    ):
        self.check_channel_allowed(ChannelKind.BUSINESS)
        params = {
            "channel": channel,
            "instType": inst_type,
            **kwargs,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def business_grid_positions_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        algo_id: str,
        channel: str = "grid-positions",
    ):
        self.check_channel_allowed(ChannelKind.BUSINESS)
        params = {
            "channel": channel,
            "algoId": algo_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def business_grid_sub_orders_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        algo_id: str,
        channel: str = "grid-sub-orders",
    ):
        self.check_channel_allowed(ChannelKind.BUSINESS)
        params = {
            "channel": channel,
            "algoId": algo_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def business_recurring_buy_orders_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_type: Literal["SPOT", "ANY"],
        channel: str = "algo-recurring-buy",
        algo_id: str | None = None,
    ):
        self.check_channel_allowed(ChannelKind.BUSINESS)
        params = {
            "channel": channel,
            "instType": inst_type,
        }
        if algo_id:
            params["algoId"] = algo_id
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def business_copy_trading_notification_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        channel: str = "copytrading-notification",
        inst_type: str = "SWAP",
        inst_id: str | None = None,
    ):
        self.check_channel_allowed(ChannelKind.BUSINESS)
        params = {
            "channel": channel,
            "instType": inst_type,
        }
        if inst_id:
            params["instId"] = inst_id
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def business_lead_trading_notification_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        channel: str = "copytrading-lead-notification",
        inst_type: str = "SWAP",
        inst_id: str | None = None,
    ):
        self.check_channel_allowed(ChannelKind.BUSINESS)
        params = {
            "channel": channel,
            "instType": inst_type,
        }
        if inst_id:
            params["instId"] = inst_id
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def business_candlesticks_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_id: str,
        channel: str,
    ):
        self.check_channel_allowed(ChannelKind.BUSINESS)
        params = {
            "channel": channel,
            "instId": inst_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def business_all_trades_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_id: str,
        channel: str = "trades-all",
    ):
        self.check_channel_allowed(ChannelKind.BUSINESS)
        params = {
            "channel": channel,
            "instId": inst_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def business_mark_price_candlesticks_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_id: str,
        channel: str,
    ):
        self.check_channel_allowed(ChannelKind.BUSINESS)
        params = {
            "channel": channel,
            "instId": inst_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def business_index_candlesticks_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_id: str,
        channel: str,
    ):
        self.check_channel_allowed(ChannelKind.BUSINESS)
        params = {
            "channel": channel,
            "instId": inst_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    async def business_economic_calendar_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        channel: str = "economic-calendar",
    ):
        self.check_channel_allowed(ChannelKind.BUSINESS)
        params = {
            "channel": channel,
        }
        if op == "subscribe":
            await self._subscribe(params, channel, auth=True)
        else:
            await self._unsubscribe(params, channel, auth=True)

    """
    Public Channels
    /ws/v5/public
    """

    async def public_tickers_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_id: str,
        channel: str = "tickers",
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instId": inst_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)

    async def public_trades_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_id: str,
        channel: str = "trades",
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instId": inst_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)

    async def public_order_book_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_id: str,
        channel: Literal[
            "books", "books5", "bbo-tbt", "books50-l2-tbt", "books-l2-tbt"
        ],
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instId": inst_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)

    async def public_option_trades_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        channel: str = "option-trades",
        inst_type: str = "OPTION",
        **kwargs,
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instType": inst_type,
            **kwargs,
        }
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)

    async def public_call_auction_details_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_id: str,
        channel: str = "call-auction-details",
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instId": inst_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)

    async def public_instruments_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_type: Literal["SPOT", "MARGIN", "SWAP", "FUTURES", "OPTION", "ANY"],
        channel: str = "instruments",
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instType": inst_type,
        }
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)

    async def public_open_interest_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_id: str,
        channel: str = "open-interest",
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instId": inst_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)

    async def public_funding_rate_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_id: str,
        channel: str = "funding-rate",
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instId": inst_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)

    async def public_price_limit_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_id: str,
        channel: str = "price-limit",
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instId": inst_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)

    async def public_option_summary_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_family: str,
        channel: str = "opt-summary",
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instFamily": inst_family,
        }
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)

    async def public_estimated_delivery_price_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_type: Literal["OPTION", "FUTURES", "SWAP"],
        channel: str = "estimated-price",
        **kwargs,
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instType": inst_type,
            **kwargs,
        }
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)

    async def public_mark_price_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_id: str,
        channel: str = "mark-price",
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instId": inst_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)

    async def public_index_tickers_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_id: str,
        channel: str = "index-tickers",
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instId": inst_id,
        }
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)

    async def public_liquidation_orders_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_type: Literal["MARGIN", "SWAP", "FUTURES", "OPTION"],
        channel: str = "liquidation-orders",
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instType": inst_type,
        }
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)

    async def public_adl_warning_channel(
        self,
        op: Literal["subscribe", "unsubscribe"],
        inst_type: Literal["SWAP", "FUTURES", "OPTION"],
        channel: str = "adl-warning",
        inst_family: str | None = None,
    ):
        self.check_channel_allowed(ChannelKind.PUBLIC)
        params = {
            "channel": channel,
            "instType": inst_type,
        }
        if inst_family:
            params["instFamily"] = inst_family
        if op == "subscribe":
            await self._subscribe(params, channel)
        else:
            await self._unsubscribe(params, channel)
