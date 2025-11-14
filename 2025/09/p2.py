from functools import partial
from itertools import pairwise, product,starmap,combinations, permutations


from operator import contains, eq, contains


def is_child_of(a,b,c):
    for x, y, z in zip(a,b,c):
        if z not in {x,y}:
            return False

    return True
    # return all(map(partial(contains, tuple(zip(a,b))), c))

def parse(s):
    result = []
    for x in s.splitlines():
        a, b = x.split(":",1)
        result.append(b)

    return result

def similarity(a,b):
    return sum(map(eq, a,b))

def solve(parsed_input):
    result = 0
    for a, b, c in permutations(parsed_input, 3):
        # print(a,b,c)
        if is_child_of(a,b,c):
            result += similarity(c,a) * similarity(c,b)
            print(a,b,c)

    return result//2


if __name__ == "__main__":
    with open("everybody_codes_e2025_q09_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))

