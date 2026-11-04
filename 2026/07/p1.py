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
        # a, b = line.split(", ")
        # f
        k = id_, energy, *connections = map(int, findall(r"\d+", line))
        result[id_] = energy, connections


    return result

def solve(data):
    result = 0

    received = defaultdict(int)
    start = max(data, key=lambda x: len(data[x][1]))

    left = [(start, 5)]
    while left:
        curr, energy = left.pop()
        received[curr] += energy
        if energy == 0:
            continue
        for connection in data[curr][1]:
            left.append((connection, energy - 1))

    print(sum(received.values()) + sum(z for z, _ in data.values()))

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q07_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
