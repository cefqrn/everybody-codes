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

    data = []
    for line in s.splitlines():
        data.append(eval(line))

    return data

def solve(data):
    result = 0

    for seq in data:
        seen = {curr := 0}
        for x in seq:
            new = curr - x
            if new < 0:
                new = curr + x
            elif new in seen:
                new = curr + x
            curr = new
            seen.add(new)
        result += curr

    return result

if __name__ == "__main__":
    with open("everybody_codes_e4_q01_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
