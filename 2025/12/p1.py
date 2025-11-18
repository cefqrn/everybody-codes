from functools import partial
from itertools import pairwise, product,starmap
from operator import contains, eq

def parse(s):
    g = {}
    for y, line in enumerate(s.splitlines()):
        for x, e in enumerate(line):
            g[y,x] = int(e)

    return g

def solve(parsed_input):
    g = parsed_input

    left = [((0,0), g[(0,0)])]
    seen = set()
    while left:
        (x, y), _ = pos, v = left.pop()
        if pos in seen:
            continue
        seen.add(pos)

        for dx, dy in (0, -1), (1, 0), (-1, 0), (0, 1):
            npos = nx, ny = x+dx, y+dy
            if (nv := g.get(npos, 99999)) <= v:
                left.append((npos, nv))

    return len(seen)

if __name__ == "__main__":
    with open("everybody_codes_e2025_q12_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))

