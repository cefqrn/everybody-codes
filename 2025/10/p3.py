# see p3_3.py for first working solution

from collections import defaultdict
from functools import partial
from itertools import combinations, pairwise, permutations, product, starmap
from operator import contains, eq
from math import inf


def parse(s):
    hiding_spots = set()
    sheep_positions = set()

    start = None

    y = 0
    for y, line in enumerate(s.splitlines()):
        print(y)
        for x, c in enumerate(line):
            if c == "S":
                sheep_positions.add((x,y))
            elif c == "#":
                hiding_spots.add((x,y))
            elif c == "D":
                start = x, y

    assert start

    return y, start, frozenset(sheep_positions), frozenset(hiding_spots)


def horse_moves():
    yield  2,  1
    yield  2, -1
    yield -2,  1
    yield -2, -1
    yield  1,  2
    yield  1, -2
    yield -1,  2
    yield -1, -2

from functools import cache


@cache
def sheep(board_height, dragon_position, sheep_positions: frozenset, hiding_spots: frozenset):
    if not sheep_positions:
        return 1

    result = 0
    for pos in sheep_positions:
        x, y = pos
        if y == board_height - 1:
            continue

        npos = nx, ny = x, y+1
        if npos == dragon_position and npos not in hiding_spots:
            continue

        new_positions = sheep_positions ^ {pos, npos}
        result += dragon((board_height, dragon_position, new_positions, hiding_spots))

    return result



@cache
def dragon(state):
    board_height, dragon_position, sheep_positions, hiding_spots = state
    if not sheep_positions:
        return 1

    x, y = dragon_position

    # dragon moves
    result = 0
    for dx, dy in horse_moves():
        npos = nx, ny = x+dx, y+dy
        next_positions = frozenset(sheep_positions - ({npos} if npos not in hiding_spots else set()))

        result += sheep(board_height, npos, next_positions, hiding_spots)

    return result


if __name__ == "__main__":
    with open("everybody_codes_e2025_q10_p3.txt") as f:
        data = parse(f.read().strip())

    print(sheep(*data))

