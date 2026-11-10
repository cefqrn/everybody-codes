from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from copy import deepcopy
from fractions import Fraction
from functools import cache, partial
# from itertools import batched, chain, cycle, islice, pairwise, combinations, product, takewhile, zip_longest
from itertools import combinations, permutations
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

def floyd_warshall(portal_count, distances):
    for j in range(portal_count):
        for i in range(portal_count):
            for k in range(portal_count):
                dist = min(distances[i][k], distances[i][j] + distances[j][k])
                distances[i][k] = dist
                distances[k][i] = dist

    return sum(map(sum, distances))


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

    connections = [[inf] * portal_count for _ in range(portal_count)]
    for i in range(portal_count):
        connections[i][i] = 0
        for j in range(1, 3+1):
            j = (i + j) % portal_count
            connections[i][j] = 1
            connections[j][i] = 1

    before = floyd_warshall(portal_count, deepcopy(connections))
    print(f"{before = }")

    for a, b in data:
        connections[a-1][b-1] = 1
        connections[b-1][a-1] = 1

    best = 0
    offset = portal_count // 8
    for start in range(portal_count // 8):
        spots = list(range(start, portal_count, offset))

        for perm1 in combinations(spots, r=4):
            left = set(spots).difference(perm1)

            for perm2 in permutations(left):
                if any(a > b for a, b in zip(perm1, perm2)):
                    continue

                curr_connections = deepcopy(connections)

                for a, b in zip(perm1, perm2):
                    curr_connections[a][b] = 1
                    curr_connections[b][a] = 1

                    after = floyd_warshall(portal_count, curr_connections)

                    best = max(best, before - after)

    result = best

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q11_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
