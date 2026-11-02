from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from operator import itemgetter
from re import findall

directions = (0, 1), (1, 0), (0, -1), (-1, 0)
directions += (1, 1), (1, -1), (-1, -1), (-1, 1)

from itertools import batched
def parse(s):

    result = {}
    for line in s.splitlines():
        a, b = line.split(":")
        b = b.split(",")

        result[a] = b

    return result

def solve(data):
    result = 0

    print(data)

    seen = set()
    left = ["NULL"]
    while left:
        curr = left.pop()
        if curr in seen:
            continue
        seen.add(curr)
        for req in data.get(curr, []):
            left.append(req)
    result = len(seen - {"NULL"})

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q06_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
