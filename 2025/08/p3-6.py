from bisect import bisect_left, bisect_right
from collections import defaultdict
from itertools import combinations, pairwise

def count_cut(connections_from, a, b):
    a, b = sorted([a, b])

    cut = b in connections_from[a]
    for x in range(a+1, b):
        l = connections_from[x]
        cut += len(l) - (bisect_right(l, b) - bisect_left(l, a))

    return cut

if __name__ == "__main__":
    with open("everybody_codes_e2025_q08_p3.txt") as f:
        order = f.read().strip()

    order = tuple(map(int, order.split(",")))

    k = [8, 256][len(order) > 20]

    connections_from = defaultdict(list)
    for a, b in pairwise(order):
        connections_from[a].append(b)
        connections_from[b].append(a)

    for l in connections_from.values():
        l.sort()

    best = 0
    for a, b in combinations(range(1, k+1), r=2):
        cut = count_cut(connections_from, a, b)
        best = max(best, cut)

    print(best)
