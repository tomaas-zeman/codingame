import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

numbers = []
words = []
number = ""
word = ""
for c in s:
    if c.isdigit():
        if len(word) != 0:
            numbers.append(int(number))
            words.append(word)
            number = ""
            word = ""
        number += c

    elif c.isalpha():
        word += c

numbers.append(int(number))
words.append(word)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

result = ""
for i in range(len(numbers)):
    result += words[i] * numbers[i]

print(result)
