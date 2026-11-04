from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from operator import itemgetter
from re import findall

directions = (0, 1), (1, 0), (0, -1), (-1, 0)
directions += (1, 1), (1, -1), (-1, -1), (-1, 1)

from itertools import batched
def parse(s):

    result = {}
    for line in s.splitlines():
        # a, b = line.split(", ")
        # f
        k = id_, energy, *connections = map(int, findall(r"\d+", line))
        result[id_] = energy, connections


    return result

def solve_for_start(start, initial_data):
    states = [Counter() for _ in range(10)]

    energies = {k: v[0] for k, v in initial_data.items()}
    states[-1][start] += 1

    popped = set()

    while any(states):
        # print(states)
        # print(states)
        next_states = [Counter() for _ in range(10)]
        for i, state in enumerate(states, 1):
            for cloud, amount in state.items():
                if cloud in popped: continue

                energies[cloud] += amount * i
                if i >= 2:
                    for neighbor in initial_data[cloud][1]:
                        next_states[i-2][neighbor] += amount

        for cloud, energy in energies.items():
            if cloud in popped: continue

            if energy < 1000000: continue
            # if energy < 100: continue

            # print("explosion @", cloud, "w/", energy)

            popped.add(cloud)
            for neighbor in initial_data[cloud][1]:
                next_states[-1][neighbor] += 1

        states = next_states

    # print(energies)

    result = 0
    for k, v in energies.items():
        if k in popped: continue
        result += v

    # exit()
    return result

    # for i in range(1, 10+1)[::-1]:
    #     next_states = states.copy()
    #     next_ = defaultdict(int)
    #     for c, v in current.items():
    #         received[c] += v * i
    #         for k in data[c][1]:
    #             next_[k] += v

def solve(data):
    result = 0

    # print(solve_for_start(6, data))

    result = tuple(map(partial(solve_for_start, initial_data=data), sorted(data)))

    # print(result)
    return max(result)

if __name__ == "__main__":
    with open("everybody_codes_e2026_q07_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
