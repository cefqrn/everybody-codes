from functools import partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from math import inf

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

def parse(s):
    grid = {}
    for y, line in enumerate(s.splitlines()):
        for x, c in enumerate(line):
            if c == "@":
                vpos = x, y
            elif c == "S":
                pos = x, y
                grid[x, y] = 0
            else:
                grid[x, y] = int(c)

    return grid, pos, vpos

def kill(grid, pos, at_t):
    vx, vy = pos
    for (x, y), c in grid.items():
        if (x-vx)**2 + (y-vy)**2 <= at_t**2:
            grid[x, y] = None

from itertools import count
from heapq import heappop, heappush
def solve(data):
    grid, spos, vpos = data

    for R in count():
        # if R == 1:
        #     break

        limit = (R+1)*30
        kill(grid, vpos, R)

        seen = defaultdict(lambda: inf)
        left = [(0, spos)]
        while left:
            state = t, pos = heappop(left)

            # print(t, pos)
            if t > limit:
                break

            if seen[pos] <= t:
                continue
            seen[pos] = t

            x, y = pos
            # force going left first
            if y == vpos[1] and x > vpos[0]:
                continue

            for dx, dy in directions:
                npos = nx, ny = x+dx, y+dy
                if (cost := grid.get(npos)) is None:
                    continue

                heappush(left, (t+cost, npos))

        # print(R, seen)
        vx, vy = vpos
        left = [(seen[vx, y], (vx, y)) for y in range(vy+1, 999) if grid.get((vx, y)) is not None]
        # print(left)
        if not left:
            return None
        seen = defaultdict(lambda: inf)
        while left:
            state = t, pos = heappop(left)

            if t > limit:
                break

            if pos == spos:
                print(R, t)
                return R * t

            if seen[pos] <= t:
                continue
            seen[pos] = t

            x, y = pos
            # force going right
            if y == vpos[1] and x < vpos[0]:
                # print("aaa")
                continue

            for dx, dy in directions:
                npos = nx, ny = x+dx, y+dy
                if (cost := grid.get(npos)) is None:
                    continue

                heappush(left, (t+cost, npos))


if __name__ == "__main__":
    with open("everybody_codes_e2025_q17_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
