from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import batched, chain, count, cycle, islice, pairwise, combinations, product, takewhile, zip_longest
from heapq import heappop, heappush
from math import comb, inf
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


from math import sin, cos, pi

from fractions import Fraction

def solve_p1(data):

    result = 0

    # print(data)

    hands = list(map(list, zip(*data)))
    # hands = hands[:2]

    # print(hands)

    # print(" ".join(f"{360*pos/mod:.0f}"for mod, _, pos, _ in hands))




    met_previously = [
        Fraction(pos2, mod2) == Fraction(pos1, mod1)
        for (mod1, _, pos1, _), (mod2, _, pos2, _)
        in combinations(hands, r=2)
    ]
    step = Fraction(1, 8)
    for t in count():
        moved = False

        initital_comparisons = []
        for a, b in combinations(hands, r=2):
            k = get_k(a, b)
            initital_comparisons.append(k)

        for i, hand in enumerate(hands):
            mod, direction, pos, left = hand

            if not left: continue
            moved = True

            pos = (pos + direction * step) % mod
            left -= step

            hands[i] = mod, direction, pos, left

        # print(hands)

        final_comparisons = []
        for a, b in combinations(hands, r=2):
            k = get_k(a, b)
            final_comparisons.append(k)

        for i, ((z1, _), (z2, d)) in enumerate(zip(initital_comparisons, final_comparisons)):
            if z1 == z2:  # no change
                # print("no change")
                met_previously[i] = False
                continue
            if d < 0:  # other side
                # print("wrong side")
                met_previously[i] = False
                continue
            if met_previously[i]:  # no double count
                # print("double count")
                met_previously[i] = False
                continue

            # print(i)
            result += 1
            met_previously[i] = True
        # print()

        # print(" ".join(f"{pos/mod:.2f}"for mod, _, pos, _ in hands))
        # print(" ".join(f"{360*pos/mod:.0f}"for mod, _, pos, _ in hands))


        if not moved:
            break

    # print(hands)




    return result

def parse(s):
    return *map(parse_p1, s.split("\n\n")),

def solve(data):
    # data = data[-8],
    solutions = *map(solve_p1, data),
    print(solutions)
    return sum(solutions)


if __name__ == "__main__":
    with open("everybody_codes_e2026_q13_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
