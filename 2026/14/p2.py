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

    outside = 0
    inside = 0

    edges = {}

    @cache
    def edges_between(a: str, b: str | None=None):
        """None for outside"""
        result = 0
        for (x, y), c in data.items():
            if c != a: continue

            for dx, dy in directions:
                np = nx, ny = x+dx, y+dy
                result += data.get(np) == b

        # print(a, b, result)

        return result


    values = list(set(data.values())) + [None]

    distance = {}
    for a, b in combinations(values, r=2):
        distance[a, b] = distance[b, a] = edges_between(a, b)


    result = 0

    seen = {None}
    left = set(values) - {None}
    # while left:
    while left:
        # find closest to tree

        best = None
        best_cost = None
        for s in seen:
            for l in left:
                curr = distance[s, l]
                if not curr: continue
                if best_cost is None or curr < best_cost:
                    best = l
                    best_cost = curr


        # closest = min(left, key=lambda l: min(distance[l, k] for k in seen if distance[l, k]))
        # cost = min(distance[closest, l] for l in seen if distance[l, closest])
        seen.add(best)
        left.remove(best)
        result += best_cost

        print(best_cost)

        # for curr in left:
        # for k in seen:

    # for (x, y), c in data.items():
    #     # print(x, y, c)

    #     for dx, dy in directions:
    #         np = nx, ny = x+dx, y+dy

    #         inside += data.get(np) not in {None, c}
    #         outside += np not in data



    #     ...


    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q14_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
