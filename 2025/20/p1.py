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
            data[x, y] = c

    return data, s.splitlines()

def solve(data):
    # for l in data:
    grid, lines = data

    result = 0
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c != "T":
                continue

            if grid.get((x+1, y)) == "T":
                result += 1

            if (x ^ y) & 1:
                print(x, y)
                if grid.get((x, y+1)) == "T":
                    result += 1

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2025_q20_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
