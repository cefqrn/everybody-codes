from collections import defaultdict
from itertools import pairwise
from collections import Counter

if __name__ == "__main__":
    with open("everybody_codes_e2025_q08_p3.txt") as f:
        order = f.read().strip()

    order = tuple(map(int, order.split(",")))

    k = [8, 256][len(order) > 20]

    connections_from = defaultdict(list)

    result = Counter()
    for a, b in pairwise(order):
        a, b = sorted([a, b])

        result[a, b] += 1
        result[b, a] += 1
        for m in range(a+1, b):
            for n in range(1, a):
                result[m, n] += 1
                result[n, m] += 1

            for n in range(b+1, k+1):
                result[m, n] += 1
                result[n, m] += 1

    print(result.most_common(1))