# bitcoin-tx-tutorial

This repo contains a series of python jupyter-notebooks to explain how bitcoin transactions are created and signed. The notebooks will start up an instance of bitcoind in regtest mode so that transactions can be validated and broadcasted on regtest. Each notebook has some questions and exercises to test your understanding. 

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
- A lot of the code and inspiration for this tutorial comes from [Shlomi Zeltsinger](https://github.com/zeltsi), in particular his [segwit tutorial](https://github.com/zeltsi/segwit_tutorial/tree/master/transactions), and from Jimmy Song's [Programming Bitcoin book](https://github.com/jimmysong/programmingbitcoin).
