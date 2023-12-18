#!/usr/bin/env python3

import sys
import base64
from operator import xor
from Crypto.Util.number import *


# Original key
KEY6 = "ENIT{Br!ute_frce__15_my_f4v0ur173_by7e}"

# Convert the key to bytes and then to hexadecimal
KEY6_bytes = bytes(KEY6, 'utf-8')
KEY6_hex = KEY6_bytes.hex()

# XOR each byte with 0x10
xored_bytes = bytes([byte ^ 0xAB for byte in KEY6_bytes])

# Convert the result bytes to a new hex string
xored_hex_string = xored_bytes.hex()

print(f"Original KEY6 hex: {KEY6_hex}")
print(f"XOR value: 0xAB")
print(f"XOR result hex string: {xored_hex_string}")