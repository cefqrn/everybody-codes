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
    pipes = defaultdict(list)
    # pipes[0].append((0, 1))
    for x, h, g in sorted(map(eval, s.splitlines())):
        pipes[x].append((h, g))

    for v in pipes.values():
        v.sort(reverse=True)

    return pipes



def solve(data):
    pipes = data

    # pairs = tuple(pairwise(pipes.items()))
    pipes = tuple(pipes.items())

    print(len(pipes))


    @cache
    def solve1(x, y, pipe_index):
        try:
            pipe_x, intervals = pipes[pipe_index]
        except IndexError:
            return 0

        result = inf
        for h, g in intervals:
            for ny in range(h, h+g):
                dy = ny - y
                nx = x + abs(dy)  # get to correct height
                if nx > pipe_x:  # too high/low
                    continue

                if (pipe_x - nx) % 2:  # can't hover
                    continue

                # print(pipe_index, y, ny, x, pipe_x, "flaps", max(0, dy), (pipe_x - nx) // 2)

                flap_count = max(0, dy) + (pipe_x - nx) // 2

                result = min(result, flap_count + solve1(pipe_x, ny, pipe_index+1))#.update(flap_count + k for k in solve1(pipe_x, ny, pipe_index+1))

        return result

    return solve1(0, 0, 0)



if __name__ == "__main__":
    with open("everybody_codes_e2025_q19_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
