from test_framework.test_shell import TestShell
"""
Commonly used functions for setting up the notebooks.
setup_testshell - sets up the testshell on a clean chain and returns the TestNode
fund_address - funds an address with an amount of btc and returns the outpoint
"""

def setup_testshell():
    """Start up a testshell, create a wallet, and fund it with a mature coinbase transaction."""
    test = TestShell().setup(
        num_nodes=1,
        setup_clean_chain=True
    )
    node = test.nodes[0]

    # Create a new wallet and address that we can mine blocks so that we can fund our transactions
    node.createwallet(wallet_name='mywallet')
    mining_address = node.getnewaddress()

    # Generate 101 blocks so that the first block's block reward reaches maturity
    node.generatetoaddress(nblocks=101, address=mining_address, invalid_call=False)

    # Check that we were able to mine 101 blocks
    assert(node.getblockcount() == 101)

    return node


def get_utxo_index(node, address: str, txid: str) -> int:
    """Identify the output of a txid belonging to the address."""
    raw_tx = node.getrawtransaction(txid)
    decoded = node.decoderawtransaction(raw_tx)
    if decoded["vout"][0]["scriptPubKey"]["address"] == address:
        index = 0
    elif decoded["vout"][1]["scriptPubKey"]["address"] == address:
        index = 1
    else:
        raise Exception(f"couldn't find output with address {address}")
    return index


def fund_address(node, address: str, amount: float) -> (str, int):
    """Fund an address with an amount of btc and get back the outpoint."""
    txid = node.sendtoaddress(address, amount)
    index = get_utxo_index(node, address, txid)

    # Mine a block to confirm the tx
    mining_address = node.getnewaddress()
    node.generatetoaddress(nblocks=1, address=mining_address, invalid_call=False)

    return txid, index
