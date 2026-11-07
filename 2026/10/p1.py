from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product, takewhile, zip_longest
from heapq import heappop, heappush
from math import inf
from operator import itemgetter
from re import findall
from typing import NamedTuple

directions = ()
# directions += ( 0,  1), ( 1,  0), ( 0, -1), (-1,  0)
# directions += ( 1,  1), ( 1, -1), (-1, -1), (-1,  1)



dirs = ">v<^"

class Vec(NamedTuple):
    x: int
    y: int

    def __add__(self, o):
        return Vec(self.x + o.x, self.y + o.y)
    def __neg__(self):
        return Vec(-self.x, -self.y)
    def __sub__(self, o):
        return self + -o
    def rot(self):
        return Vec(-self.y, self.x)
    def flip(self):
        return Vec(-self.x, -self.y)


directions += Vec(1, 0), Vec(0, 1), Vec(-1, 0), Vec(0, -1)

from itertools import batched
def parse(s):

    grid = {}
    # grid = []

    ghosts = defaultdict(list)
    for y, line in enumerate(s.splitlines()):
        # grid.append(tuple(map(int, findall(r"\d+", line))))
        for x, c in enumerate(line):
            if c in ">v<^":
                ghosts[Vec(x, y)].append(directions[">v<^".index(c)])
            grid[Vec(x, y)] = c


    return ghosts, grid

def solve(data):
    result = 0

    ghosts, grid = data
    print(data)

    # for l in data:
    #     ...

    for _ in range(10):
        curr = 0

        print(ghosts)

        new_ghosts1 = defaultdict(list)
        for pos, dirs in ghosts.items():
            for d in dirs:
                new_ghosts1[pos + d].append(d)

        # check wall
        new_ghosts2 = defaultdict(list)
        for pos, dirs in new_ghosts1.items():
            for d in dirs:
                if grid.get(pos, ".") != "#":
                    new_ghosts2[pos].append(d)
                else:
                    curr += 1
                    new_ghosts2[pos - d].append(d.rot())

        # check ghost
        new_ghosts3 = defaultdict(list)
        for pos, dirs in new_ghosts2.items():
            if len(dirs) <= 1:
                new_ghosts3[pos] = dirs
            else:
                curr += len(dirs)
                new_ghosts3[pos] = [d.flip() for d in dirs]


        ghosts = new_ghosts3


        print(curr)
        result += curr

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q10_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
