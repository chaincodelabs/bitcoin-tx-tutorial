# Covered in hash-functions.ipynb
import hashlib

def sha256(data: bytes) -> bytes:
    '''One round of SHA256'''
    return hashlib.sha256(data).digest()

def hash256(data: bytes) -> bytes:
    '''Two rounds of SHA256 (aka Hash256)'''
    hash_1 = sha256(data)
    hash_2 = sha256(hash_1)
    return hash_2

def hash160(data: bytes) -> bytes:
    '''sha256 followed by ripemd160'''
    hash_1 = hashlib.sha256(data).digest()
    hash_2 = hashlib.new('ripemd160', hash_1).digest()
    return hash_2
