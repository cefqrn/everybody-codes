from dsu import DisjointSetUnion

from itertools import combinations

def parse(s):
    result = []

    for x in s.splitlines():
        a, b = x.split(":", 1)
        result.append((
            int(a),
            b.encode().translate(
                bytes.maketrans(b"ATCG", bytes(range(4))))))

    return result

def solve(parsed_input):
    possibilities = []  # trie
    for i, dna in parsed_input:
        curr = possibilities
        for c in dna:
            if not curr:
                curr += [], [], [], []

            curr = curr[c]

        curr.append(i)

    families = DisjointSetUnion(len(parsed_input))
    for (j, parent_a), (k, parent_b) in combinations(parsed_input, 2):
        left = [(possibilities, parent_a, parent_b)]
        while left:
            curr, a, b = left.pop()

            if a:  # and b
                if ncurr := curr[a[0]]:
                    left.append((ncurr, a[1:], b[1:]))
                if b[0] != a[0] and (ncurr := curr[b[0]]):
                    left.append((ncurr, a[1:], b[1:]))
            else:
                i, = curr
                if i not in (j, k):
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
