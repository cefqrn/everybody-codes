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
    def dist_to(a, b):
        if a == b:
            return 0

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

    # for i, j in combinations(range(1, portal_count+1), r=2):
        # result += 2 * 
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


def solve(data):
    result = 0

    portal_count, data = data

    connections = defaultdict(list)
    for a, b in pairwise(chain(range(1, portal_count+1), [1])):
        connections[a].append(b)
        connections[b].append(a)

    before = solve_n(portal_count, connections)

    for a, b in data:
        connections[a].append(b)
        connections[b].append(a)

    after = solve_n(portal_count, connections)

    print(before, after)
    result = before - after

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q11_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
