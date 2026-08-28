from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial, reduce
from itertools import chain, cycle, islice, pairwise, combinations, product, starmap
from heapq import heappop, heappush
from math import inf
from re import findall

directions = (0, -1), (1, 0), (0, 1), (-1, 0)

def parse(s):
    data = s

    data = []
    a, b, c, d = s.splitlines()
    data.append(int(a.split("=")[1]))
    data.append(int(b.split("=")[1]))
    data.append(c.split("=")[1])
    data.append(d.split("=")[1])

    return data

"""
width=30
height=10
horizontal-offsets=10011
vertical-offsets=11011
"""

from typing import NamedTuple
class Vec2(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def towards(self, other):
        new = self + other
        return Vec2(new.x // 2, new.y // 2)

    @property
    def adjacent(self):
        yield self + Vec2(0, 1)
        yield self + Vec2(0, -1)
        yield self + Vec2(1, 0)
        yield self + Vec2(-1, 0)

def solve(data):
    result = 0

    blocked = set()
    width, height, horizontal_offsets, vertical_offsets = data

    for y, n in zip(range(height+1), cycle(horizontal_offsets)):
        for x in range(n=="1", width+1, 2):
            curr = Vec2(x, y)
            other = Vec2(x, y-1)
            blocked.add((curr, other))
            blocked.add((other, curr))

    for x, n in zip(range(width+1), cycle(vertical_offsets)):
        for y in range(n=="1", height+1, 2):
            curr = Vec2(x, y)
            other = Vec2(x-1, y)
            blocked.add((curr, other))
            blocked.add((other, curr))

    for curr in starmap(Vec2, product(range(width+1), range(height+1))):
        for other in curr.adjacent:
            if (curr, other) not in blocked:
                break
        else:
            result += 1

    return result

if __name__ == "__main__":
    with open("everybody_codes_e4_q03_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
