import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = [int(x) for x in input().split()]  # the n temperatures expressed as integers ranging from -273 to 5526

min = 0 if not temps else None
for t in temps:
    if min is None or \
            (t == 0) or \
            (min < 0 and 0 > t > min) or \
            (0 < t <= abs(min)):
        min = t

print(min)
