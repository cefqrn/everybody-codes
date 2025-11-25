from functools import partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

def parse(s):
    return eval(s)


from functools import cache

@cache
def solve2(data, start_from=1):
    if not any(data):
        return ()

    wall = list(data)
    for i in range(start_from-1, len(data), start_from):
        wall[i] -= 1
        if wall[i] < 0:
            return None

    wall = tuple(wall)
    for x in range(start_from+1, len(data)):
        if (result := solve2(wall, x)) is not None:
            return start_from, *result

    return None

@cache
def solve(data):
    from math import prod

    return prod(solve2(data))


if __name__ == "__main__":
    with open("everybody_codes_e2025_q16_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
