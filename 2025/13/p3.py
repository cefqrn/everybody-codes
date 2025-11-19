from functools import partial
from itertools import pairwise, product, starmap
from operator import eq

from collections import deque
import p1

def parse(s):
    clock = deque([1])

    i = 0
    for i, x in enumerate(s.splitlines()):
        a, b = x.split("-")
        r = range(int(a), int(b)+1)
        if not i & 1:
            for z in r:
                clock.append(z)
        else:
            for z in r:
                clock.appendleft(z)

    clock.rotate(-clock.index(1))

    return clock

def solve(data):
    data.rotate(-202520252025)
    return data.popleft()


if __name__ == "__main__":
    with open("everybody_codes_e2025_q13_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
