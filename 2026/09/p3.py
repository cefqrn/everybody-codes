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

    for i, l in enumerate(data):
        _, growth, limit = l
        branches = Counter({0: 1})

        if limit == 1:
            steps = 1
        else:
            steps = 0
            split_points = 1
            while (els := split_points) < limit:
                # print("hi", els, branches)
                new_branches = Counter()
                skip = growth - max(branches)
                for b, v in branches.items():
                    b += skip
                    if b == growth:
                        new_branches[b//2] += v * 2
                        new_branches[1] += v
                        split_points += v
                    else:
                        new_branches[b] += v
                branches = new_branches
                steps += skip

            # print(split_points)

        print(f"{steps}, {(i+1)/len(data):.2%}")
        # print("hi", els)

        # if i > 2:
        #     break

        result += steps
        # print(steps)





    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q09_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
