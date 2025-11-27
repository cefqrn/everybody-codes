
from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from re import findall

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

from fractions import Fraction

def parse(s):
    return tuple(map(int, s.splitlines()))

def solve1(data, first):
    curr = Fraction(first)
    for a, b in pairwise(data):
        curr *= Fraction(a, b)
    return int(curr)

def solve(data):
    # curr = Fraction(10000000000000)
    # for a, b in pairwise(data[::-1]):
    #     curr *= Fraction(a, b)

    # return int(curr)


    def is_ok(first):
        return solve1(data, first) >= 10000000000000

    hi = 1
    while solve1(data, hi) <= 10000000000000:
        hi *= 2

    lo = 0
    print(hi)

    while lo < hi:
        mid = (lo + hi) // 2
        if is_ok(mid):
            hi = mid - 1
        else:
            lo = mid + 1

    print(mid)


    return bisect_left(range((1<<63)-1), True, key=is_ok)

if __name__ == "__main__":
    with open("everybody_codes_e2025_q04_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
