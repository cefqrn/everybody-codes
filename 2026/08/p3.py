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

class Position:
    def __init__(self, c, x, y):
        self.x = x
        self.y = y
        self.c = int(c) if c.isdigit() else c
    def __str__(self): return f"{self.c:2}"
    __repr__ = __str__


from itertools import batched
def parse(s):

    # grid = {}
    grid = []
    for y, line in enumerate(s.splitlines()):
        line = [Position(c, x, y) for x, c in enumerate(line)]
        grid.append(line)
    #     for x, c in enumerate(line):
    #         grid[x, y] = c


    return grid

grown = 0
def count_lights(lines):
    global grown
    result = 0
    for line in lines:
        amount = 0
        highest = 0
        for x in line:
            if x.c == ".": continue

            highest -= 1

            if x.c <= 0:
                x.c += 1
                continue

            if x.c > highest:
                amount += x.c > highest
                highest = max(x.c, highest)
                x.c += 1
                if x.c == 10:
                    x.c = -2
                    grown += 1

        result += amount
    return result


def solve_d(data, initial_reversal, i):
    target_reversal = not initial_reversal
    reversal = initial_reversal

    # print(data)

    new_data = []
    for l in data:
        dots = tuple(takewhile(lambda x: x.c == ".", l))

        if reversal:
            l = l[len(dots):]
        else:
            l = l[:len(dots)] + l
        new_data.append(l)

        if not dots:
            reversal = target_reversal

    lines = tuple(zip_longest(*new_data, fillvalue=Position(".", 999, 999)))
    # print(*lines, sep="\n")

    if i:
        return count_lights(map(reversed, lines))
    else:
        return count_lights(lines)

def solve_e(data, i):
    match i:
        case 0: return solve_d(data, False, 0)
        case 1: return solve_d(data, True , 0)
        case 2: return count_lights(map(reversed, data))
        case 3: return solve_d(data, False, 1)
        case 4: return solve_d(data, True , 1)
        case 5: return count_lights(data)


def solve(data):
    result = 0

    # while result <= 

    for i in cycle(range(6)):
        prev=  result
        result += solve_e(data, i)
        # if grown >= 100:
        #     break
        if grown >= 100000:
            break

        # print(result - prev)
        # print(*data, sep="\n")

    # reversal = False

    # a, b = solve_d(data, True)
    # c, d = solve_d(data, False)

    # e = count_lights(data)
    # f = count_lights(map(reversed, data))

    # print(a, b, c, d, e, f)
    # result = a + b + c + d + e + f

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2026_q08_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
