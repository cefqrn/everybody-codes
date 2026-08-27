from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial, reduce
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from re import findall

directions = (0, -1), (1, 0), (0, 1), (-1, 0)

def parse(s):
    data = s

    data = []
    for line in s.splitlines():
        data.append(line)

    return data

from typing import NamedTuple
class Vec2(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def towards(self, other):
        new = self + other
        return Vec2(new.x // 2, new.y // 2)

    def adjacent(self):
        yield self + Vec2(0, 1)
        yield self + Vec2(0, -1)
        yield self + Vec2(1, 0)
        yield self + Vec2(-1, 0)

def solve(data):
    result = 0

    beacons = {}
    start = Vec2(*eval(data[0].split("=")[1]))
    for seq in data[1:-1]:
        name, coords = seq.split("=")
        beacons[name] = Vec2(*eval(coords))
    _, moves = data[-1].split("=")

    # print(start, moves, beacons)
    seen = {start}
    pos = start
    for move in moves:
        pos = pos.towards(beacons[move])
        seen.add(pos)

    fireflies = set()
    for pos in seen:
        fireflies.update(set(pos.adjacent()) - seen)

    # print(A, B, C, START, MOVES)

    print(pos)


    return len(fireflies)

if __name__ == "__main__":
    with open("everybody_codes_e4_q02_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
