from heapq import nlargest
from math import prod
from typing import Counter


directions = ()
directions += ( 0,  1), ( 1,  0), ( 0, -1), (-1,  0)
# directions += ( 1,  1), ( 1, -1), (-1, -1), (-1,  1)

directions_arrows = "^>v<"


def parse(s):

    # grid = {}
    grid = []

    a, b = s.split("\n\n")

    return a, b

    # for y, line in enumerate(s.splitlines()):

        # digits = tuple(map(int, findall(r"\d+", line)))
        # grid.append(digits)
        # grid.append(line)

        # for x, c in enumerate(line):
        #     if c == ".":
        #         continue

        #     grid[x, y] = c


    return grid


def solve(data):

    result = 0

    a, b = data

    counts = Counter()
    for x, y in map(sorted, zip(a, b)):
        if x == "\n": continue
        match x, y:
            case "\n", "\n": c = "\n"
            case "K", _:     c = "K"
            case _, "K":     c = "K"
            case "C", "M":   c = "B"
            case "C", "Y":   c = "G"
            case "M", "Y":   c = "R"
            case c1, c2:
                if c1 != c2: raise ValueError
                c = c1
        counts[c] += 1

    result = prod(nlargest(3, counts.values()))

    # print(data)

    # for _ in data:



    #     ...

    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q19_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
