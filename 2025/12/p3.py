from functools import partial
from itertools import pairwise, product,starmap
from operator import contains, eq

def parse(s):

    global w, h, g
    g = {}
    h = len(s.splitlines())
    for y, line in enumerate(s.splitlines()):
        w = len(line)
        for x, e in enumerate(line):
            g[y,x] = int(e)

    return g


def exploded_by(pos, ignored):
    left = [(pos, g[pos])]

    seen = set()
    while left:
        (x, y), _ = pos, v = left.pop()
        if pos in seen or pos in ignored:
            continue
        seen.add(pos)

        for dx, dy in (0, -1), (1, 0), (-1, 0), (0, 1):
            npos = nx, ny = x+dx, y+dy
            if (nv := g.get(npos, 99999)) <= v:
                left.append((npos, nv))

    return seen


def solve(parsed_input):
    g = parsed_input

    best_exploded = None
    best = 0
    for pos in g:
        curr = exploded_by(pos, set())
        if len(curr) > best:
            best_exploded = curr
            best = len(curr)

    ignored = best_exploded

    best_exploded = None
    best = 0
    for pos in g:
        curr = exploded_by(pos, ignored)
        if len(curr) > best:
            best_exploded = curr
            best = len(curr)

    ignored |= best_exploded

    best_exploded = None
    best = 0
    for pos in g:
        curr = exploded_by(pos, ignored)
        if len(curr) > best:
            best_exploded = curr
            best = len(curr)

    ignored |= best_exploded

    return len(ignored)

if __name__ == "__main__":
    with open("everybody_codes_e2025_q12_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))

