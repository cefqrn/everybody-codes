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
        result.append((int(a), b))

    return result

def similarity(a, b):
    return sum(map(eq, a, b))

def solve(parsed_input):
    families = DisjointSetUnion(len(parsed_input))
    for (i, possible_child) in parsed_input:
        parents_by_similarity = sorted(
            parsed_input,
            key=lambda parent: similarity(possible_child, parent[1]),
            reverse=True)
        for (j, parent_a), (k, parent_b) in combinations(parents_by_similarity, 2):
            if i in (j, k):
                continue

            if is_child_of(parent_a, parent_b, possible_child):
                families.union(i-1, j-1)
                families.union(i-1, k-1)
                break

    family_sets = families.to_sets()
    biggest_family = max(family_sets, key=len)
    return sum(i+1 for i in biggest_family)

if __name__ == "__main__":
    with open("everybody_codes_e2025_q09_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
