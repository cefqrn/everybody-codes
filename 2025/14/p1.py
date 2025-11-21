from functools import partial
from itertools import pairwise, product, starmap
from operator import eq
from collections import deque, defaultdict

def parse(s):
    g = {}
    for y, line in enumerate(s.splitlines()):
        for x, c in enumerate(line):
            g[x, y] = c

    return g

def solve(data):
    g = data

    result = 0
    for _ in range(10):
        ngrid = g.copy()
        for p, s in g.items():
            x, y = p
            nc = 0
            for dx, dy in (1, 1), (-1, 1), (1, -1), (-1, -1):
                np = nx, ny = x+dx, y+dy
                if g.get(np) == "#":
                    nc += 1

            ngrid[p] = "#."[(s == "#") ^ (nc & 1)]

        # print(ngrid)

        g = ngrid


        for c in g.values():
            if c == "#":
                result += 1

        print(result)


    return result

if __name__ == "__main__":
    with open("everybody_codes_e2025_q14_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
