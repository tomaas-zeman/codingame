import sys
import math
import numpy
import random

GRID_X = 30
GRID_Y = 20
RANDOM_MOVE_TRIES = 100
FUTURE_STEPS = 50
FALLBACK_FUTURE_STEPS = 50


class Move:
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"
    
    @staticmethod
    def values():
        return [Move.LEFT, Move.RIGHT, Move.UP, Move.DOWN]
    
    @staticmethod
    def next_coord(x, y, move):
        if move == Move.LEFT:
            return x - 1, y
        elif move == Move.RIGHT:
            return x + 1, y
        elif move == Move.UP:
            return x, y - 1
        elif move == Move.DOWN:
            return x, y + 1


def pick_random_move(grid, current_x, current_y):
    for i in range(RANDOM_MOVE_TRIES):
        next_move = Move.values()[random.randint(0, 3)]
        if is_next_position_free(grid, current_x, current_y, next_move):
            return next_move
    return None


def is_next_position_free(grid, current_x, current_y, move):
    return (move == Move.LEFT and current_x != 0 and grid[current_x - 1][current_y] == 0) or \
           (move == Move.RIGHT and current_x != GRID_X - 1 and grid[current_x + 1][current_y] == 0) or \
           (move == Move.UP and current_y != 0 and grid[current_x][current_y - 1] == 0) or \
           (move == Move.DOWN and current_y != GRID_Y - 1 and grid[current_x][current_y + 1] == 0)


def future_looks_good(grid, current_x, current_y, move):
    if move is None:
        return False, 0

    grid_copy = numpy.copy(grid)

    next_x, next_y = Move.next_coord(current_x, current_y, move)
    grid_copy[next_x][next_y] = 1
    for i in range(FUTURE_STEPS):
        next_move = pick_random_move(grid_copy, next_x, next_y)

        if next_move is None:
            return False, i

        next_x, next_y = Move.next_coord(next_x, next_y, next_move)
        grid_copy[next_x][next_y] = 1

    return True, 0


# init grid
grid = numpy.zeros((GRID_X, GRID_Y))
while 1:
    number_of_players, my_player_number = [int(i) for i in input().split()]
    current_x = None
    current_y = None
    for player_number in range(number_of_players):
        start_x, start_y, last_x, last_y = [int(j) for j in input().split()]

        # fill occupied positions
        grid[start_x][start_y] = 1
        grid[last_x][last_y] = 1

        # set my position
        if player_number == my_player_number:
            current_x = last_x
            current_y = last_y

    # TODO: beware of close opponent head

    # pick random move and look into the future if it looks good
    # if not, try different random moves
    move = pick_random_move(grid, current_x, current_y)
    looks_good, steps = future_looks_good(grid, current_x, current_y, move)
    if looks_good:
        print(move)
    else:
        take_the_one_with_most_steps = True
        for i in range(FALLBACK_FUTURE_STEPS):
            fallback_move = pick_random_move(grid, current_x, current_y)
            fallback_looks_good, fallback_steps = future_looks_good(grid, current_x, current_y, fallback_move)
            if fallback_looks_good:
                print(fallback_move)
                take_the_one_with_most_steps = False # we have a winner here, no need to take some worse solution
                break
            elif fallback_steps > steps:
                steps = fallback_steps
                move = fallback_move
        if take_the_one_with_most_steps:
            print(move)