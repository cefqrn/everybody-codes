from functools import partial
from itertools import pairwise, product,starmap, count


from operator import contains, eq

def parse(s):
    return tuple(map(int, s.split()))



def solve(parsed_input):
    ducks = list(parsed_input)

    for result in count():
        is_sorted = True
        for i, j in pairwise(range(len(ducks))):
            x = ducks[i]
            y = ducks[j]
            if x > y:
                ducks[i] -= 1
                ducks[j] += 1
                is_sorted = False
        if is_sorted:
            break

    print("sorted in", result)

    expected = sum(ducks) // len(ducks)
    assert expected*len(ducks) == sum(ducks)

    debt = 0

    for x in ducks:
        if x < expected:
            # debt += 
            result += expected - x

    return result

if __name__ == "__main__":
    with open("everybody_codes_e2025_q11_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))

