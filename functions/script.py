# From Bitcoin script.ipynb
def varint_len(data: bytes):
    '''returns the length of the input as a variable integer'''
    l = len(data)
    if l < int('fd',16):
        varint = l.to_bytes(1, byteorder="little", signed=False)
    elif l < int('ffff',16):
        varint = bytes.fromhex("fd") + l.to_bytes(2, byteorder="little", signed=False)
    else:
        raise Exception("This function only handles up to 0xffff bytes")
    return varint

def pushbytes(data: bytes):
    '''prepends the length of the input in bytes.
    Used for adding OP_PUSHBYTES in bitcoin script where stack items can be of arbitrary length.
    see BIP62
    '''
    l = len(data)
    if l <= 76:
        pushbytes = l.to_bytes(1, byteorder="little", signed=False)
    elif l <= 255:
        pushbytes = bytes.fromhex("4c") + l.to_bytes(1, byteorder="little", signed=False)
    elif l <= 520:
        pushbytes = bytes.fromhex("4d") + l.to_bytes(2, byteorder="little", signed=False)
    else:
        raise Exception("This function only handles up to 520 bytes")
    return pushbytes + data
