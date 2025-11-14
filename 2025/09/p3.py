from functools import partial
from itertools import pairwise, product,starmap,combinations, permutations


from operator import contains, eq, contains


def is_child_of(a,b,c):
    for x, y, z in zip(a,b,c):
        if z not in {x,y}:
            return False

    return True
    # return all(map(partial(contains, tuple(zip(a,b))), c))

from collections import defaultdict


def parse(s):
    result = []

    for x in s.splitlines():
        a, b = x.split(":",1)
        result.append((a,b))

    return result

def similarity(a,b):
    return sum(map(eq, a,b))

def get_families(connections):
    left = set(connections)
    families = []
    while left:
        family = set()
        remaining = [left.pop()]
        while remaining:
            curr = remaining.pop()
            family.add(curr)
            for x in connections[curr]:
                if x in left:
                    left.remove(x)
                    remaining.append(x)

        families.append(family)

    print(families[0])
    return families

def solve(parsed_input):
    result = 0

    connections = defaultdict(set)
    for a, b, c in permutations(parsed_input, 3):
        if is_child_of(a[1],b[1],c[1]):
            connections[a] |= {b,c}
            connections[b] |= {a,c}
            connections[c] |= {a,b}

    return sum(int(i) for i, _ in max(get_families(connections), key=len))
    # print(*map(len, get_families(connections)))

    # return result//2


if __name__ == "__main__":
    with open("everybody_codes_e2025_q09_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
