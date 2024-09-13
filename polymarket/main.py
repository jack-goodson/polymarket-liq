from py_clob_client.client import ClobClient
from py_clob_client.clob_types import BookParams


def connect():
    host: str = "wss://ws-subscriptions-clob.polymarket.com/ws/"
    key: str = "0x2be414a2d942d9efa85f4397d5d4581d7b9225325069d84a740b992b5035b9b9"
    chain_id: int = 137

    ### Initialization of a client that trades directly from an EOA
    client = ClobClient(host, key=key, chain_id=chain_id)

    return client

client = connect()

creds = client.create_api_key()

resp = client.get_prices(
    params=[
        BookParams(
            token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563",
            side="BUY",
        )
    ]
)

print(resp)


