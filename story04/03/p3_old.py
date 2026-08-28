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

def solve_p2(data):
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


    isolated = set()
    for curr in starmap(Vec2, product(range(width+1), range(height+1))):
        for other in curr.adjacent:
            if (curr, other) not in blocked:
                break
        else:
            isolated.add(curr)

    to_see = set(starmap(Vec2, product(range(width+1), range(height+1))))

    H_RANGE = range(width+1)
    V_RANGE = range(height+1)

    curr_group = False
    groups = [[], []]

    def find_neighbors(initial, group):
        if initial not in to_see:
            return

        left = [initial]
        adjacent = set()
        seen = set()
        while left:
            curr = left.pop()
            if curr in seen: continue
            seen.add(curr)
            for adj in curr.adjacent:
                if adj.x not in H_RANGE:
                    continue
                if adj.y not in V_RANGE:
                    continue
                if (curr, adj) in blocked:
                    adjacent.add(adj)
                else:
                    left.append(adj)

        groups[group].append(seen)
        to_see.difference_update(seen)

        for adj in adjacent:
            find_neighbors(adj, not group)

    find_neighbors(next(iter(to_see)), False)

    group_a, group_b = groups

    group_a_count = 0
    for x in group_a:
        if len(x) > 1:
            continue
        x, = x
        if x in isolated:
            group_a_count += 1

    group_b_count = len(isolated) - group_a_count

    return group_a_count, group_b_count

def solve(data):
    result = 0

    blocked = set()
    actual_width, actual_height, horizontal_offsets, vertical_offsets = data

    width, height = len(horizontal_offsets), len(vertical_offsets)

    for y, n in zip(range(height+4), cycle(horizontal_offsets)):
        for x in range((n=="1"), width+4, 2):
            curr = Vec2(x, y)
            other = Vec2(x, y-1)
            blocked.add((curr, other))
            blocked.add((other, curr))

    for x, n in zip(range(width+4), cycle(vertical_offsets)):
        for y in range((n=="1"), height+4, 2):
            curr = Vec2(x, y)
            other = Vec2(x-1, y)
            blocked.add((curr, other))
            blocked.add((other, curr))


    isolated = set()
    for curr in starmap(Vec2, product(range(width+1), range(height+1))):
        for other in curr.adjacent:
            if (curr, other) not in blocked:
                break
        else:
            isolated.add(curr)

    print(isolated)

    H_RANGE = range(width+1)
    V_RANGE = range(height+1)
    to_see = set(starmap(Vec2, product(range(width+1), range(height+1))))

    groups = [[], []]

    def find_neighbors(initial, group):
        if initial not in to_see:
            return

        left = [initial]
        adjacent = set()
        seen = set()
        while left:
            curr = left.pop()
            if curr in seen: continue
            seen.add(curr)
            for adj in curr.adjacent:
                if adj.x not in H_RANGE:
                    continue
                if adj.y not in V_RANGE:
                    continue
                if (curr, adj) in blocked:
                    adjacent.add(adj)
                else:
                    left.append(adj)

        groups[group].append(seen)
        to_see.difference_update(seen)

        for adj in adjacent:
            find_neighbors(adj, not group)

    find_neighbors(next(iter(to_see)), False)

    group_a, group_b = groups

    group_a_count = 0
    for x in group_a:
        if len(x) > 1:
            continue
        x, = x
        if x in isolated:
            group_a_count += 1

    group_b_count = len(isolated) - group_a_count

    actual_counts = [0, 0]
    for x, y in product(range(actual_width // width), range(actual_height // height)):
        order = (x ^ y) & 1
        actual_counts[0 - order] += group_a_count
        actual_counts[1 - order] += group_b_count

    print(actual_counts)


    actual_width


    return max(group_a_count, group_b_count)

if __name__ == "__main__":
    with open("everybody_codes_e4_q03_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
