import sys
import math

n = int(input())
for i in range(n):
    number = int(input())
    print("".join([str(x) for x in bin(number)[2:]]).replace("0", ".").replace("1", "-"))
