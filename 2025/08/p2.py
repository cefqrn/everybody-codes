from functools import partial
from itertools import pairwise, product
from operator import contains

from collections import defaultdict
k = 256
# k = 8

if __name__ == "__main__":
    with open("everybody_codes_e2025_q08_p2.txt") as f:
        order = f.read().strip()

    order = tuple(map(int, order.split(",")))

    connections = defaultdict(set)

    knots = 0
    for a, b in map(sorted, pairwise(order)):
        r = range(a, b+1)
        for x in range(a+1, b):
            for out in connections[x]:
                knots += out not in r

        connections[a].add(b)
        connections[b].add(a)

    print(knots)


    # print(len(order), len(set(pairwise(order))))



    # for a, b in pairwise(order):
    #     print(abs(b-a), k//2)

    # print(sum(abs(b-a) == k//2 for a, b in pairwise(order)))
