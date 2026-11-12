from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import batched, chain, count, cycle, islice, pairwise, combinations, product, takewhile, zip_longest
from heapq import heappop, heappush
from math import comb, floor, inf
from operator import itemgetter, mul
from re import findall
from typing import NamedTuple

directions = ()
directions += ( 0,  1), ( 1,  0), ( 0, -1), (-1,  0)
# directions += ( 1,  1), ( 1, -1), (-1, -1), (-1,  1)


def parse_p1(s):

    # grid = {}
    grid = []

    for y, line in enumerate(s.splitlines()):

        if y == 1:
            grid.append(l := [])
            for c in line.split()[1].split(":"):
                l.append(1 | -(c == "CCW"))
            continue

        digits = tuple(map(int, findall(r"\d+", line)))
        grid.append(digits)
        # grid.append(line)

        # for x, c in enumerate(line):
        #     if c == ".":
        #         continue

        #     grid[x, y] = c

        ...

    return grid


def cross(u, v):
    a, b, c = u
    x, y, z = v
    return b*z - c*y, -a*z + c*x, a*y - b*x


def cross_2d_z(u, v):
    a, b = u
    x, y = v
    _, _, z = cross((a, b, 1), (x, y, 1))
    return z


def dot(u, v):
    return sum(map(mul, u, v))


def sign(x):
    if x == 0: return 0
    if x > 0: return  1
    if x < 0: return -1


def to_vec(a):
    angle = a * 2*pi
    return cos(angle), sin(angle)


def get_k(a, b):
    mod1, _, pos1, _ = a
    mod2, _, pos2, _ = b
    a = to_vec(Fraction(pos1, mod1))
    b = to_vec(Fraction(pos2, mod2))
    return sign(cross_2d_z(a, b)), dot(a, b)


from math import sin, cos, pi, ceil, floor

from fractions import Fraction

def solve_p1(data):

    result = 0

    # print(data)

    hands = list(map(list, zip(*data)))
    for (m1, d1, p1, t1), (m2, d2, p2, t2) in combinations(hands, r=2):
        # center on p1
        p0 = p = Fraction(p2, m2) - Fraction(p1, m1)
        relative_velocity = Fraction(d2, m2) - Fraction(d1, m1)

        # t1 = t2 = 1
        p += relative_velocity * min(t1, t2)

        a, b = len(range(ceil(p0), floor(p)+1)), len(range(ceil(p), floor(p0)+1))
        before = max(a, b) - p0.is_integer()

        print("before", p0, p)

        p0 = p
        if t1 < t2:
            relative_velocity = Fraction(d2, m2)
        elif t2 < t1:
            relative_velocity = -Fraction(d1, m1)

        t_left = max(t1, t2) - min(t1, t2)
        p += relative_velocity * t_left

        print("after", p0, p)

        a, b = len(range(ceil(p0), floor(p)+1)), len(range(ceil(p), floor(p0)+1))
        after = max(a, b) - p0.is_integer()

        print(before, after)

        result += before + after

        # t1 = t2 = 0
        # a = Fraction(p1, m1)
        # b = Fraction(p2, m2)

        # a += t1 * Fraction(d1, m1)
        # b += t2 * Fraction(d2, m2)

        # diff = max(a, b) - min(a, b)

        # print(f"{a:.2f} {b:.2f}: {diff:.2f}")

        # result += int(diff)

    return result

def parse(s):
    return *map(parse_p1, s.split("\n\n")),

def solve(data):
    # data = data[-8],
    solutions = *map(solve_p1, data),
    print(solutions)
    return sum(solutions)


if __name__ == "__main__":
    with open("everybody_codes_e2026_q13_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
