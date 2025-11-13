from functools import partial
from itertools import combinations, pairwise, permutations
from operator import contains

from collections import defaultdict
k = 256
# k = 8


def count_cut(connections, a, b):
    a, b = sorted([a, b])

    cut = b in connections[a]

    r = range(a, b+1)
    for x in range(a+1, b):
        for out in connections[x]:
            cut += out not in r

    return cut



if __name__ == "__main__":
    with open("everybody_codes_e2025_q08_p3.txt") as f:
        order = f.read().strip()

    order = tuple(map(int, order.split(",")))

    connections = defaultdict(list)

    for a, b in pairwise(order):
        connections[a].append(b)
        connections[b].append(a)

    best = -9
    for a, b in combinations(range(1, k+1), r=2):
        cut = count_cut(connections, a, b)
        best = max(best, cut)

    print(best)
