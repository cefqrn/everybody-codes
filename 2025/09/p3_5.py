from dsu import DisjointSetUnion

from itertools import combinations

def parse_dna(dna):
    result = 0
    for c in dna:
        result = (result << 4) | (1 << "ATCG".index(c))

    return result

def parse(s):
    result = []

    dna_length = None
    for x in s.splitlines():
        a, b = x.split(":", 1)
        dna_length = len(b)
        result.append((
            int(a),
            parse_dna(b)))

    return dna_length, result

def solve(parsed_input):
    dna_length, ducks = parsed_input

    families = DisjointSetUnion(len(ducks))
    for (j, parent_a), (k, parent_b) in combinations(ducks, 2):
        allowed = parent_a | parent_b
        for (i, potential_child) in ducks:
            if i in (j, k):
                continue

            curr_parents = allowed
            curr_child   = potential_child
            for _ in range(dna_length):
                if not (curr_child & 0xf & curr_parents):
                    break

                curr_child   >>= 4
                curr_parents >>= 4
            else:
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
