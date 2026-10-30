from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import chain, count, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from operator import itemgetter
from re import findall

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

from itertools import batched
def parse(s):
    # return (tuple(map(int, s.split(","))))
    result = []
    for batch in batched(findall(r"\d+", s), 4):
        result.append(tuple(map(int, batch)))
    return result

    return data, s.splitlines()

def solve(data):
    # for l in data:

    result = 0
    ids = defaultdict(list)

    points = defaultdict(int)

    solves = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    time_for = {}
    for a, b ,c , d in data:
        time_for[a, b, c] = d

    for a, b ,c , d in data:
        for k in range(1, c):
            d += time_for[a, b, k]
        solves[b][c][d].append(a)

    print(solves)
    for quest in solves.values():
        for part, solve in quest.items():
            print(solve)
            solve = sorted(solve.items())

            left = part * 50
            for (_, people) in solve:
                tmp = max(0, left)
                for person in people:
                    print(person, tmp)
                    points[person] += tmp
                    left -= 1
                # print(reward, people)
            # print(part, solve)

    # for k, v in ids.items():
    #     # print(v)
    #     ids[k] = -len(v), sum(v)

    buckets = defaultdict(list)
    for person, score in points.items():
        buckets[score].append(person)

    # print(buckets)

    place = 1
    for weight, people in sorted(buckets.items(), reverse=True):
        print(place, weight, len(people))
        result += place * weight * len(people)
        place += len(people)

    # print(buckets)
    # z = sorted(points.items(), key=lambda x: x[1])
    # print(z)
    # for i, (_, t) in enumerate(z, 1):
    #     result += i*t

    # result = 0
    # for (a, b) in data:
    #     for i, (a, b) in zip(range(4)[::-1], zip(a, b)):
    #         result += int(a)**i * int(b)
        # i, (x, y) in zip(range(4)[::-1], data)
        # for?
        # print(i, *zip(a, b))  # noqa: F821

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q04_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
