from bisect import bisect_left, bisect_right
from collections import deque, defaultdict
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from re import findall

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

def parse(s):
    return sorted(eval(s))

def solve(data):
    
    result = 0
    return sum(sorted(set(data))[:20])

if __name__ == "__main__":
    with open("everybody_codes_e2025_q03_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
