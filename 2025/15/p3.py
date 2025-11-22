# does not work, see p3_4.py for the first working solution

from functools import partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from math import inf
from heapq import heappop, heappush

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

def parse(s):
    wall = {}
    x, y = 0, 0
    d = dx, dy = directions[0]

    for inst in s.split(","):
        d = dx, dy = directions[(directions.index(d) + [1,-1][inst[0] == "L"]) % 4]
        for _ in range(int(inst[1:])):
            x += dx
            y += dy

            wall[x, y] = "#"

    return wall

def solve(data):
    print("starting search")
    
    walls = data
    last = tuple(data)[-1]
    lx, ly = last

    def h(pos):
        x, y = pos
        return abs(lx - x) + abs(ly - y)

    curr_f = h(p:=(0, 0))
    now = [(curr_f, 0, p)]
    later = []

    seen = defaultdict(lambda: inf)
    while now:
        next_f = inf
        while now:
            s = f, t, pos = now.pop()

            if f > curr_f:
                next_f = min(next_f, f)
                later.append(s)
                continue

            if seen[pos] <= f:
                continue
            seen[pos] = f

            x, y = pos

            for dx, dy in directions:
                npos = nx, ny = x+dx, y+dy
                nt = t+1

                if npos == last:
                    return nt

                if npos in walls:
                    continue
                later.append((nt+h(npos), nt, npos))

        now, later = later, now
        curr_f = next_f


if __name__ == "__main__":
    with open("everybody_codes_e2025_q15_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
