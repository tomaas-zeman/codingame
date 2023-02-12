import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

opponent_count = int(input())  # Opponent count

# game loop
while 1:
    game_round = int(input())
    # x: Your x position
    # y: Your y position
    # back_in_time_left: Remaining back in time
    x, y, back_in_time_left = [int(i) for i in input().split()]
    for i in range(opponent_count):
        # opponent_x: X position of the opponent
        # opponent_y: Y position of the opponent
        # opponent_back_in_time_left: Remaining back in time of the opponent
        opponent_x, opponent_y, opponent_back_in_time_left = [int(j) for j in input().split()]
    for i in range(20):
        line = input()  # One line of the map ('.' = free, '0' = you, otherwise the id of the opponent)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # action: "x y" to move or "BACK rounds" to go back in time
    print("17 10")
