# Starts up bitcoind in regtest mode and creates a spendable utxo (with 1 confirmation)
# for the given address and amount

import json
import os
import subprocess
import time

CLI = "bitcoin-cli -regtest"

def setup_regtest_bitcoind() -> str:
    # Make sure bitcoind is not already running
    os.system(f"{CLI} stop")
    time.sleep(2)

    # Delete any previous files to restart regtest
    os.system("rm -rfv $HOME/Library/Application\ Support/Bitcoin/regtest/")

    # Start up bitcoind in regtest mode
    os.system("bitcoind -regtest -daemon -fallbackfee=0.0002")
    time.sleep(1.5)

    # Create a new wallet and address that we can mine blocks so that we can fund our transactions
    wallet = subprocess.getoutput(f"{CLI} createwallet mywallet")
    mining_address = subprocess.getoutput(f"{CLI} getnewaddress")

    # Generate 101 blocks so that the first block's block reward reaches maturity
    result = subprocess.getoutput(f"{CLI} generatetoaddress 101 {mining_address}")

    # Check that we were able to mine 101 blocks
    blockcount = subprocess.getoutput(f"{CLI} getblockcount")
    assert(blockcount == "101")

    return

def get_utxo_index(address: str, txid: str) -> int:
    raw_tx = subprocess.getoutput(f"{CLI} getrawtransaction {txid}")
    decoded = subprocess.getoutput(f"{CLI} decoderawtransaction {raw_tx}")
    d = json.loads(decoded)
    if d["vout"][0]["scriptPubKey"]["address"] == address:
        index = 0
    elif d["vout"][1]["scriptPubKey"]["address"] == address:
        index = 1
    else:
        raise Exception(f"couldn't find output with address {address}")
    return index

def fund_address(address: str, amount: float) -> (str, int):
    txid = subprocess.getoutput(f"{CLI} sendtoaddress {address} {amount}")
    index = get_utxo_index(address, txid)

    # Mine a block to confirm the tx
    subprocess.getoutput(f"{CLI} generate 1")

    return txid, index