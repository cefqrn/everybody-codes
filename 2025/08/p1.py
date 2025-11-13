from functools import partial
from itertools import pairwise, product
from operator import contains

if __name__ == "__main__":
    with open("everybody_codes_e2025_q08_p1.txt") as f:
        order = f.read().strip()

    order = tuple(map(int, order.split(",")))

    k = 32

    for a, b in pairwise(order):
        print(abs(b-a), k//2)

    print(sum(abs(b-a) == k//2 for a, b in pairwise(order)))
