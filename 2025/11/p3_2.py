from functools import partial
from operator import gt, sub
from statistics import mean

def parse(s):
    return eval(s.replace(*"\n,"))

def solve(ducks):
    expected = mean(ducks)
    return sum(map(partial(sub, expected), filter(partial(gt, expected), ducks)))

if __name__ == "__main__":
    with open("everybody_codes_e2025_q11_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))

