from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from dataclasses import dataclass
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

@dataclass
class Vec:
    x: int
    y: int
    collisions: int = 0

    def __add__(self, o):
        return Vec(self.x + o.x, self.y + o.y)
    def __neg__(self):
        return Vec(-self.x, -self.y)
    def __sub__(self, o):
        return self + -o
    def rot(self):
        return Vec(-self.y, self.x, self.collisions + 1)
    def flip(self):
        return Vec(-self.x, -self.y, self.collisions + 1)
    def __lt__(self, o):
        return (self.x, self.y) < (o.x, o.y)
    def __hash__(self):
        return hash((self.x, self.y))
    def __eq__(self, o):
        return (self.x, self.y) == (o.x, o.y)
    def __iter__(self):
        return iter((self.x, self.y, self.collisions))


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
DEATH = 1000000000000

def step(ghosts, grid):
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
                nd = d.rot()
                if nd.collisions >= DEATH:
                    continue
                new_ghosts2[pos - d].append(nd)

    # check ghost
    new_ghosts3 = defaultdict(list)
    for pos, dirs in new_ghosts2.items():
        if len(dirs) <= 1:
            new_ghosts3[pos] = dirs
        else:
            for d in dirs:
                nd = d.flip()
                if nd.collisions >= DEATH:
                    continue
                new_ghosts3[pos].append(nd)

    return new_ghosts3


def solve(data):
    result = 0

    ghosts, grid = data

    seen = set()
    seen_arr = []

    prev_count = None
    i = 0
    while True:
        ghost_count = sum(1 for _ in chain.from_iterable(ghosts.values()))
        if ghost_count == 1:
            print(i, ghosts)
        if ghost_count != prev_count:
            print(i, ghost_count)
            prev_count = ghost_count
            if not ghost_count:
                break

        hashable = tuple((k, tuple(Vec(*z) for z in v)) for k, v in sorted(ghosts.items()))

        if hashable in seen:
            last_seen = seen_arr.index(hashable)
            loop_size = len(seen_arr) - last_seen

            least_steps = inf
            for (_, prev), (_, curr) in zip(seen_arr[last_seen], hashable):
                for a, b in zip(prev, curr):
                    diff = b.collisions - a.collisions
                    to_death = (DEATH-1) - b.collisions
                    to_death_steps = to_death // diff

                    least_steps = min(least_steps, to_death_steps)

            mut_hashable = tuple((k, v) for k, v in sorted(ghosts.items()))
            for (_, prev), (_, curr) in zip(seen_arr[last_seen], mut_hashable):
                for a, b in zip(prev, curr):
                    diff = b.collisions - a.collisions
                    b.collisions += least_steps * diff

            print(least_steps, loop_size, least_steps * loop_size)
            i += least_steps * loop_size


            nghosts = defaultdict(list)
            for pos, dirs in ghosts.items():
                for d in dirs:
                    if d.collisions >= DEATH:
                        continue
                    nghosts[pos].append(d)

            hashable = tuple((k, tuple(Vec(*z) for z in v)) for k, v in sorted(nghosts.items()))

            seen = set()
            seen_arr = []
        else:
            seen.add(hashable)
            seen_arr.append(hashable)

            nghosts = step(ghosts, grid)
            i += 1

        ghosts = nghosts

    return i

if __name__ == "__main__":
    with open("everybody_codes_e2026_q10_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
