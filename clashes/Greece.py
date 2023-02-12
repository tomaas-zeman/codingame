import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
result = [n]
while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n *= 3
        if n % 2 != 0:
            n += 1
    result.append(int(n))

print(" ".join([str(x) for x in result]))
