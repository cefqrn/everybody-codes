from heapq import nlargest
from itertools import permutations
from math import prod
from typing import Counter


directions = ()
directions += ( 0,  1), ( 1,  0), ( 0, -1), (-1,  0)
# directions += ( 1,  1), ( 1, -1), (-1, -1), (-1,  1)

directions_arrows = "^>v<"


def parse(s):

    return Counter(c for c in s if not c.isspace())


def solve(data):
    print(data)

    a, b, c = sorted([data["C"], data["M"], data["Y"]])

    d, r = divmod(a + b + c, 3)

    return (d + (r > 0)) * (d + (r > 1)) * d



if __name__ == "__main__":
    with open("everybody_codes_e2026_q19_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
