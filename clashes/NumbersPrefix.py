import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

operation, split_position, string = input().split()
split_position = int(split_position)
string = string

first_number = string[:split_position]
second_number = string[split_position:]

# To debug: print("Debug messages...", file=sys.stderr)
if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "/":
    print(first_number / second_number)
elif operation == "*":
    print(first_number * second_number)

