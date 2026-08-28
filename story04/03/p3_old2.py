from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial, reduce
from itertools import chain, cycle, islice, pairwise, combinations, product, starmap
from heapq import heappop, heappush
from math import inf
from re import findall

directions = (0, -1), (1, 0), (0, 1), (-1, 0)

def parse(s):
    data = s

    data = []
    a, b, c, d = s.splitlines()
    data.append(int(a.split("=")[1]))
    data.append(int(b.split("=")[1]))
    data.append(c.split("=")[1])
    data.append(d.split("=")[1])

    return data

"""
width=30
height=10
horizontal-offsets=10011
vertical-offsets=11011
"""

def solve(data):
    result = 0

    actual_width, actual_height, horizontal_offsets, vertical_offsets = data

    for y, (a, b) in enumerate(pairwise(horizontal_offsets + horizontal_offsets[0])):
        if a != b:
            continue

        for x, (c, d) in enumerate(pairwise(vertical_offsets + vertical_offsets[0])):
            if c != d:
                continue

            if not (x ^ y ^ int(a) ^ int(c)) & 1:
                print(x, y)

    return result

if __name__ == "__main__":
    with open("everybody_codes_e4_q03_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
