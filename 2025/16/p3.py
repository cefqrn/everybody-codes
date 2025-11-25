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


def solve1(data, length):
    # result = sum((length - (x-1)) // x for x in data)
    expected = sum(len(range(x-1, length, x)) for x in data)
    # print(result, expected)
    # assert result == expected

    return expected
    # length // x
    # return sum(len(range(x-1, length, x)) for x in data)

N = 202520252025000
# N = 100
@cache
def solve(data):
    spells = solve2(data)
    # print(solve1(spells, 90))

    def can_solve(data, length):
        return solve1(spells, length) <= N

    hi = 99999999999999999
    lo = 1
    while hi > lo:
        mid = (hi + lo) // 2
        if can_solve(data, mid):
            lo = mid + 1
        else:
            hi = mid - 1

    for i in range(lo-5, hi+5):
        print(i, can_solve(..., i))

    # print(can_solve(data, 48))
    # print(solve1(data, 47))

    print(lo, hi)


    # if solve(solve1, spells)
    # return bisect_right(range(1, 9999999999999999999), False, key=partial(solve1, spells))

    # return solve1(solve2(data), 10)


if __name__ == "__main__":
    with open("everybody_codes_e2025_q16_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
