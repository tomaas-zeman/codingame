import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.

# game loop
while 1:
    speed = int(input())  # the motorbike's speed.
    coord_x = int(input())  # the position on the road of the motorbike.

    if speed <= gap and coord_x < road + gap:
        print("SPEED")
    elif coord_x == road - 1:
        print("JUMP")
    elif coord_x >= road + gap:
        print("SLOW")
    elif speed > gap + 1:
        print("SLOW")
    else:
        print("WAIT")
