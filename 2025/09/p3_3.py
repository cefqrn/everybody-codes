from dsu import DisjointSetUnion

from itertools import combinations
from operator import eq

def is_child_of(parent_a, parent_b, possible_child):
    return all(map(
        lambda a, b, x: x in (a, b),
        parent_a, parent_b, possible_child))

def parse(s):
    result = []

    for x in s.splitlines():
        a, b = x.split(":", 1)
        result.append((int(a), b.encode()))

    return result

def similarity(a, b):
    return sum(map(eq, a, b))

def solve(parsed_input):
    possibilities = {}
    for i, dna in parsed_input:
        curr = possibilities
        for c in dna:
            curr = curr.setdefault(c, {})

        curr["id"] = i

    families = DisjointSetUnion(len(parsed_input))
    for (j, parent_a), (k, parent_b) in combinations(parsed_input, 2):
        left = [(possibilities, memoryview(parent_a), memoryview(parent_b))]
        while left:
            curr, a, b = left.pop()
            if not a:  # or not b
                i = curr["id"]
                if i in (j, k):
                    continue

                families.union(i-1, j-1)
                families.union(i-1, k-1)

                continue

            for c in {a[0], b[0]}:
                if c not in curr:
                    continue

                left.append((curr[c], a[1:], b[1:]))

    family_sets = families.to_sets()
    biggest_family = max(family_sets, key=len)
    return sum(i+1 for i in biggest_family)

if __name__ == "__main__":
    from time import perf_counter
    st = perf_counter()

    with open("everybody_codes_e2025_q09_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
    print(perf_counter() - st)

