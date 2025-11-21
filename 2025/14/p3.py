from functools import partial
from itertools import pairwise, product, starmap
from operator import eq
from collections import deque, defaultdict

def parse(s):
    pattern = {}
    for y, line in enumerate(s.splitlines()):
        for x, c in enumerate(line):
            pattern[x, y] = c

    g = {}
    for p in product(range(34), repeat=2):
        g[p] = "."

    return g, pattern

def solve(data):
    initial, pattern = data
    g = initial

    result = 0
    prev = None
    seen = []
    matches = []
    for i in range(1000000000):
        ngrid = g.copy()
        for p, s in g.items():
            x, y = p
            nc = 0
            for dx, dy in (1, 1), (-1, 1), (1, -1), (-1, -1):
                np = nx, ny = x+dx, y+dy
                if g.get(np) == "#":
                    nc += 1

            ngrid[p] = "#."[(s == "#") ^ (nc & 1)]

        g = ngrid
        s = "".join(g.values())
        if s in seen:
            break
        seen.append(s)

        for (x, y), c in pattern.items():
            if g[x+13, y+13] != c:
                break
        else:
            print(i, None if prev is None else i-prev)
            prev = i
            matches.append((i, s.count("#")))


    # print(seen.index(x))

    # print(len(seen))
    # print(matches)

    repeats, left = divmod(1000000000, len(seen))
    result += sum(n for _, n in matches) * repeats


    for x, n in matches:
        if x >= left:
            break

        result += n

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2025_q14_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
