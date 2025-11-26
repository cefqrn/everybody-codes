from functools import partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

def parse(s):
    grid = {}
    pos = None
    for y, line in enumerate(s.splitlines()):
        for x, c in enumerate(line):
            if c == "@":
                pos = x, y
            else:
                grid[x, y] = int(c)

    assert pos
    return grid, pos

def solve(data):
    grid, pos = data
    vx, vy = pos

    # (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc) <= R * R

    best = -99
    best_r = None
    for R in range(999):
        result = 0
        for (x, y), c in grid.items():
            if (x-vx)**2 + (y-vy)**2 <= R*R:
                result += c
                grid[x, y] = 0

        if result > best:
            best = result
            best_r = R


    return best*best_r

if __name__ == "__main__":
    with open("everybody_codes_e2025_q17_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
