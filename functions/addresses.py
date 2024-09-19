# Covered in addresses.ipynb
from functions.hashfunctions import *
from functions.script import *
import functions.bip_350_bech32_reference as b32
import base58
import ecdsa

def privkey_to_pubkey(privkey: bytes):
    '''Converts a private key (bytes) to a compressed pubkey (bytes)'''
    privkey = ecdsa.SigningKey.from_string(privkey, curve=ecdsa.SECP256k1) # Don't forget to specify the curve
    uncompressed_pubkey = privkey.get_verifying_key()

    x_cor = bytes.fromhex(uncompressed_pubkey.to_string().hex())[:32] # The first 32 bytes are the x coordinate
    y_cor = bytes.fromhex(uncompressed_pubkey.to_string().hex())[32:] # The last 32 bytes are the y coordinate
    if int.from_bytes(y_cor, byteorder="big", signed=True) % 2 == 0: # We need to turn the y_cor into a number.
        compressed_pubkey = bytes.fromhex("02") + x_cor
    else:
        compressed_pubkey = bytes.fromhex("03") + x_cor
    return compressed_pubkey

def privkey_to_wif(privkey, compressed_pubkey, testnet):
    '''
    Converts a private key (bytes) into a wallet import format
    https://en.bitcoin.it/wiki/Wallet_import_format
    '''
    if testnet:
        prefix = b"\xEF"
    else:
        prefix = b"\x80"
    # if the privkey will correspond to a compressed public key
    if compressed_pubkey:
        extended = prefix + privkey + b"\x01"
    else:
        extended = prefix + privkey
    return encode_base58_checksum(extended)


## Base58
def encode_base58_checksum(b: bytes):
    return base58.b58encode(b + hash256(b)[:4]).decode()

def decode_base58(s: str):
    return base58.b58decode(s)

# TODO
# def validate_checksum()

def pk_to_p2pkh(compressed: bytes, network: str):
    '''Creates a p2pkh address from a compressed pubkey'''
    pk_hash = hash160(compressed)
    if network == "regtest" or network == "testnet":
        prefix = bytes.fromhex("6f")
    elif network == "mainnet":
        prefix = bytes.fromhex("00")
    else:
        return "Enter the network: testnet/regtest/mainnet"
    return encode_base58_checksum(prefix + pk_hash)

def script_to_p2sh(redeemScript, network):
    '''Creates a p2sh base58 address corresponding to a redeemScript'''
    rs_hash = hash160(redeemScript)
    if network == "regtest" or network == "testnet":
        prefix = bytes.fromhex("c4")
    elif network == "mainnet":
        prefix = bytes.fromhex("05")
    else:
        return "Enter the network: tesnet/regtest/mainnet"
    return encode_base58_checksum(prefix + rs_hash)

# bech32/bech32m
def spk_to_bech32(spk, network):
    '''Creates a bech32 or bech32m address corresponding to a scriptPubkey'''
    version = spk[0] - 0x50 if spk[0] else 0
    program = spk[2:]
    if network == "testnet":
        prefix = 'tb'
    elif network == "regtest":
        prefix = 'bcrt'
    elif network == "mainnet":
        prefix = 'bc'
    else:
        return "Enter the network: testnet/regtest/mainnet"
    return b32.encode(prefix, version, program)

def bech32_to_spk(hrp, address):
    '''Decodes a bech32 or bech32m address to a scriptPubkey'''
    witver, witprog = b32.decode(hrp, address)
    pubkey_hash = bytearray(witprog)
    return (
        witver.to_bytes(1, byteorder="little", signed=False)
        + pushbytes(pubkey_hash)
    )

## Segwit
def pk_to_p2wpkh(compressed, network):
    '''Creates a p2wpkh bech32 address corresponding to a compressed pubkey'''
    pk_hash = hash160(compressed)
    spk = bytes.fromhex("0014") + pk_hash
    return spk_to_bech32(spk, network)

def script_to_p2wsh(redeemScript, network):
    '''Creates a p2wsh bech32 address corresponding to a redeemScript'''
    script_hash = hashlib.sha256(redeemScript).digest()
    spk = bytes.fromhex("0020") + script_hash
    return spk_to_bech32(spk, network)

def pk_to_p2sh_p2wpkh(compressed, network):
    pk_hash = hash160(compressed)
    redeemScript = bytes.fromhex("0014"+str(pk_hash.hex()))
    rs_hash = hash160(redeemScript)
    if network == "regtest" or network == "testnet":
        prefix = b"\xc4"
    elif network == "mainnet":
        prefix = b"\x05"
    else:
        return "Enter the network: tesnet/regtest/mainnet"
    return encode_base58_checksum(prefix + rs_hash)
