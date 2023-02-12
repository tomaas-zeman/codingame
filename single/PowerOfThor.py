import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

dist_x = light_x - initial_tx
dist_y = light_y - initial_ty

min = min(abs(dist_x), abs(dist_y))
rest = max(abs(dist_x), abs(dist_y)) - min

diagonal = ""
if dist_y < 0:
    diagonal += "N"
elif dist_y > 0:
    diagonal += "S"
if dist_x < 0:
    diagonal += "W"
elif dist_x > 0:
    diagonal += "E"

perpendicular = ""
if min == abs(dist_x):
    perpendicular = "S" if dist_y > 0 else "N"
else:
    perpendicular = "W" if dist_x < 0 else "E"

directions = [diagonal] * min
directions += [perpendicular] * rest

counter = 0
while 1:
    remaining_turns = int(input())
    print(directions[counter])
    counter += 1