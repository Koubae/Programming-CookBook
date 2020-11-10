import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value