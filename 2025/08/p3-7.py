from bisect import bisect_left, bisect_right
from collections import defaultdict
from itertools import pairwise

def main():
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
    for a in range(1, k+1):
        curr = 0
        for b in range(a+2, k+1):
            l1 = connections_from[b]
            curr -= bisect_left(l1, b-1) - (i := bisect_right(l1, a))

            l2 = connections_from[b-1]
            curr += len(l2) - (bisect_right(l2, b) - bisect_left(l2, a))

            with_current = curr + (i and l1[i-1] == a)

            best = max(best, with_current)

    print(best)

if __name__ == "__main__":
    main()
