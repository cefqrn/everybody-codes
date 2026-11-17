from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import batched, chain, count, cycle, groupby, islice, pairwise, combinations, product, takewhile, zip_longest
from heapq import heappop, heappush
from math import comb, inf
from operator import itemgetter, mul
from re import findall
from typing import NamedTuple

directions = ()
directions += ( 0,  1), ( 1,  0), ( 0, -1), (-1,  0)
# directions += ( 1,  1), ( 1, -1), (-1, -1), (-1,  1)


def parse(s):

    # grid = {}
    grid = []

    for y, line in enumerate(s.splitlines()):

        # digits = tuple(map(int, findall(r"\d+", line)))
        # grid.append(digits)
        # grid.append(line)

        # for x, c in enumerate(line):
        #     if c == ".":
        #         continue

        #     grid[x, y] = c

        ...

    return s

    return grid


def solve(data):

    result = 0

    data *= 10
    groups = list(data)

    # groups = ([k for k, _ in groupby(data)])
    # print(groups)

    # groups = list(data)
    # print("".join(groups), result)


    lo = 0
    hi = len(groups) - 1
    while True:
        init = groups[lo]
        while lo < hi:
            while groups[lo] == init:
                lo += 1
            while groups[hi] != init:
                hi -= 1
            if lo >= hi:
                break

            # print(lo, hi)
            groups[lo:hi+1] = groups[lo:hi+1][::-1]
            result += hi - lo + 1

            print("".join(groups), result)
        hi = len(groups) - 1

        # groups.popleft()
        # if not groups:

    # print(data)
    # while lo <= hi:
    #     if data[lo] != data[hi]:
    #         result += 1



    # for _ in data:



    #     ...

    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q16_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
