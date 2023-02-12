import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
inputs = [int(x) for x in input().split()]
odd = []
even = []
for num in inputs:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

if len(odd) == 1:
    print(odd[0])
else:
    print(even[0])

