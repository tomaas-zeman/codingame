import sys
import math


def process(line):
    result = ""
    print_whitespaces = False
    for char in line:
        if char.isspace():
            if print_whitespaces:
                result += char
        else:
            if char == "'":
                print_whitespaces = not print_whitespaces
            result += char
    return result


n = int(input())
result = ""

for i in range(n):
    line = input()
    result += process(line)

print(result)
