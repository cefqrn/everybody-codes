from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from re import findall

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

def parse(s):
    return list(map(eval, s.splitlines()))

def solve(data):
    pipes = defaultdict(list)
    for x, h, g in sorted(data):
        pipes[x].append((h, g))


    left = [(0, 0, 0, False, 0)]
    while left:
        s = x, y, passed, done, jumps = left.pop()

        # print(s, len(pipes))

        if passed == len(pipes):
            return jumps

        if (holes := pipes.get(x)) is not None:
            for h, g in holes:
                if y in range(h, h+g):
                    break
            else:
                print("blocked by", x)
                continue

            passed += 1
            done = False

        print(x, y, passed)

        if not done:
            left.append((x+1, y+1, passed, False, jumps+1))
        left.append((x+1, y-1, passed, True, jumps))


    return result

if __name__ == "__main__":
    with open("everybody_codes_e2025_q19_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
