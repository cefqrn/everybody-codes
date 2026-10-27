from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from re import findall

from itertools import batched

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

def parse(s):
    result = []
    for line in s.splitlines():
        result.append(line_result := [])
        for order in line.split():
            try:
                a, b = map(int, order.split("<"))
            except ValueError:
                b, a = map(int, order.split(">"))
            line_result.append((a, b))

    return result

    return data, s.splitlines()

def solve(data):
    # for l in data:

    # print(data)

    result = 0

    from itertools import permutations

    for line in map(sorted, data):
        ins = defaultdict(set)
        outs = defaultdict(set)
        clean = set(chain.from_iterable(line))
        for a, b in line:
            ins[b].add(a)
            if b in clean:
                clean.remove(b)
            outs[a].add(b)

        order = []
        while clean:
            z = clean.pop()
            order.append(z)
            for out in outs[z]:
                ins[out].remove(z)
                if not ins[out]:
                    clean.add(out)

        result += int("".join(map(str, order))[::-1])

    return result

if __name__ == "__main__":
    for part in 1, 2, 3:
        with open(f"everybody_codes_e2026_q02_p{part}.txt") as f:
            data = parse(f.read().strip())

        print(solve(data))
