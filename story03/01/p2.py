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

    data = {}
    for line in s.splitlines():
        a, b = line.split(":")
        k = [[c <= 'Z' for c in w] for w in b.split()]
        k = [reduce(lambda a, x: 2*a + x, w) for w in k]
        data[int(a)] = k

    return data

def solve(data):


    best = []

    hi = -inf
    for k, v in data.items():
        *_, shine = v
        if shine > hi:
            best = [k]
            hi = shine
        elif shine == hi:
            best.append(k)

    result = 0

    print(min(best, key=lambda x: sum(data[x][:-1])))

    return result

if __name__ == "__main__":
    with open("everybody_codes_e3_q01_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
