from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product, takewhile, zip_longest
from heapq import heappop, heappush
from math import inf
from operator import itemgetter
from re import findall

# directions = (0, 1), (1, 0), (0, -1), (-1, 0)
directions = (1, 1), (1, -1), (-1, -1), (-1, 1)

from itertools import batched
def parse(s):

    # grid = {}
    grid = []
    for y, line in enumerate(s.splitlines()):
        grid.append(line)
    #     for x, c in enumerate(line):
    #         grid[x, y] = c


    return grid

def count_lights(lines):
    result = 0
    for line in lines:
        amount = 0
        highest = 0
        for x in line:
            if not x.isdigit(): continue
            highest -= 1
            x = int(x)
            amount += x > highest
            highest = max(x, highest)

        result += amount
    return result


def solve_d(data, initial_reversal):
    target_reversal = not initial_reversal
    reversal = initial_reversal

    new_data = []
    for l in data:
        dots = tuple(takewhile(lambda x: x == ".", l))

        if reversal:
            l = l[len(dots):]
        else:
            l = l[:len(dots)] + l
        new_data.append(l)

        if not dots:
            reversal = target_reversal

    lines = tuple(map(''.join, zip_longest(*new_data, fillvalue=".")))
    print(*lines, sep="\n")

    return count_lights(lines), count_lights(map(reversed, lines))


def solve(data):
    result = 0

    reversal = False

    a, b = solve_d(data, True)
    c, d = solve_d(data, False)

    e = count_lights(data)
    f = count_lights(map(reversed, data))

    print(a, b, c, d, e, f)
    result = a + b + c + d + e + f

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q08_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
