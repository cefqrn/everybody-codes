from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from re import findall

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

def parse(s):
    return (tuple(map(int, s.split(","))))

    return data, s.splitlines()

def solve(data):
    # for l in data:

    result = 0
    from math import isqrt
    from itertools import count
    for x in data:
        z = isqrt(x)
        z += not (z & 1)
        for j in count(max(3, z - 100), 2):
            n = j*j - 1
            if n >= x:
                result += n - x
                print(x, j, n-x)
                break

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q01_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
