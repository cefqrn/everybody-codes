from functools import partial
from itertools import pairwise, product, starmap
from operator import eq
from collections import deque

def parse(s):
    clock = deque([1])

    i = 0
    for i, x in enumerate(map(int, s.splitlines())):
        if i & 1:
            clock.append(x)
        else:
            clock.appendleft(x)

    clock.rotate(-i//2)

    # print(clock)

    return clock

def solve(data):
    data.rotate(2025)
    return data.popleft()

if __name__ == "__main__":
    with open("everybody_codes_e2025_q13_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
