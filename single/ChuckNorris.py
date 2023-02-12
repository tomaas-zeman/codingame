import sys
import math

message = input()
binary = ""
for c in message:
    tmp = str(bin(ord(c))[2:])
    tmp = "0"*(7-len(tmp)) + tmp
    binary += tmp
result = ""
seq_size = 0
seq_bit = None
for i in range(len(binary) + 1):
    if len(binary) == i:
        result += "{} {}".format("0" if seq_bit == "1" else "00", "0" * seq_size)
        break

    b = binary[i]
    if seq_bit is None:
        seq_bit = b
        seq_size += 1
    elif seq_bit == b:
        seq_size += 1
    else:
        result += "{} {} ".format("0" if seq_bit == "1" else "00", "0" * seq_size)
        seq_bit = b
        seq_size = 1

print(result)