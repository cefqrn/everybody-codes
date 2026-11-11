from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import batched, chain, cycle, islice, pairwise, combinations, product, takewhile, zip_longest
from heapq import heappop, heappush
from math import inf
from operator import itemgetter
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

    return grid


def solve(data):

    result = 0

    print(data)

    groups = []

    seen = set()
    for p in data:
        if p in seen: continue

        group = set()
        left = [p]
        while left:
            curr = x, y = left.pop()
            if curr not in data: continue
            if curr in group: continue
            group.add(curr)
            for dx, dy in directions:
                np = nx, ny = x+dx, y+dy
                left.append(np)

        seen.update(group)
        groups.append(group)


        lo_x = min(map(itemgetter(0), group))
        lo_y = min(map(itemgetter(1), group))
        hi_x = max(map(itemgetter(0), group))
        hi_y = max(map(itemgetter(1), group))

        w = hi_x - lo_x + 1
        h = hi_y - lo_y + 1
        lo = min(w, h)

        result += lo
        # print(lo)


    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q12_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
