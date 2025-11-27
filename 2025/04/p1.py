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

def solve(data):
    curr = Fraction(2025)
    for a, b in pairwise(data):
        curr *= Fraction(a, b)
    return int(curr)

if __name__ == "__main__":
    with open("everybody_codes_e2025_q04_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
