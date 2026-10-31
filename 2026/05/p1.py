from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from operator import itemgetter
from re import findall

directions = (0, 1), (1, 0), (0, -1), (-1, 0)
directions += (1, 1), (1, -1), (-1, -1), (-1, 1)

from itertools import batched
def parse(s):
    grid = {}
    lines = s.splitlines()
    for y, line in enumerate(lines):
        width = len(line)
        for x, c in enumerate(line):
            grid[x, y] = c
    height = len(lines)

    grid[width//2, height//2] = "#"

    # result = []
    # for batch in batched(findall(r"\d+", s), 4):
    #     result.append(tuple(map(int, batch)))
    # return result
    return grid

def solve(data):
    result = 0

    neighboring = set()
    while True:
        curr = data.copy()

        for (x, y), state in data.items():
            if state == "#":
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    neighboring.add((nx, ny))
                continue

            if (x, y) not in neighboring:
                continue

            neighbors = 0
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                neighbors += data.get((nx, ny), "asdf") in "1#"

            if neighbors >= 5:
                curr[x, y] = "#"
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    neighboring.add((nx, ny))

        if curr == data:
            break

        data = curr
        print(sum(1 for x in chain.from_iterable(data.values()) if x == "#"))

    # print(data)

    result = sum(1 for x in chain.from_iterable(data.values()) if x == "#")

    # for x in data:
    #     result += 0

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q05_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
