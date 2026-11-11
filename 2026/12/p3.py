from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import batched, chain, cycle, islice, pairwise, combinations, product, takewhile, zip_longest
from heapq import heappop, heappush
from math import inf
from operator import itemgetter
from re import findall
from typing import NamedTuple

directions = ()
directions += ( 0,  1), ( 1,  0), ( 0, -1), (-1,  0)
# directions += ( 1,  1), ( 1, -1), (-1, -1), (-1,  1)


def parse(s):

    grid = {}
    # grid = []

    for y, line in enumerate(lines:=s.splitlines()):

        # digits = tuple(map(int, findall(r"\d+", line)))
        # grid.append(digits)
        # grid.append(line)

        for x, c in enumerate(line):
            if c == ".":
                continue

            grid[x, len(lines)-y] = c

    return grid


def solve(data):

    result = 0

    # print(data)

    groups = []

    seen = set()
    for p in data:
        if p in seen: continue

        group = set()
        left = [p]
        while left:
            curr = x, y = left.pop()
            if curr not in data: continue
            if curr in group: continue
            group.add(curr)
            for dx, dy in directions:
                np = nx, ny = x+dx, y+dy
                left.append(np)

        seen.update(group)
        groups.append(group)


        lo_x = min(map(itemgetter(0), group))
        lo_y = min(map(itemgetter(1), group))
        hi_x = max(map(itemgetter(0), group))
        hi_y = max(map(itemgetter(1), group))

        corners = (lo_x, lo_y), (lo_x, hi_y), (hi_x, lo_y), (hi_x, hi_y)
        missing = None
        for i, c in enumerate(corners):
            if c not in group:
                assert not missing
                missing = i

        w = hi_x - lo_x + 1
        h = hi_y - lo_y + 1
        if missing is None:
            for p in product(range(lo_x+1, hi_x), range(lo_y+1, hi_y)):
                if p not in group:
                    break
            else:
                lo = min(w, h)
                result += lo
                # print(lo)
                continue

            left = [p]
            hole = set()
            while left:
                curr = x, y = left.pop()
                if curr in hole: continue
                if curr in group: continue
                hole.add(curr)
                for dx, dy in directions:
                    np = nx, ny = x+dx, y+dy
                    left.append(np)
            print("MISSING MIDDLE")


            m_lo_x = min(map(itemgetter(0), hole))
            m_lo_y = min(map(itemgetter(1), hole))
            m_hi_x = max(map(itemgetter(0), hole))
            m_hi_y = max(map(itemgetter(1), hole))

            print(m_lo_x, m_lo_y, m_hi_x, m_hi_y)

            # 012
            # 3 4
            # 567
            need_to_cover = set(range(8))
            possible = [
                ({0, 1, 2}, hi_y - m_hi_y),
                ({1}, m_hi_x - m_lo_x + 1),
                ({6}, m_hi_x - m_lo_x + 1),
                ({5, 6, 7}, m_lo_y - lo_y),

                ({0, 3, 5}, m_lo_x - lo_x),
                ({3}, m_hi_y - m_lo_y + 1),
                ({4}, m_hi_y - m_lo_y + 1),
                ({2, 4, 7}, hi_x - m_hi_x),
            ]

            best = inf
            for number_used, _ in enumerate(possible, 1):
                for used in combinations(possible, r=number_used):
                    if need_to_cover - set(chain.from_iterable(map(itemgetter(0), used))):
                        continue

                    best = min(best, sum(map(itemgetter(1), used)))
            result += best


            insides = set()
            for x, y in group:
                if x not in range(m_lo_x, m_hi_x+1): continue
                if y not in range(m_lo_y, m_hi_y+1): continue
                insides.add((x, y))

            result += solve(insides)


            continue




        group = [(x-lo_x, y-lo_y) for x, y in group]

        # print(f"{missing = }")

        if missing == 0:
            group = [(x, y) for x, y in group]
        if missing == 1:
            group = [(x, -y) for x, y in group]
        if missing == 2:
            group = [(-x, y) for x, y in group]
        if missing == 3:
            group = [(-x, -y) for x, y in group]

        lo_x = min(map(itemgetter(0), group))
        lo_y = min(map(itemgetter(1), group))
        hi_x = max(map(itemgetter(0), group))
        hi_y = max(map(itemgetter(1), group))
        group = [(x-lo_x, y-lo_y) for x, y in group]
        lo_x = min(map(itemgetter(0), group))
        lo_y = min(map(itemgetter(1), group))
        hi_x = max(map(itemgetter(0), group))
        hi_y = max(map(itemgetter(1), group))

        w = hi_x - lo_x + 1
        h = hi_y - lo_y + 1

        # print(sorted(group, key=lambda x:(x[1],x[0])))

        for i, x in enumerate(range(lo_x, hi_x+1)):
            if (x, lo_y) in group:
                break
        i = w - i

        for j, y in enumerate(range(lo_y, hi_y+1)):
            if (lo_x, y) in group:
                break
        j = h - j

        # print(i, j, "gives", w, h, i+j)

        lo = min(w, h, i+j)
        result += lo

    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q12_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
