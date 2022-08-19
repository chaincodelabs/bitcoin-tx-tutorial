# Covered in hash-functions.ipynb
import hashlib

def hash256(data: bytes):
    '''Two rounds of SHA256 (aka Hash256)'''
    hash_1 = hashlib.sha256(data).digest()
    hash_2 = hashlib.sha256(hash_1).digest()
    return hash_2

def hash160(data: bytes):
    '''sha256 followed by ripemd160'''
    hash_1 = hashlib.sha256(data).digest()
    hash_2 = hashlib.new('ripemd160', hash_1).digest()
    return hash_2
