from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from re import findall

directions = (0, -1), (1, 0), (0, 1), (-1, 0)

def parse(s):
    data = s

    data = {}

    for y, line in enumerate(s.splitlines()):
        for x, c in enumerate(line):
            data[x,y] = c
            if c == "@":
                start = x, y
            if c == "#":
                end = x, y


    return data, start, end

def solve(data):
    data, start, end = data
    result = 0

    pos = start
    seen = {start}
    j = 0
    for i, (dx, dy) in enumerate(cycle(directions)):
        if pos == end:
            return j
        x, y = pos
        npos = nx, ny = x+dx, y+dy

        if npos in seen:
            continue
        seen.add(npos)

        j += 1

        pos = npos

    return result

if __name__ == "__main__":
    with open("everybody_codes_e3_q02_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
