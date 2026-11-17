from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import batched, chain, count, cycle, groupby, islice, pairwise, combinations, product, takewhile, zip_longest
from heapq import heappop, heappush
from math import comb, inf
from operator import itemgetter, mul
from re import findall
from typing import NamedTuple

directions = ()
directions += ( 0,  1), ( 1,  0), ( 0, -1), (-1,  0)
# directions += ( 1,  1), ( 1, -1), (-1, -1), (-1,  1)


def parse(s):

    # grid = {}
    grid = []

    for y, line in enumerate(s.splitlines()):

        # digits = tuple(map(int, findall(r"\d+", line)))
        # grid.append(digits)
        # grid.append(line)

        # for x, c in enumerate(line):
        #     if c == ".":
        #         continue

        #     grid[x, y] = c

        ...

    return s

    return grid


def solve(data):

    result = 0

    groups = deque(data) * 100

    # groups = ([k for k, _ in groupby(data)])
    # print(groups)

    # groups = list(data)
    # print("".join(groups), result)

    pop_side = deque([deque.popleft, deque.pop])
    append_side = deque([deque.appendleft, deque.append])

    side = 0

    left = deque()
    while groups:
        # print(result, "".join(groups)[::1|-side])
        print(result)
        init = pop_side[side](groups)
        while (k := pop_side[side](groups)) == init: ...
        append_side[side](groups, k)
        while groups:
            offset = 0
            try:
                while (k := pop_side[1-side](groups)) != init:
                    append_side[0](left, k)
                offset += 1
                # print("K", "".join(groups)[::1|-side], "".join(left))

                while (k := pop_side[1-side](groups)) == init:
                    offset += 1
                append_side[1-side](groups, k)
            except IndexError:
                break

            result += len(groups) + offset
            side = 1-side
            # result += 1

            # print(init, "".join(groups)[::1|-side])

            # pop_side.rotate()
            # append_side.rotate()
        # side = 0
        groups, left = left, groups

        # groups.popleft()
        # if not groups:

    # print(data)
    # while lo <= hi:
    #     if data[lo] != data[hi]:
    #         result += 1



    # for _ in data:



    #     ...

    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q16_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
