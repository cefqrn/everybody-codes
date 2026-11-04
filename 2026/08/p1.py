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

def solve(data):
    result = 0

    reversal = False

    new_data = []
    for l in data:
        dots = tuple(takewhile(lambda x: x == ".", l))

        if reversal:
            l = l[len(dots):]
        else:
            l = l[:len(dots)] + l
        new_data.append(l)

        if not dots:
            reversal = True
            # break

    lines = tuple(map(''.join, zip_longest(*new_data, fillvalue=".")))

    for line in lines:
        amount = 0
        highest = 0
        for x in line:
            highest -= 1
            if not x.isdigit(): continue
            x = int(x)
            if x > highest:print(x)
            amount += x > highest
            highest = max(x, highest)

        if amount:
            print(amount, "aaaa")
        result += amount


    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q08_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
