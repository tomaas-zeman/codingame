import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

sort = reversed(sorted(num))
print(" ".join([str(x) for x in sort]))
