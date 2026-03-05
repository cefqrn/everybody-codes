from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from re import findall

directions = (0, -1),(0, -1),(0, -1), (1, 0),(1, 0),(1, 0), (0, 1),(0, 1),(0, 1), (-1, 0),(-1, 0),(-1, 0),

# directions = (0, -1), (1, 0), (0, 1), (-1, 0)


def parse(s):
    data = s

    data = {}
    ends = set()

    for y, line in enumerate(s.splitlines()):
        for x, c in enumerate(line):
            data[x,y] = c
            if c == "@":
                start = x, y
            if c == "#":
                ends.add((x,y))


    return data, start, ends


def ff(ends, seen):
    left = list(ends)
    seen2 = set(ends)
    while left:
        p = x, y = left.pop()
        if max(abs(x), abs(y)) > 1234:
            return True

        for dx, dy in directions:
            npos = nx, ny = x+dx, y+dy
            if npos in seen:
                continue
            if npos in seen2:
                continue
            seen2.add(npos)
            left.append(npos)

    return False

def solve(data):
    data, start, ends = data
    result = 0

    pos = start
    seen = {start} | ends
    j = 0

    for i, (dx, dy) in enumerate(cycle(directions)):
        if not ff(ends, seen):
            return j

        x, y = pos
        npos = nx, ny = x+dx, y+dy

        if npos in seen:
            continue
        if not ff({npos}, seen):
            seen.add(npos)
            continue

        seen.add(npos)

        j += 1
        pos = npos

        # for i in range(7):
        #     for j in range(7):
        #         c = data[j, i] if (j, i) not in seen else "+"
        #         c = c if (j, i) != pos else "@"
        #         print(end=c)
        #     print()
        # print()

    return result

if __name__ == "__main__":
    with open("everybody_codes_e3_q02_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
