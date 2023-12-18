


#!/usr/bin/env python3

import sys
import base64
from operator import xor
from Crypto.Util.number import *

hex_string = "eee5e2ffd0e9d98adedfcef4cdd9c8cef4f49a9ef4c6d2f4cd9fdd9bded99a9c98f4c9d29cced6"

# Convert the hex string to bytes
original_bytes = bytes.fromhex(hex_string)

# Iterate over XOR values from 0 to 256
for xor_value in range(256):
    # Perform the XOR operation on each byte
    result_bytes = bytes([byte ^ xor_value for byte in original_bytes])
    
    # Check if the first character is 'c'
    if result_bytes[0] == 69:  # ASCII value for 'c'
        result_string = result_bytes.decode('utf-8', errors='replace')
        print(f"XOR Value: {xor_value}")
        print("Result String after XOR:", result_string)
        print("="*50)  # Separator for clarity
