from collections import defaultdict
from functools import partial
from itertools import chain, combinations, filterfalse, pairwise
from operator import getitem, contains

def iter_len(it):
    return sum(1 for _ in it)

def between(k, a, b):
    if a < b:
        return range(a+1, b)
    else:
        return chain(range(1, b), range(a+1, k+1))

def in_between(a, b, x):
    return a <= x <= b or b <= a and (x <= b or a <= x)

def count_cut(connections_from, a, b):
    return (b in connections_from[a]) \
         + iter_len(filterfalse(
               partial(in_between, a, b),
               chain.from_iterable(
                   map(partial(getitem, connections_from), between(k, a, b)))))

if __name__ == "__main__":
    with open("everybody_codes_e2025_q08_p3.txt") as f:
        order = f.read().strip()

    order = tuple(map(int, order.split(",")))

    k = [8, 256][len(order) > 20]

    connections_from = defaultdict(list)

    for a, b in pairwise(order):
        connections_from[a].append(b)
        connections_from[b].append(a)

    best = -9
    for a, b in combinations(range(1, k+1), r=2):
        cut = count_cut(connections_from, a, b)
        best = max(best, cut)

    print(best)
