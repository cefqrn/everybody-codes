from functools import partial
from itertools import pairwise, product,starmap


from operator import contains, eq

def parse(s):
    return tuple(map(int, s.split()))



def solve(parsed_input):
    ducks = list(parsed_input)
    k = 10


    r = 0
    for r in range(r, k+1):
        prev_ducks = ducks.copy()
        for i, j in pairwise(range(len(ducks))):
            x = ducks[i]
            y = ducks[j]
            if x > y:
                ducks[i] -= 1
                ducks[j] += 1
        if ducks == prev_ducks:
            break

    for r in range(r+1, k+1):
        # print(r)
        for i, j in pairwise(range(len(ducks))):
            x = ducks[i]
            y = ducks[j]
            if x > y:
                ducks[i] -= 1
                ducks[j] += 1
            elif x < y:
                ducks[i] += 1
                ducks[j] -= 1

    #     print(ducks)


    # print(ducks)

    result = 0
    for i, c in enumerate(ducks, 1):
        result += i*c

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2025_q11_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))

