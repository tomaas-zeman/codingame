import sys
import math
import string

letters = string.ascii_uppercase

width = int(input())
height = int(input())
text = input()

for i in range(height):
    row = input()
    line_to_print = ""
    for letter in text:
        try:
            index = letters.index(letter.upper())
            line_to_print += row[index*width:index*width+width]
        except ValueError:
            line_to_print += row[len(letters)*width:len(letters)*width+width]

    print(line_to_print)
