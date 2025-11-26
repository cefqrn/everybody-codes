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
    for k in s.split("\n\n"):
        a, *b = k.splitlines()
        # print(a, b, findall(r"\d+", a))
        plant, plant_thickness = map(int, findall(r"\d+", a))

        incoming = defaultdict(int)
        incoming["thickness"] = plant_thickness
        for x in b:
            if "free" in x:
                t, = map(int, findall(r"\d+", x))
                incoming["free"] = t
                continue

            other, branch_thickness = map(int, findall(r"\d+", x))
            incoming[other] = branch_thickness

        data[plant] = incoming

    return data

from functools import cache
def solve(data):
    incoming = data
    print(incoming)

    @cache
    def get_energy(plant):
        result = 0

        for x, t in incoming[plant].items():
            if x == "free":
                result += t
            elif x == "thickness":
                thickness = t
            else:
                result += t * get_energy(x)

        if result < thickness:
            return 0

        return result

    # print(get_energy(6))

    plant = tuple(data)[-1]
    return get_energy(plant)


if __name__ == "__main__":
    with open("everybody_codes_e2025_q18_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
