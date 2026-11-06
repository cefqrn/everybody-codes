from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product, takewhile, zip_longest
from heapq import heappop, heappush
from math import inf
from operator import itemgetter
from re import findall

# directions = (0, 1), (1, 0), (0, -1), (-1, 0)
directions = (1, 1), (1, -1), (-1, -1), (-1, 1)

from itertools import batched
def parse(s):

    # grid = {}
    grid = []
    for y, line in enumerate(s.splitlines()):
        grid.append(tuple(map(int, findall(r"\d+", line))))
    #     for x, c in enumerate(line):
    #         grid[x, y] = c


    return grid

def solve(data):
    result = 0

    for l in data:
        _, growth, limit = l
        branches = Counter({0: 1})
        steps = 0
        split_points = 0
        while (els := split_points + sum(k*v for k, v in branches.items())) < limit:
            print("hi", els, branches)
            new_branches = Counter()
            for b, v in branches.items():
                b += 1
                if b == growth:
                    new_branches[b//2] += v * 2
                    new_branches[1] += v
                    split_points += v
                else:
                    new_branches[b] += v
            branches = new_branches
            steps += 1
        print("hi", els, branches)

        result += steps
        print(steps)





    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q09_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
