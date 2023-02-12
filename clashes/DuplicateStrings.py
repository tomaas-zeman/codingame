import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

words = input()

count = {}
for s in words:
    if not s.strip():
        continue
    if s in count:
        count[s] += 1
    else:
        count[s] = 1

max = 0
for key in count:
    if count[key] > max:
        max = count[key]

print(str(max))
