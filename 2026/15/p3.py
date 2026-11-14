from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
# from itertools import batched, chain, count, cycle, islice, pairwise, combinations, product, takewhile, zip_longest
from heapq import heappop, heappush
from math import comb, inf
from operator import itemgetter, mul
from re import findall
from typing import NamedTuple

directions = ()
directions += ( 0,  1), ( 1,  0), ( 0, -1), (-1,  0)
# directions += ( 1,  1), ( 1, -1), (-1, -1), (-1,  1)


def parse(s):

    grid = {}
    # grid = []

    required = set()

    for y, line in enumerate(s.splitlines()):

        # digits = tuple(map(int, findall(r"\d+", line)))
        # grid.append(digits)
        # grid.append(line)

        for x, c in enumerate(line):
            if c == "S":
                start = x, y
            if c == "E":
                end = x, y
            if c == "@":
                required.add((x, y))


            grid[x, y] = c

        ...

    return grid, start, end, required




def solve_p2(grid, start, end, needed, goal):

    result = 0

    # grid, start, end, needed = data

    print(data)

    states_seen = set()
    left = deque([(0, (1, 0), (start), 0)])

    while left:
        t, direction, pos, seen = left.popleft()
        print(t, seen)

        if grid.get(pos, "#") == "#":
            continue

        if pos in needed:
            seen += 1

        if pos == end:
            if seen >= goal:
                result = t
                break

            continue

        state = direction, pos, seen
        if state in states_seen: continue
        states_seen.add(state)

        dx, dy = direction
        x, y = pos
        for dx, dy in direction, (-dy, dx), (dy, -dx):
            npos = nx, ny = x+dx, y+dy
            nstate = t+1, (dx, dy), npos, seen

            left.append(nstate)
    else:
        raise ValueError


    return result





def solve(data):

    result = 0

    grid, start, end, needed = data



    def cycle_score(start, end, initial_direction):
        states_seen = defaultdict(lambda: -inf)
        left = deque([(0, initial_direction, start, 0)])

        best = None
        best_score = None

        while left:
            t, direction, pos, seen = left.popleft()

            if t > 100 and best is None:
                return None

            if t > 2000:
                break

            # print(pos)

            if grid.get(pos, "#") == "#":
                continue

            if pos in needed:
                seen += 1

            if pos == end and direction == initial_direction and seen:
                    # print(t, seen, pos, end)
                    # print("HI")
                    score = Fraction(seen, t)
                    if best_score is None or score > best_score:
                        best = t, seen
                        best_score = score

                    continue
                # return t, seen

            state = direction, pos
            if states_seen[state] >= seen:
                continue
            states_seen[state] = seen

            dx, dy = direction
            x, y = pos
            for dx, dy in direction, (-dy, dx), (dy, -dx):
                npos = nx, ny = x+dx, y+dy
                nstate = t+1, (dx, dy), npos, seen

                left.append(nstate)
        # else:
        #     raise ValueError("no path")

        # print(start, best)

        return best


    branches = []

    skip = False
    x, y = start

    dx, dy = 1, 0
    for t in range(end[0] - start[0]):

        branch = cycle_score((x, y), (x, y), (dx, dy))
        if branch:
            print(t, branch)

        branch = cycle_score((x, y), (x, y), (-dx, dy))
        if branch:
            print(t, branch)
        # npos1 = x-dy, y+dx
        # if grid.get(npos1, "#") != "#":
            # branches.append((t, cycle_score(npos1, (x, y), (-dy, dx))))
            # print(branches)

            # raise ValueError

        # npos2 = x+dy, y-dx
        # if grid.get(npos2, "#") != "#":
            # branches.append((t, cycle_score(npos2, (x, y), (dy, -dx))))

            # raise ValueError


        x += dx
        y += dy

    print(branches)

    raise ValueError

    # print(branches)
    # raise ValueError

    best_cycle = max(branches, key=lambda x: (Fraction(x[1][1], x[1][0]), -x[0]))

    # print(best_cycle)
    # raise ValueError

    initial, cycle = best_cycle
    goal = 202620262026

    done = (goal - 2*cycle[0]) // cycle[1]
    left = goal - done * cycle[1]
    result += initial
    result += done * cycle[0]

    result += solve_p2(grid, (initial, start[1]), end, needed, left)

    # print(best_cycle)




    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q15_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
