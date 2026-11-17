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

        # digits = tuple(map(int, findall(r"\d+", line)))
        # grid.append(digits)
        # grid.append(line)

        for x, c in enumerate(line):
            if c == ".":
                continue

            grid[x, y] = c

        ...

    return grid


def solve(data):

    result = 0

    print(data)

    w = max(map(itemgetter(0), data))
    h = max(map(itemgetter(1), data))

    left = deque([(0, (0, 0))])
    seen = set()
    while left:
        t, pos = left.popleft()
        if pos not in data:
            continue

        if pos == (w, h):
            return t



        if pos in seen:
            continue
        seen.add(pos)

        x,y = pos


        for dx, dy in directions:
            npos = x+dx, y+dy
            left.append((t+1, npos))

    # for _ in data:




        # ...

    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q17_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
