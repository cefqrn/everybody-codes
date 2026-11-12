from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import batched, chain, count, cycle, islice, pairwise, combinations, product, takewhile, zip_longest
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

    for y, line in enumerate(s.splitlines()):
        for x, c in enumerate(line):
            grid[x, y] = c

        # digits = tuple(map(int, findall(r"\d+", line)))
        # grid.append(digits)
        # grid.append(line)

        # for x, c in enumerate(line):
        #     if c == ".":
        #         continue

        #     grid[x, y] = c

        ...

    return grid


def solve(data):

    result = 0

    print(data)

    outside = 0
    inside = 0

    for (x, y), c in data.items():
        # print(x, y, c)

        for dx, dy in directions:
            np = nx, ny = x+dx, y+dy

            inside += data.get(np) not in {None, c}
            outside += np not in data



        ...

    print(inside, outside)
    result = inside // 2 + outside

    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q14_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
