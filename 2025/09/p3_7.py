from dsu import DisjointSetUnion

from operator import itemgetter

def parse_dna(dna):
    return bytes(1 << "ATCG".index(c) for c in dna)

def parse(s):
    result = []

    for x in s.splitlines():
        a, b = x.split(":", 1)
        result.append((
            int(a),
            parse_dna(b)))

    return result

def similarity(a, b):
    # return sum(map(eq, a, b))
    result = 0
    for i in range(len(a)):
        result += a[i] == b[i]

    return result

def solve(ducks):
    families = DisjointSetUnion(len(ducks))
    for (i, potential_child) in ducks:
        sorted_ducks = sorted(
            ((similarity(potential_child, duck), j, duck)
                for j, duck in ducks),
            key=itemgetter(0))

        l = len(potential_child)
        r = range(l)
        for sj, j, parent_a in sorted_ducks:
            for sk, k, parent_b in reversed(sorted_ducks):
                if i in (j, k) or j == k:
                    continue

                if sj + sk < l:
                    break

                # if all(map(lambda x, a, b: x in (a, b), potential_child, parent_a, parent_b)):
                for x in r:
                    if potential_child[x] not in (parent_a[x], parent_b[x]):
                        break
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
