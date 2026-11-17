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

        # digits = tuple(map(int, findall(r"\d+", line)))
        # grid.append(digits)
        # grid.append(line)

        for x, c in enumerate(line):
            if c == ".":
                continue

            grid[x, y] = c

        ...

    return grid


def solve(data):

    result = 0

    print(data)

    w = max(map(itemgetter(0), data))
    h = max(map(itemgetter(1), data))

    seen = set()

    t = 0

    pos = 0, 0
    dx, dy = direction = 0, 1

    z = 0
    collected = False
    while True:
        x, y = pos

        # z += 1


        for ny in range(h+1):
            l = []
            for nx in range(w+1):
                c = " "
                if (nx, ny) in data:
                    c = "#"
                if pos == (nx, ny):
                    c = "v>^<"[directions.index((dx, dy))]
                l.append(c)
            print("".join(l))
        print()

        print(pos, (dx, dy), t)

        # if pos == (w, h):
        #     z += 1
        #     if z == 3:
        #         raise ValueError

        if pos == (w, h) and (dx, dy) == (0, -1):
            return t

        assert pos in data


        # if z > 10:
        #     raise ValueError

        # if pos == (w, h):
        #     collected = True

        # if collected and pos == (0, 0):
        #     return t


        # move right
        npos = x-dy, y+dx
        if npos in data:
            dx, dy = -dy, dx
            pos = npos
            continue

        # forwards
        npos = x+dx, y+dy
        if npos in data:
            pos = npos
            t += 1
        else:
            # turn left
            dx, dy = dy, -dx
            # pos = npos
            t += 1
            continue

        # # move back
        # npos = x-dx, y-dy
        # if npos in data:
        #     dx, dy = -dx, -dy
        #     pos = npos
        #     t += 3
        #     continue

    raise ValueError



        # for dx, dy in directions:
        #     npos = x+dx, y+dy
        #     left.append((t+1, npos))

    # for _ in data:




        # ...

    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q17_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
