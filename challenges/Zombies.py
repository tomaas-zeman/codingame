import sys
import math


class Creature:
    def __init__(self, id, coord, step):
        self.id = id
        self.coord = coord
        self.step = step

    def __str__(self):
        return "[{0};{1}] Creature{2}".format(self.coord.x, self.coord.y, self.id)


class Human(Creature):
    def __init__(self, id, coord):
        Creature.__init__(self, id, coord, 1000)


class Zombie(Creature):
    def __init__(self, id, coord, next_coord):
        Creature.__init__(self, id, coord, 400)
        self.next_coord = next_coord

    def __str__(self):
        return "[{0};{1}] -> [{2};{3}] Zombie{4}".format(self.coord.x, self.coord.y, self.next_coord.x, self.next_coord.y, self.id)


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{0} {1}".format(int(self.x), int(self.y))

    def valid(self):
        return self.x >= 0 and self.y >= 0


class DistanceAndTargets:
    def __init__(self, distance, zombie, human):
        self.distance = distance
        self.zombie = zombie
        self.human = human


def count_distance(a, b):
    return math.sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2))


def get_target_and_distance(human, zombies):
    nearest_zombie = None
    nearest_distance = float("inf")
    for zombie in zombies:
        if nearest_zombie is None:
            nearest_zombie = zombie
            nearest_distance = count_distance(human.coord, zombie.coord)
            continue

        new_dist = count_distance(human.coord, zombie.coord)
        if new_dist < nearest_distance:
            nearest_zombie = zombie
            nearest_distance = new_dist
    return nearest_zombie, nearest_distance


def get_sorted_distances(zombies, humans):
    distances = []
    for human in humans:
        zombie, distance = get_target_and_distance(human, zombies)
        distances.append(DistanceAndTargets(distance, zombie, human))
    return sorted(distances, key=lambda o: o.distance)


def zombie_killed_coord(zombie, me):
    radius = 2000

    # 1 = regular, 2+ = better precision
    step_granularity = 1

    distance = count_distance(zombie.coord, me.coord)

    zombie_x_change_per_step = (zombie.next_coord.x - zombie.coord.x) / step_granularity
    zombie_y_change_per_step = (zombie.next_coord.y - zombie.coord.y) / step_granularity

    zombie_new_coord = zombie.coord
    while distance > radius:
        zombie_new_coord = Coord(zombie_new_coord.x + zombie_x_change_per_step, zombie_new_coord.y + zombie_y_change_per_step)
        radius += 1000 / step_granularity
        distance = count_distance(zombie_new_coord, me.coord)

    return zombie_new_coord


def i_can_make_it(target_coord, me, zombie, human):
    zombie_to_human = count_distance(human.coord, zombie.coord) / zombie.step
    me_to_target = count_distance(me.coord, target_coord) / me.step
    me_to_human = count_distance(me.coord, human.coord) / me.step
    return min(me_to_target, me_to_human) <= zombie_to_human


previous_zombie_count = None
target_coord = None
while 1:
    x, y = [int(i) for i in input().split()]
    me = Human(-1, Coord(x, y))

    humans = []
    for i in range(int(input())):
        id, x, y = [int(j) for j in input().split()]
        humans.append(Human(id, Coord(x, y)))

    zombies = []
    for i in range(int(input())):
        id, x, y, next_x, next_y = [int(j) for j in input().split()]
        zombies.append(Zombie(id, Coord(x, y), Coord(next_x, next_y)))

    zombie_count_changed = False
    if previous_zombie_count is None:
        previous_zombie_count = len(zombies)
    elif previous_zombie_count > len(zombies):
        previous_zombie_count = len(zombies)
        zombie_count_changed = True

    # get most dangerous zombie
    if zombie_count_changed or target_coord is None:
        zombies_from_humans_distances = get_sorted_distances(zombies, humans)
        for value in zombies_from_humans_distances:
            best_current_coord = zombie_killed_coord(value.zombie, me)
            if i_can_make_it(best_current_coord, me, value.zombie, value.human) and best_current_coord.valid():
                target_coord = best_current_coord
                break

        # if still None, go to the first zombie in the list and try to lure it to itself
        if target_coord is None:
            target_coord = zombies_from_humans_distances[0].zombie.coord

        print(str(target_coord))
    else:
        print(str(target_coord))
