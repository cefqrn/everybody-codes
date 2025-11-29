from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from re import findall

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

def parse(s):
    data = {}
    for y, l in enumerate(s.splitlines()):
        for x, c in enumerate(l):
            if c == "E":
                end = x, y
                c = "T"

            elif c == "S":
                start = x, y
                c = "T"

            data[x, y] = c

    return data, s.splitlines(), start, end

def solve(data):
    # for l in data:
    grid, lines, start, end = data

    connections = defaultdict(list)
    # for y, l in enumerate(lines):
    #     for x, c in enumerate(l):
    for (x, y), c in grid.items():
            if c != "T":
                continue

            if grid.get((x+1, y)) == "T":
                connections[x, y].append((x+1, y))
                connections[x+1, y].append((x, y))
                # result += 1

            if (x ^ y) & 1:
                if grid.get((x, y+1)) == "T":
                    connections[x, y].append((x, y+1))
                    connections[x, y+1].append((x, y))
                    # result += 1

    print(connections[8, 2])

    left = [(0, start)]
    seen = set()
    while left:
        t, p = heappop(left)

        # print(p, end)

        if p == end:
            return t

        if p in seen:
            continue
        seen.add(p)
        

        for o in connections[p]:
            heappush(left, (t+1, o))



if __name__ == "__main__":
    with open("everybody_codes_e2025_q20_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
