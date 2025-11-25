from functools import partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

def parse(s):
    return eval(s)

def solve(data):
    wall = [0]*90
    for x in data:
        for i in range(x-1, 90, x):
            wall[i] += 1
    result = 0
    result += sum(wall)
    return result

if __name__ == "__main__":
    with open("everybody_codes_e2025_q16_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
