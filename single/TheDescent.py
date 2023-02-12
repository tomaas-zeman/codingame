import sys
import math


def position_of_highest(mountains):
    position = -1
    height = 0
    for i in range(len(mountains)):
        if mountains[i] > height:
            position = i
            height = mountains[i]

    return position


can_fire = True
last_position = 0
while 1:
    # first -> then <- then again -> ...
    # 0-7    10-1
    position, altitude = [int(i) for i in input().split()]
    mountains = []
    for i in range(8):
        mountains.append(int(input()))

    if last_position == position:
        can_fire = True

    if position == position_of_highest(mountains):
        print("FIRE")
        can_fire = False
    else:
        print("HOLD")
