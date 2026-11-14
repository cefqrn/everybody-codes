from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
# from itertools import batched, chain, count, cycle, islice, pairwise, combinations, product, takewhile, zip_longest
from heapq import heappop, heappush
from math import comb, inf
from operator import itemgetter, mul
from re import findall
from typing import NamedTuple

directions = ()
directions += ( 0,  1), ( 1,  0), ( 0, -1), (-1,  0)
# directions += ( 1,  1), ( 1, -1), (-1, -1), (-1,  1)


def parse(s):

    grid = {}
    # grid = []

    required = set()

    for y, line in enumerate(s.splitlines()):

        # digits = tuple(map(int, findall(r"\d+", line)))
        # grid.append(digits)
        # grid.append(line)

        for x, c in enumerate(line):
            if c == "S":
                start = x, y
            if c == "E":
                end = x, y
            if c == "@":
                required.add((x, y))


            grid[x, y] = c

        ...

    return grid, start, end, required


def solve(data):

    result = 0

    grid, start, end, needed = data

    print(data)

    states_seen = set()
    left = deque([(0, (1, 0), (start), 0)])

    while left:
        t, direction, pos, seen = left.popleft()
        print(t, seen)

        if grid.get(pos, "#") == "#":
            continue

        if pos in needed:
            seen += 1

        if pos == end:
            if seen >= 2026:
                result = t
                break

            continue

        state = direction, pos, seen
        if state in states_seen: continue
        states_seen.add(state)

        dx, dy = direction
        x, y = pos
        for dx, dy in direction, (-dy, dx), (dy, -dx):
            npos = nx, ny = x+dx, y+dy
            nstate = t+1, (dx, dy), npos, seen

            left.append(nstate)
    else:
        raise ValueError


    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q15_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
