#!/usr/bin/env python3

import sys
import base64
from operator import xor
from Crypto.Util.number import *

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY4 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY5 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
KEY6 = "ENIT{x000r_i5_ass0c1at1v3}"

# Convert KEY6 to bytes and then to hexadecimal
KEY6_hex = bytes(KEY6, 'utf-8').hex()

KEY1_b = int(KEY1, 16)
KEY4_b = int(KEY4, 16)
KEY5_b = int(KEY5, 16)
KEY6_b = int(KEY6_hex, 16)

print(KEY6_b)

F = KEY6_b ^ KEY1_b ^ KEY5_b

F_hex = hex(F)
message = f"The flag F is: {F_hex}"
message_bytes = bytes.fromhex(F_hex[2:])
print(message_bytes.hex()) 
#message_bytes
#message = message_bytes.decode('utf-8')

#print(f"The flag message is: {message}")
