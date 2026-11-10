from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
# from itertools import batched, chain, cycle, islice, pairwise, combinations, product, takewhile, zip_longest
# from itertools import batched, combinations, permutations
from heapq import heappop, heappush
from math import inf
import math
from operator import itemgetter
from re import findall
from typing import NamedTuple

directions = ()
directions += ( 0,  1), ( 1,  0), ( 0, -1), (-1,  0)
directions += ( 1,  1), ( 1, -1), (-1, -1), (-1,  1)

def parse(s):

    grid = {}
    grid = []

    for y, line in enumerate(s.splitlines()):
        grid.append(tuple(map(int, findall(r"\d+", line))))
        for x, c in enumerate(line):
            ...

    portals = grid[0][0]
    grid = tuple(grid[2:])

    return portals, grid

def solve_n(portal_count, connections):
    @cache
    def dist_to(a, b):
        if a == b:
            return 0

        if a > b:
            return dist_to(b, a)

        seen = {}
        left = deque([(0, a)])
        while left:
            t, curr = left.popleft()
            if curr in seen: continue
            seen[curr] = t

            if curr == b:
                return t

            for n in connections[curr]:
                left.append((t+1, n))

        return inf

    # result = 0
    # for i, j in combinations(range(1, portal_count+1), r=2):
    #     result += 2 * dist_to(i, j)
    # return result

    result = 0
    for i in range(1, portal_count+1):
        curr = 0
        for j in range(1, portal_count+1):
            if i == j: continue
            curr += dist_to(i, j)
            # print(i, j, dist_to(i, j))
        # print(i, curr)
        result += curr
    # print("asdhjkfashjkdasdfhjk")
    return result

def rotate(a, portal_count):
    if a > portal_count:
        return a - portal_count
    elif a < 1:
        return a + portal_count
    else:
        return a


def solve(data):
    result = 0

    portal_count, data = data

    connections = defaultdict(set)
    for a in range(1, portal_count+1):
        for z in range(-3, 3+1):
            if not z: continue
            b = rotate(a + z, portal_count)
            connections[a].add(b)
            connections[b].add(a)

    before = solve_n(portal_count, connections)
    print(f"{before = }")

    for a, b in data:
        connections[a].add(b)
        connections[b].add(a)

    from copy import deepcopy
    best = 0
    offset = portal_count // 8
    from random import shuffle
    for start in range(1, portal_count // 8):
        spots = list(range(start, portal_count+1, offset))

        for _ in range(100):
            curr_connections = deepcopy(connections)
            # for a, b in batched(spots, 2):
            for a, b in zip(spots[::2], spots[1::2]):
                curr_connections[a].add(b)
                curr_connections[b].add(a)

            after = solve_n(portal_count, curr_connections)
            best = max(best, before - after)
            shuffle(spots)

        # best = max(best, before - after)
        # shuffle(spots)
        # print(spots)
        # for perm1 in combinations(spots, r=4):
        #     left = set(spots).difference(perm1)
        #     for perm2 in permutations(left):
        #         curr_connections = deepcopy(connections)
        #         for a, b in zip(perm1, perm2):
        #             curr_connections[a].add(b)
        #             curr_connections[b].add(a)

        #             after = solve_n(portal_count, curr_connections)

        #             best = max(best, before - after)

    result = best

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q11_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
