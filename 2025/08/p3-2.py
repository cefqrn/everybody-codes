from collections import defaultdict
from functools import partial
from itertools import chain, combinations, filterfalse, pairwise, starmap
from operator import getitem, contains

def iter_len(it):
    return sum(1 for _ in it)

def count_cut(connections_from, a, b):
    a, b = sorted([a, b])

    between_range = range(a, b+1)
    return (b in connections_from[a]) \
         + iter_len(filterfalse(
               partial(contains, between_range),
               chain.from_iterable(
                   map(partial(getitem, connections_from), range(a+1, b)))))

if __name__ == "__main__":
    with open("everybody_codes_e2025_q08_p3.txt") as f:
        order = f.read().strip()

    order = eval(order)

    k = [8, 256][len(order) > 20]

    connections_from = defaultdict(list)

    for a, b in pairwise(order):
        connections_from[a].append(b)
        connections_from[b].append(a)

    print(max(starmap(
        partial(count_cut, connections_from),
        combinations(range(1, k+1), 2))))
