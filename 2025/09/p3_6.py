from dsu import DisjointSetUnion

from itertools import combinations
from operator import and_, or_

def parse_dna(dna):
    return bytes(1 << "ATCG".index(c) for c in dna)

def parse(s):
    result = []

    for x in s.splitlines():
        a, b = x.split(":", 1)
        result.append((
            int(a),
            b.encode().translate(bytes.maketrans(b"ATCG", b"\x01\x02\x04\x08"))))

    return result

def solve(ducks):
    families = DisjointSetUnion(len(ducks))
    for (j, parent_a), (k, parent_b) in combinations(ducks, 2):
        fused_parents = bytes(map(or_, parent_a, parent_b))
        for (i, potential_child) in ducks:
            if i in (j, k):
                continue

            if not all(map(and_, potential_child, fused_parents)):
                continue

            families.union(i-1, j-1)
            families.union(i-1, k-1)

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
