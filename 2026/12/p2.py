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

            grid[x, -y] = c

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

        corners = (lo_x, lo_y), (lo_x, hi_y), (hi_x, lo_y), (hi_x, hi_y)
        missing = None
        for i, c in enumerate(corners):
            if c not in group:
                assert not missing
                missing = i

        w = hi_x - lo_x + 1
        h = hi_y - lo_y + 1
        if missing is None:
            lo = min(w, h)
            result += lo
            print(lo)
            continue

        group = [(x-lo_x, y-lo_y) for x, y in group]

        print(f"{missing = }")

        if missing == 0:
            group = [(x, y) for x, y in group]
        if missing == 1:
            group = [(x, -y) for x, y in group]
        if missing == 2:
            group = [(-x, y) for x, y in group]
        if missing == 3:
            group = [(-x, -y) for x, y in group]

        lo_x = min(map(itemgetter(0), group))
        lo_y = min(map(itemgetter(1), group))
        hi_x = max(map(itemgetter(0), group))
        hi_y = max(map(itemgetter(1), group))
        group = [(x-lo_x, y-lo_y) for x, y in group]
        lo_x = min(map(itemgetter(0), group))
        lo_y = min(map(itemgetter(1), group))
        hi_x = max(map(itemgetter(0), group))
        hi_y = max(map(itemgetter(1), group))

        w = hi_x - lo_x + 1
        h = hi_y - lo_y + 1

        print(sorted(group, key=lambda x:(x[1],x[0])))

        for i, x in enumerate(range(lo_x, hi_x+1)):
            if (x, lo_y) in group:
                break
        i = w - i

        for j, y in enumerate(range(lo_y, hi_y+1)):
            if (lo_x, y) in group:
                break
        j = h - j

        print(i, j, "gives", w, h, i+j)

        lo = min(w, h, i+j)
        result += lo

        print(lo)

    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q12_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
