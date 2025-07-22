import orjson
from typing import Any, Dict, Literal


async def get_v5_asset_delivery_record(
    self, category: Literal["inverse", "linear", "option"], **kwargs
):
    """
    Query delivery records of Invese Futures, USDC Futures and Options, sorted by deliveryTime in descending order
    https://bybit-exchange.github.io/docs/v5/asset/delivery
    """
    endpoint = "/v5/asset/delivery-record"
    payload = {"category": category, **kwargs}
    raw = await self._fetch("GET", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_settlement_record(self, category: str = "linear", **kwargs):
    """
    Query session settlement records of USDC perpetual and futures
    https://bybit-exchange.github.io/docs/v5/asset/settlement
    """
    endpoint = "/v5/asset/settlement-record"
    payload = {"category": category, **kwargs}
    raw = await self._fetch("GET", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_exchange_order_record(self, **kwargs):
    """
    Get Coin Exchange Records
    https://bybit-exchange.github.io/docs/v5/asset/exchange
    """
    endpoint = "/v5/asset/exchange/order-record"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_coin_query_info(self, coin: str | None = None):
    """
    Query coin information, including chain information, withdraw and deposit status.
    https://bybit-exchange.github.io/docs/v5/asset/coin-info
    """
    endpoint = "/v5/asset/coin/query-info"
    payload = {}
    if coin:
        payload["coin"] = coin
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_transfer_query_sub_member_list(self):
    """
    Query the sub UIDs under a main UID. It returns up to 2000 sub accounts, if you need more, please call this endpoint.
    https://bybit-exchange.github.io/docs/v5/asset/sub-uid-list
    """
    endpoint = "/v5/asset/transfer/query-sub-member-list"
    raw = await self._fetch("GET", endpoint, signed=True)
    return orjson.loads(raw)


# Balances
async def get_v5_asset_transfer_query_asset_info(
    self, account_type: str = "SPOT", coin: str | None = None
):
    """
    Get Asset Info
    https://bybit-exchange.github.io/docs/v5/asset/balance/asset-info
    """
    endpoint = "/v5/asset/transfer/query-asset-info"
    payload = {"account_type": account_type}
    if coin:
        payload["coin"] = coin
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_transfer_query_account_coins_balance(
    self, account_type: str, **kwargs
):
    """
    Get All Coins Balance
    https://bybit-exchange.github.io/docs/v5/asset/balance/all-balance
    """
    endpoint = "/v5/asset/transfer/query-account-coins-balance"
    payload = {"account_type": account_type, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_transfer_query_account_coin_balance(
    self, account_type: str, coin: str, **kwargs
):
    """
    Get Single Coin Balance
    https://bybit-exchange.github.io/docs/v5/asset/balance/account-coin-balance
    """
    endpoint = "/v5/asset/transfer/query-account-coin-balance"
    payload = {"account_type": account_type, "coin": coin, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_withdraw_withdrawable_amount(self, coin: str):
    """
    Get Withdrawable Amount
    https://bybit-exchange.github.io/docs/v5/asset/balance/delay-amount
    """
    endpoint = "/v5/asset/withdraw/withdrawable-amount"
    payload = {"coin": coin}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


# Transfer
async def get_v5_asset_transfer_query_transfer_coin_list(
    self, from_account_type: str, to_account_type: str
):
    """
    Get Transferable Coin
    https://bybit-exchange.github.io/docs/v5/asset/transfer/transferable-coin
    """
    endpoint = "/v5/asset/transfer/query-transfer-coin-list"
    payload = {"fromAccountType": from_account_type, "toAccountType": to_account_type}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_v5_asset_transfer_inter_transfer(
    self,
    from_account_type: str,
    to_account_type: str,
    coin: str,
    transfer_id: str,
    amount: str,
):
    """
    Create Internal Transfer
    https://bybit-exchange.github.io/docs/v5/asset/transfer/create-inter-transfer
    """
    endpoint = "/v5/asset/transfer/inter-transfer"
    payload = {
        "fromAccountType": from_account_type,
        "toAccountType": to_account_type,
        "coin": coin,
        "transferId": transfer_id,
        "amount": amount,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_transfer_query_inter_transfer_list(self, **kwargs):
    """
    Get Internal Transfer Records
    https://bybit-exchange.github.io/docs/v5/asset/transfer/inter-transfer-list
    """
    endpoint = "/v5/asset/transfer/query-inter-transfer-list"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_v5_asset_transfer_universal_transfer(
    self,
    from_account_type: str,
    to_account_type: str,
    coin: str,
    amount: str,
    transfer_id: str,
    from_member_id: int,
    to_member_id: int,
):
    """
    Create Universal Transfer
    https://bybit-exchange.github.io/docs/v5/asset/transfer/unitransfer
    """
    endpoint = "/v5/asset/transfer/universal-transfer"
    payload = {
        "fromAccountType": from_account_type,
        "toAccountType": to_account_type,
        "coin": coin,
        "amount": amount,
        "transferId": transfer_id,
        "fromMemberId": from_member_id,
        "toMemberId": to_member_id,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_transfer_query_universal_transfer_list(self, **kwargs):
    """
    Get Universal Transfer Records
    https://bybit-exchange.github.io/docs/v5/asset/transfer/unitransfer-list
    """
    endpoint = "/v5/asset/transfer/query-universal-transfer-list"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


# Deposit
async def get_v5_asset_deposit_query_allowed_list(self, **kwargs):
    """
    Get Allowed Deposit Coin Info
    https://bybit-exchange.github.io/docs/v5/asset/deposit/deposit-coin-spec
    """
    endpoint = "/v5/asset/deposit/query-allowed-list"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_v5_asset_deposit_to_account(
    self, account_type: Literal["UNIFIED", "SPOT", "CONTRACT", "FUND"]
):
    """
    Set Deposit Account
    https://bybit-exchange.github.io/docs/v5/asset/deposit/set-deposit-acct
    """
    endpoint = "/v5/asset/deposit/deposit-to-account"
    payload = {"accountType": account_type}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_deposit_query_record(self, **kwargs):
    """
    Get Deposit Records (on-chain)
    https://bybit-exchange.github.io/docs/v5/asset/deposit/deposit-record
    """
    endpoint = "/v5/asset/deposit/query-record"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_deposit_query_sub_member_record(
    self, sub_member_id: int, **kwargs
):
    """
    Get Sub Deposit Records (on-chain)
    https://bybit-exchange.github.io/docs/v5/asset/deposit/sub-deposit-record
    """
    endpoint = "/v5/asset/deposit/query-sub-member-record"
    payload = {"subMemberId": sub_member_id, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_deposit_query_internal_record(self, **kwargs):
    """
    Get Internal Deposit Records (off-chain)
    https://bybit-exchange.github.io/docs/v5/asset/deposit/internal-deposit-record
    """
    endpoint = "/v5/asset/deposit/query-internal-record"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_deposit_query_address(
    self, coin: str, chain_type: str | None = None
):
    """
    Get Master Deposit Address
    https://bybit-exchange.github.io/docs/v5/asset/deposit/master-deposit-addr
    """
    endpoint = "/v5/asset/deposit/query-address"
    payload = {
        "coin": coin,
    }
    if chain_type:
        payload["chainType"] = chain_type
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_deposit_query_sub_member_address(
    self, coin: str, chain_type: str, sub_member_id: int
):
    """
    Get Sub Deposit Address
    https://bybit-exchange.github.io/docs/v5/asset/deposit/sub-deposit-addr#http-request
    """
    endpoint = "/v5/asset/deposit/query-sub-member-address"
    payload = {"coin": coin, "subMemberId": sub_member_id, "chainType": chain_type}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


# Withdraw
async def get_v5_asset_withdraw_query_record(self, **kwargs):
    """
    Get Withdrawal Records
    https://bybit-exchange.github.io/docs/v5/asset/withdraw/withdraw-record
    """
    endpoint = "/v5/asset/withdraw/query-record"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_withdraw_query_vasp_list(
    self,
):
    """
    This endpoint is particularly used for kyc=KOR users. When withdraw funds, you need to fill entity id.
    https://bybit-exchange.github.io/docs/v5/asset/withdraw/vasp-list
    """
    endpoint = "/v5/asset/withdraw/vasp/list"
    raw = await self._fetch("GET", endpoint, signed=True)
    return orjson.loads(raw)


async def post_v5_asset_withdraw_create(
    self, address: str, amount: str, timestamp: int, **kwargs
):
    """
    Withdraw assets from your Bybit account. You can make an off-chain transfer if the target wallet address is from Bybit. This means that no blockchain fee will be charged.
    https://bybit-exchange.github.io/docs/v5/asset/withdraw
    """
    endpoint = "/v5/asset/withdraw/create"
    payload = {"address": address, "amount": amount, "timestamp": timestamp, **kwargs}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_v5_asset_withdraw_cancel(
    self,
    _id: str,
):
    """
    Cancel the withdrawal
    https://bybit-exchange.github.io/docs/v5/asset/withdraw/cancel-withdraw
    """
    endpoint = "/v5/asset/withdraw/cancel"
    payload = {"id": _id}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


# Convert
async def get_v5_asset_exchange_query_coin_list(
    self,
    account_type: Literal[
        "eb_convert_funding",
        "eb_convert_uta",
        "eb_convert_spot",
        "eb_convert_contract",
        "eb_convert_inverse",
    ],
    **kwargs,
):
    """
    Get Convert Coin List
    https://bybit-exchange.github.io/docs/v5/asset/convert/convert-coin-list
    """
    endpoint = "/v5/asset/exchange/query-coin-list"
    payload = {"accountType": account_type, **kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_v5_asset_exchange_quote_apply(
    self,
    from_coin: str,
    to_coin: str,
    request_coin: str,
    request_amount: str,
    account_type: str,
    **kwargs,
):
    """
    Request a Quote
    https://bybit-exchange.github.io/docs/v5/asset/convert/apply-quote
    """
    endpoint = "/v5/asset/exchange/quote-apply"
    payload = {
        "fromCoin": from_coin,
        "toCoin": to_coin,
        "requestCoin": request_coin,
        "requestAmount": request_amount,
        "accountType": account_type,
        **kwargs,
    }
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def post_v5_asset_exchange_convert_execute(
    self,
    quote_tx_id: str,
):
    """
    Confirm a Quote
    https://bybit-exchange.github.io/docs/v5/asset/convert/confirm-quote
    """
    endpoint = "/v5/asset/exchange/convert-execute"
    payload = {"quoteTxId": quote_tx_id}
    raw = await self._fetch("POST", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_exchange_convert_result_query(
    self, quote_tx_id: str, account_type: str
):
    """
    You can query the exchange result by sending quoteTxId. Make sure you input correct account type and quoteTxId, otherwise you cannot find it.
    https://bybit-exchange.github.io/docs/v5/asset/convert/get-convert-result
    """
    endpoint = "/v5/asset/exchange/convert-result-query"
    payload = {"quoteTxId": quote_tx_id, "accountType": account_type}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)


async def get_v5_asset_exchange_query_convert_history(self, **kwargs):
    """
    Get Convert history
    https://bybit-exchange.github.io/docs/v5/asset/convert/get-convert-history
    """
    endpoint = "/v5/asset/exchange/query-convert-history"
    payload = {**kwargs}
    raw = await self._fetch("GET", endpoint, payload=payload, signed=True)
    return orjson.loads(raw)
