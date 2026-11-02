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

    inverse = defaultdict(set)
    for k, v in data.items():
        for x in v:
            inverse[x].add(k)

    print

    # print(inverse.get("NULL"))

    versions_used = [set(), set(), set()]

    for i, start in enumerate(("NULLv1", "NULLv2", "NULLv3")):
        seen = versions_used[i]
        left = [start]
        while left:
            curr = left.pop()
            if curr in seen:
                continue
            seen.add(curr)
            for req in inverse.get(curr, []):
                left.append(req)
        seen.remove(start)

    print(versions_used)

    result = sum(v >= 2 for v in Counter(chain.from_iterable(versions_used)).values())

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q06_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
