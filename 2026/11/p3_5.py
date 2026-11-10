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
    data = []

    for line in s.splitlines():
        data.append(tuple(map(int, findall(r"\d+", line))))

    portals = data[0][0]
    data = tuple(data[2:])

    return portals, data

def floyd_warshall(portal_count, distances):
    for j in range(portal_count):
        for i in range(portal_count):
            for k in range(portal_count):
                dist = min(distances[i][k], distances[i][j] + distances[j][k])
                distances[i][k] = dist
                distances[k][i] = dist

    return sum(map(sum, distances))


def partial_floyd_warshall(portal_count, distances, added):
    # extend the distance matrix
    distances = [row + [inf] * len(added) for row in distances]
    last_rows = [[inf] * (portal_count + len(added)) for _ in added]
    distances += last_rows

    R = range(portal_count + len(added))

    # add dummy nodes for the new connections
    # such that passing through the node takes 1 step
    for i, (a, b) in enumerate(added, portal_count):
        distances[i][i] = 0

        distances[a][i] = 1
        distances[i][a] = 1

        distances[b][i] = 0
        distances[i][b] = 0

    # allow dummy portal paths to pass through existing portals
    for j in R[:portal_count]:
        for i in R:
            for k in R[portal_count:]:
                dist = min(distances[i][k], distances[i][j] + distances[j][k])
                distances[i][k] = dist
                distances[k][i] = dist

    # skip checking paths through existing portals
    for j in R[portal_count:]:
        for i in R:
            for k in R:
                dist = min(distances[i][k], distances[i][j] + distances[j][k])
                distances[i][k] = dist
                distances[k][i] = dist

    # ignore distances from the added rows
    return sum(sum(row[:portal_count]) for row in distances[:portal_count])


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

    # precompute shortest paths going through existing connections
    _ = floyd_warshall(portal_count, connections)

    best = 0
    offset = portal_count // 8
    for start in range(portal_count // 8):
        spots = list(range(start, portal_count, offset))

        for perm1 in combinations(spots, r=4):
            left = set(spots).difference(perm1)

            for perm2 in permutations(left):
                if any(a > b for a, b in zip(perm1, perm2)):
                    continue

                # then just check if adding the new connections makes anything shorter
                added = tuple(zip(perm1, perm2))
                after = partial_floyd_warshall(portal_count, connections, added)

                best = max(best, before - after)

    result = best

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q11_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
