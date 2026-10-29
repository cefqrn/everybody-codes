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
    for batch in batched(findall(r"\d+", s), 3):
        result.append(batch[1:])
    return result

    return data, s.splitlines()


def iso2(a, b):
    result = 0
    a *= len(b)
    a = a[-len(b):]
    for i, (a, b) in zip(range(len(b))[::-1], zip(a, b)):
        result += (k := int(a)**i * int(b))
    return result

def solve(data):
    # for l in data:

    result = 0


    for (a, b) in data:
        a *= len(b)
        a = a[-len(b):]
        z = iso2(a, b)
        for k in range(1, int(b)):
            if iso2(a, str(k)) == z:
                break
        else:
            result += z
        print(result)

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q03_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
