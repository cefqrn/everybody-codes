# fixed bug in p3
#   no longer accepts paths that end right as the volcano expands

from functools import partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from math import inf

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

W, H = -inf, -inf

def parse(s):
    global W, H
    grid = {}
    H = len(lines := s.splitlines())
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            W = len(line)
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
        left = [(0, spos, None)]
        path_from = {}
        while left:
            state = t, pos, prev = heappop(left)

            # print(t, pos)
            if t >= limit:
                break

            if seen[pos] <= t:
                continue
            seen[pos] = t
            path_from[pos] = prev

            x, y = pos
            # force going left first
            if y == vpos[1] and x > vpos[0]:
                continue

            for dx, dy in directions:
                npos = nx, ny = x+dx, y+dy
                if (cost := grid.get(npos)) is None:
                    continue

                heappush(left, (t+cost, npos, pos))

        # print(R, seen)
        vx, vy = vpos
        left = [(seen[vx, y], (vx, y), (vx, y)) for y in range(vy+1, 999) if grid.get((vx, y)) is not None]

        old_path_from = path_from
        path_from = {}
        if not left:
            return None
        seen = defaultdict(lambda: inf)
        while left:
            state = t, pos, prev = heappop(left)

            if t >= limit:
                break

            if seen[pos] <= t:
                continue
            seen[pos] = t
            path_from[pos] = prev

            if pos == spos:
                print(R, t)
                curr = pos
                path = []
                while path_from[curr] != curr:
                    path.append(curr)
                    curr = path_from[curr]

                while curr:
                    path.append(curr)
                    curr = old_path_from[curr]

                for y in range(H):
                    result = ""
                    for x in range(W):
                        pos = (x, y)
                        if pos == spos:
                            result += "S"
                        elif (r:=grid.get(pos)) is not None:
                            if pos in path:
                                result += str(r)#"#"
                            else:
                                result += "."#str(r)
                        elif pos == vpos:
                            result += "@"
                        else:
                            assert pos not in path
                            result += " "

                    print(result)


                # print(path)
                return R * t

            x, y = pos
            # force going right
            if y == vpos[1] and x < vpos[0]:
                # print("aaa")
                continue

            for dx, dy in directions:
                npos = nx, ny = x+dx, y+dy
                if (cost := grid.get(npos)) is None:
                    continue

                heappush(left, (t+cost, npos, pos))


if __name__ == "__main__":
    with open("everybody_codes_e2025_q17_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
