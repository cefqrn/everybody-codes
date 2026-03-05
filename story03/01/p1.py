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
    result = 0

    for k, v in data.items():


        hi = max(v)
        print(v, hi)
        if v.count(hi) > 1:
            continue

        if v[1] == hi:
            result += k

            print(k, v, hi, v[1])



    return result

if __name__ == "__main__":
    with open("everybody_codes_e3_q01_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
