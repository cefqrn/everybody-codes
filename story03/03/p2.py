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
    data = {}

    for y, line in enumerate(s.splitlines()):
        # for x, c in enumerate(line):
        #     ...

        z = {}
        for k, v in (k.split("=", 1) for k in line.split(", ")):
            z[k] = v

        data[z["id"]] = z
        # print(line.split(", "))

    return data

def traverse(tree):
    left = tree["leftSocket"]
    right = tree["rightSocket"]
    if isinstance(left, str):
        yield tree, left, "leftSocket"
    else:
        yield from traverse(left)

    if isinstance(right, str):
        yield tree, right, "rightSocket"
    else:
        yield from traverse(right)


def checksum(tree, n):
    left = tree["leftSocket"]
    right = tree["rightSocket"]

    result = 0

    if not isinstance(left, str):
        added, n = checksum(left, n)
        result += added

    result += n*int(tree["id"])
    n += 1

    print(tree["id"])

    if not isinstance(right, str):
        added, n = checksum(right, n)
        result += added

    return result, n


def solve(data):
    result = 0

    root, *rest = data.values()

    for other in rest:
        looking_for = other["plug"]
        for t, v, location in traverse(root):
            if set(looking_for.split()) & set(v.split()):
            # print(v, looking_for)
            # if v == looking_for:
                t[location] = other
                break
        else:
            raise ValueError

    #     break

        # from pprint import pp
        # pp(root)

        # print()
        # print()
        # print()
        # print()

    # print(*traverse(root))

    # print(root)

    # _, k = traverse(root)
    # print(k)
    # print(root)
    # for v in rest:
    #     print(v)

    return checksum(root, 1)

if __name__ == "__main__":
    with open("everybody_codes_e3_q03_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
