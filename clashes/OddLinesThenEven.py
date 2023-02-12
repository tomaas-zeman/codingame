import sys
import math

n = int(input())
lines = []
for i in range(n):
    lines.append(input())

for i in range(0, n, 2):
    print(lines[i])

for i in range(1, n, 2):
    print(lines[i])

