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
    for y, line in enumerate(b:=s.splitlines()):
        for x, c in enumerate(line):
            if c == "S":
                sheep_positions.add((x,y))
            elif c == "#":
                hiding_spots.add((x,y))
            elif c == "D":
                start = x, y

    assert start

    return (len(line), len(b)), start, frozenset(sheep_positions), frozenset(hiding_spots)


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


def solve(parsed_input):
    (w, h), dragon_position, sheep_positions, hiding_spots = parsed_input

    @cache
    def sheep(dragon_position, sheep_positions: frozenset):
        if not sheep_positions:
            return 1

        result = 0
        all_skipped = True
        for pos in sheep_positions:
            x, y = pos

            npos = nx, ny = x, y+1
            if npos == dragon_position and npos not in hiding_spots:
                continue

            all_skipped = False

            if y == h - 1:
                continue

            new_positions = sheep_positions ^ {pos, npos}
            result += dragon(dragon_position, new_positions)

        if all_skipped:
            result += dragon(dragon_position, sheep_positions)

        return result

    W, H = range(w), range(h)

    @cache
    def dragon(dragon_position, sheep_positions):
        x, y = dragon_position

        # dragon moves
        result = 0
        for dx, dy in horse_moves():
            npos = nx, ny = x+dx, y+dy
            if nx not in W or ny not in H:
                continue

            next_positions = frozenset(sheep_positions - ({npos} if npos not in hiding_spots else set()))

            result += sheep(npos, next_positions)

        return result

    return sheep(dragon_position, sheep_positions)


if __name__ == "__main__":
    with open("everybody_codes_e2025_q10_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))

