from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from re import findall

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

from itertools import batched
def parse(s):
    # return (tuple(map(int, s.split(","))))
    result = []
    for batch in batched(findall(r"\d+", s), 2):
        result.append(batch)
    return result

    return data, s.splitlines()

def solve(data):
    # for l in data:

    result = 0
    for (a, b) in data:
        a *= len(b)
        a = a[-len(b):]
        print(a, b)
        for i, (a, b) in zip(range(len(b))[::-1], zip(a, b)):
            result += (k := int(a)**i * int(b))
            print("is", k, int(a)**i, b)
        print(result)
        # i, (x, y) in zip(range(4)[::-1], data)
        # for?
        # print(i, *zip(a, b))  # noqa: F821

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q03_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
