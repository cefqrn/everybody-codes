from bisect import bisect_left, bisect_right
from collections import deque, defaultdict
from functools import partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from re import findall

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

def parse(s):
    result = []
    data = defaultdict(lambda: defaultdict(int))
    s, test_cases = s.split("\n\n\n")

    rtest_cases = []
    for l in test_cases.splitlines():
        rtest_cases.append(tuple(map(int, findall(r"-?\d+", l))))


    free_branches = []
    for k in s.split("\n\n"):
        a, *b = k.splitlines()
        plant, plant_thickness = map(int, findall(r"-?\d+", a))

        incoming = defaultdict(int)
        incoming["thickness"] = plant_thickness
        for x in b:
            if "free" in x:
                t, = map(int, findall(r"-?\d+", x))
                incoming["free"] = t
                free_branches.append(plant)
                continue

            other, branch_thickness = map(int, findall(r"-?\d+", x))
            incoming[other] = branch_thickness

        data[plant] = incoming

    return data, free_branches, rtest_cases

from functools import cache
def solve(data):
    incoming, free_branches, test_cases = data

    def maximize(plant):
        result = 0
        for x, t in incoming[plant].items():
            if x == "free":
                print(plant, "max")
                return 1

            if x == "thickness":
                thickness = t
                continue

            if t < 0:
                result += minimize(x) * t
            else:
                result += maximize(x) * t

        if result < thickness:
            return 0

        return result

    def minimize(plant):
        result = 0
        for x, t in incoming[plant].items():
            if x == "free":
                print(plant, "min")
                return 0

            if x == "thickness":
                thickness = t
                continue

            if t < 0:
                result += maximize(x) * t
            else:
                result += minimize(x) * t

        if result < thickness:
            return 0

        return result


    def with_case(test_case):
        @cache
        def get_energy(plant):
            result = 0

            for x, t in incoming[plant].items():
                if x == "free":
                    result += t * test_case[free_branches.index(plant)]
                elif x == "thickness":
                    thickness = t
                else:
                    result += t * get_energy(x)

            if result < thickness:
                return 0

            return result

        result = get_energy(tuple(incoming)[-1])

        return result

    plant = tuple(incoming)[-1]
    best = maximize(plant)

    print(best)


    # result = 0
    # for test_case in test_cases:
    #     result += with_case(test_case)
    # return result


if __name__ == "__main__":
    with open("everybody_codes_e2025_q18_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
