# bitcoin-tx-tutorial

This repo contains a series of python jupyter-notebooks to explain how bitcoin transactions are created and signed. The notebooks will start up an instance of bitcoind in regtest mode so that transactions can be validated and broadcasted on regtest. Each notebook has some questions and exercises to test your understanding.

## Prerequisite knowledge
- A high level understanding of the bitcoin. e.g. [Mastering Bitcoin](https://github.com/bitcoinbook/bitcoinbook) by Andreas Antonopoulos UTXO model, in particular [Chapter 6](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch06.asciidoc).
- A conceptual understanding of [hash functions](https://www.thesslstore.com/blog/what-is-a-hash-function-in-cryptography-a-beginners-guide).
- [Hexadecimal notation](https://inst.eecs.berkeley.edu/~cs61bl/r//cur/bits/decimal-binary-hex.html?topic=lab28.topic&step=2&course=) and [endianness](https://www.freecodecamp.org/news/what-is-endianness-big-endian-vs-little-endian/).

## Chapters

+ Chapter 1: 'Legacy Transactions'
  - '[The First Bitcoin Transaction (Pay to Pubkey)](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/chapter1-legacy/first-btc-tx.ipynb)'
  - '[P2PKH - Pay to Pubkey Hash](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/chapter1-legacy/p2pkh.ipynb)'
  - '[P2SH - Pay to Script Hash (2-of-3 Mulitisig)](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/chapter1-legacy/p2sh-multisig.ipynb)'
+ Chapter 2: 'Segwit v0'
  - '[P2WPKH - Pay to Witness Pubkey Hash](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/chapter2-segwitv0/p2wpkh.ipynb)'
  - '[P2WSH - Pay to Witness Script Hash (2-of-2 Multisig)](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/chapter2-segwitv0/p2wsh-2-of-2-multisig.ipynb)'
+ Chapter 3: 'Taproot'
  - '[Schnorr signatures and TapTweaks](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/chapter3-taproot/schnorr-sig-and-taptweak.ipynb)'
  - '[TapTrees](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/chapter3-taproot/taproot-taptree.ipynb)'
  - '[P2TR - Key path and Script path spends](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/chapter3-taproot/p2tr-key-and-script-path.ipynb)'
+ Chapter 4: 'Signature hashes'
  - '[Signature hash evolution](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/chapter4-sighash/sighash-evolution.ipynb)'
  - '[Signature hash flags](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/chapter4-sighash/sighash-flags.ipynb)'
+ Chapter 5: 'Timelocks'
  - '[Transaction-level timelocks](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/chapter5-timelocks/transaction-level-timelocks.ipynb)'
  - '[Script-level timelocks](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/chapter5-timelocks/script-level-timelocks.ipynb)'
+ Appendix:
  - '[Elliptic Curve Math Review](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/appendix/elliptic_curve_math_review.ipynb)'
  - '[Hash Functions](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/appendix/hash-functions.ipynb)'
  - '[Bitcoin Script](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/appendix/bitcoin_script.ipynb)'
  - '[Addresses](https://github.com/DariusParvin/bitcoin-tx-tutorial/blob/main/appendix/addresses.ipynb)'

## Setup
This project requires Python 3.6 (or greater) to be [installed](https://www.python.org/downloads/) on your machine already. All other dependencies will be installed automatically with pip3.

To verify your Python version, run
```sh
python3 --version
```
If it is properly installed, you should see something like:
```sh
Python 3.9.13
```

To copy the repository to your local machine, it is recommended to use [`git`](https://git-scm.com/downloads) but alternatively you can also download the files directly from [GitHub](https://github.com/DariusParvin/bitcoin-tx-tutorial), there are no further dependencies on `git`.

```sh
git clone https://github.com/DariusParvin/bitcoin-tx-tutorial
cd bitcoin-tx-tutorial
```

To create a virtual environment and install all dependencies:
```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Finally, to launch the interactive notebook:
```sh
jupyter notebook
```

## Acknowledgements
- This work wouldn't have been possible without the funding from [chaincode](https://chaincode.com).
- A lot of the code and inspiration for this tutorial comes from the following places:
  - Shlomi Zeltsinger's [segwit tutorial](https://github.com/zeltsi/segwit_tutorial/tree/master/transactions)
  - Jimmy Song's [Programming Bitcoin exercises](https://github.com/jimmysong/pb-exercises).
  - Bitcoin Optech [Schnorr Taproot Workshop](https://bitcoinops.org/en/schorr-taproot-workshop/)
