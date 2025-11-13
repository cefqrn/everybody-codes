from collections import defaultdict
from functools import partial
from itertools import chain, combinations, filterfalse, pairwise, product, tee
from operator import getitem, contains
from collections import Counter

def split(a, b):
    a, b = sorted([a, b])
    return range(a+1, b), tuple(chain(range(1, a), range(b+1, k+1)))

if __name__ == "__main__":
    with open("everybody_codes_e2025_q08_p3.txt") as f:
        order = f.read().strip()

    order = tuple(map(int, order.split(",")))

    k = [8, 256][len(order) > 20]

    connections_from = defaultdict(list)

    result = Counter()
    for a, b in pairwise(order):
        x, y = split(a, b)

        result += Counter(chain(product(x, y), product(y, x)))
        result[a, b] += 1
        result[b, a] += 1

    print(result.most_common(1))