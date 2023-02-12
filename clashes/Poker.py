import sys
import math

mapping = {"A": 14, "K": 13, "Q": 12, "J": 11}


def to_numbers(hand):
    cards = hand.split()
    return [int(mapping[x]) if x in mapping else int(x) for x in cards]


def to_string(numbers):
    return [remap(x) for x in numbers]


def remap(x):
    for letter, value in mapping.items():
        if value == x:
            return letter
    return str(x)


def rank(hand):
    numbers = sorted(to_numbers(hand))

    counts = {}
    for card in numbers:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1

    # todo get highest card: max(stats.keys(), key=(lambda k: stats[k]))
    if len(counts) == 2:
        key, value = list(counts.items())[0]
        if value == 1 or value == 4:
            return 6  # four of a kind
        else:
            return 5  # full house
    elif len(counts) == 5:
        if numbers[4] - numbers[0] == 4:
            return 4  # straight
        else:
            return 0  # nothing
    elif len(counts) == 3:
        if max(counts.values()) == 3:
            return 3  # three of a kind
        else:
            return 2  # two pairs
    else:
        return 1  # one pair


# first_hand = input()
# second_hand = input()

a = "A K Q J 9"
b = "A K Q J J"
c = "A Q Q J J"
d = "A K J J J"
e = "A K Q J 10"
f = "Q Q Q J J"
g = "A K K K K"

print(rank(a))
print(rank(b))
print(rank(c))
print(rank(d))
print(rank(e))
print(rank(f))
print(rank(g))


