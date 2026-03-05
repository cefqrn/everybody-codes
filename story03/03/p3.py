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
            if k == "leftSocket":
                z["lOld"] = v
            if k == "rightSocket":
                z["rOld"] = v

        data[z["id"]] = z
        # print(line.split(", "))

    return data

def traverse(tree):
    left = tree["leftSocket"]
    right = tree["rightSocket"]
    if isinstance(left, str):
        yield tree, tree["lOld"], "leftSocket", None
    else:
        z = yield tree, tree["lOld"], "leftSocket", left
        # z = yield
        print("gota", z)

        yield
        if not z:
            yield from traverse(left)
        else:
            print("got displaced, ignoring")

    print("@", tree["id"])

    if isinstance(right, str):
        yield tree, tree["rOld"], "rightSocket", None
    else:
        z = yield tree, tree["rOld"], "rightSocket", right
        # z = yield
        print("gota", z)

        yield
        if not z:
            yield from traverse(right)
        else:
            print("got displaced, ignoring")


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

    # for other in rest:
    left = deque(rest)

    while left:
        other = left.popleft()

        looking_for = other["plug"]
        it = traverse(root)
        print("placing", other["id"])
        for t, v, location, displaced in it:
            print(v, looking_for, location, t["id"])
            if len(set(looking_for.split()) & set(v.split())) == 2:
                if not displaced or displaced["plug"] != v:
                    t[location] = other
                    if displaced:  # move the thingy
                        other = displaced
                        looking_for = other["plug"]
                        print("DISPLACING", other["id"])
                        it.send(True)
                        continue
                    else:
                        break
                else:
                    print("didn't add strong")

            if displaced:
                it.send(False)

            if not displaced and (set(looking_for.split()) & set(v.split())):
                t[location] = other
                break
        else:
            left.appendleft(other)
            # raise ValueError

    #     break

        from pprint import pp
        pp(root)

        print()
        print()
        print()
        print()

    # print(*traverse(root))

    # print(root)

    # _, k = traverse(root)
    # print(k)
    # print(root)
    # for v in rest:
    #     print(v)

    return checksum(root, 1)

if __name__ == "__main__":
    with open("everybody_codes_e3_q03_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
