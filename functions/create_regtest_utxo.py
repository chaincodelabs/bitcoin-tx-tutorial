# Starts up bitcoind in regtest mode and creates a spendable utxo (with 1 confirmation)
# for the given address and amount

import json
import os
import subprocess
import time

def setup_regtest_bitcoind() -> str:
    # Make sure bitcoind is not already running
    os.system("bitcoin-cli -regtest stop")
    time.sleep(2)

    # Delete any previous files to restart regtest
    os.system("rm -rfv $HOME/Library/Application\ Support/Bitcoin/regtest/")

    # Start up bitcoind in regtest mode
    os.system("bitcoind -regtest -daemon -fallbackfee=0.0002")
    time.sleep(1.5)

    # Create a new wallet and address that we can mine blocks so that we can fund our transactions
    wallet = subprocess.getoutput("bitcoin-cli -regtest createwallet mywallet")
    mining_address = subprocess.getoutput("bitcoin-cli -regtest getnewaddress")

    # Generate 101 blocks so that the first block's block reward reaches maturity
    result = subprocess.getoutput(f"bitcoin-cli -regtest generatetoaddress 101 {mining_address}")

    # Check that we were able to mine 101 blocks
    blockcount = subprocess.getoutput("bitcoin-cli -regtest getblockcount")
    assert(blockcount == "101")

    return mining_address

def fund_address(address: str, amount: float) -> str:
    txid = subprocess.getoutput(f"bitcoin-cli -regtest sendtoaddress {address} {amount}")
    return txid

def get_utxo_index(address: str, txid: str) -> int:
    raw_tx = subprocess.getoutput(f"bitcoin-cli -regtest getrawtransaction {txid}")
    decoded = subprocess.getoutput(f"bitcoin-cli -regtest decoderawtransaction {raw_tx}")
    d = json.loads(decoded)
    if d["vout"][0]["scriptPubKey"]["address"] == address:
        index = 0
    elif d["vout"][1]["scriptPubKey"]["address"] == address:
        index = 1
    else:
        raise Exception(f"couldn't find output with address {address}")
    return index

def create_regtest_utxo(address: str, amount: float) -> tuple([str, int]):
    mining_address = setup_regtest_bitcoind()
    txid = fund_address(address, amount)
    index = get_utxo_index(address, txid)

    # Mine a block to confirm the tx
    subprocess.getoutput(f"bitcoin-cli -regtest generatetoaddress 1 {mining_address}")

    return (txid, index)
