import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
words = []
for i in range(n):
    words.append(input())

shift = 0
a = ""
b = ""
for i in range(n):
    a += words[i][i]
    b += words[i][n-i-1]

print(a + " " + b)
