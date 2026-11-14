from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
# from itertools import batched, chain, count, cycle, islice, pairwise, combinations, product, takewhile, zip_longest
from heapq import heappop, heappush
from itertools import chain, combinations, pairwise, tee
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




def solve_p2(grid, start, end, needed, goal, initial_direction):

    result = 0

    # grid, start, end, needed = data

    # print(data)

    states_seen = set()
    left = deque([(0, (1, 0), (start), 0)])

    while left:
        t, direction, pos, seen = left.popleft()
        # print(t, seen)

        if grid.get(pos, "#") == "#":
            continue

        if pos in needed:
            seen += 1

            # if seen > goal:
            #     continue

        if pos == end:
            if seen == goal:
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



    def branch_score(start, end, initial_direction):
        states_seen = defaultdict(lambda: -inf)
        left = deque([(0, initial_direction, start, 0)])

        best = None
        best_score = None

        while left:
            t, direction, pos, seen = left.popleft()

            # if t > 100 and best is None:
            #     return None

            # if t > 2000:
            #     break

            # print(pos)

            if grid.get(pos, "#") == "#":
                continue

            if pos in needed:
                seen += 1

            if pos[1] == start[1] and t:
                return t, seen, pos[0]

            state = direction, pos
            if states_seen[state] >= seen:
                continue
            states_seen[state] = seen

            dx, dy = direction
            x, y = pos
            for dx, dy in (direction,) + (t > 0) * ((-dy, dx), (dy, -dx)):
                npos = nx, ny = x+dx, y+dy
                nstate = t+1, (dx, dy), npos, seen

                left.append(nstate)
        # else:
        #     raise ValueError("no path")

        # print(start, best)

        return best

    def cycle_score(start, max_t=1000):
        left = [(0, start, 0)]
        seen = defaultdict(lambda: -inf)

        best_score = -inf
        best = None
        while left:
            t, state, score = heappop(left)
            if t > max_t:
                break

            if seen[state] >= score: continue
            seen[state] = score

            if state == start and t:
                result = Fraction(score, t)
                if result > best_score:
                    best_score = result
                    best = state, score, t
                continue

            for neighbor, cost, bonus in connections[state]:
                nstate = t + cost, (neighbor, -state[1]), score + bonus
                heappush(left, nstate)

        # raise Exception

        return best, best_score


    def best_path(start, end, initial_direction):
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

            if pos == end:
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
        npos1 = x-dy, y+dx
        if grid.get(npos1, "#") != "#":
            branches.append((t, dx, branch_score((x, y), (x, y), (-dy, dx))))

        npos2 = x+dy, y-dx
        if grid.get(npos2, "#") != "#":
            branches.append((t, -dx, branch_score((x, y), (x, y), (dy, -dx))))

        x += dx
        y += dy

    print(branches)


    connections = defaultdict(list)
    for start, direction, (cost, bonus, end) in sorted(set(branches)):
        connections[start, direction].append((end, cost, bonus))

    possible_starts = sorted(set(connections))

    # for (start, _), (end, _) in combinations(possible_starts, r=2):
    #     if start == end: continue
    #     connections[start,  1].append((end,   abs(end - start), 0))
    #     connections[start, -1].append((end,   abs(end - start), 0))
    #     connections[end,    1].append((start, abs(end - start), 0))
    #     connections[end,   -1].append((start, abs(end - start), 0))

    start_positions = sorted(set(k for k, _ in possible_starts))

    for a, b in pairwise(start_positions):
        if start == end: continue
        connections[a,  1].append((b, abs(b - a), 0))
        connections[a, -1].append((b, abs(b - a), 0))
        connections[b,  1].append((a, abs(b - a), 0))
        connections[b, -1].append((a, abs(b - a), 0))


    # print(possible_starts)




    grid, start, end, needed = data


    best = None
    # best_score = (-inf, -inf)
    best_score = -inf
    for s in possible_starts:
        state, score = cycle_score(s)

    #     if score < best_score[0]: continue

    #     path = best_path(start, (s[0], start[1]), (1, 0))
    #     print(s, path)
    #     path_t, path_score = path

    #     score = score, Fraction(path_score, path_t)
    #     if score > best_score:
    #         print("NEW BEST", s, score[0], path_t, path_score)
    #         best_score = score
    #         best = state, path_t, path_score

    # ((initial, dy), score, t), path_t, path_score = best

        if score > best_score:
            print("NEW BEST", s, score)
            best_score = score
            best = state




    (initial, dy), score, t = best
    initial_direction = 0, dy

    cycle_sulfur = score
    cycle_length = t

    print()
    print()
    print()
    print(initial, initial_direction, cycle_sulfur, cycle_length)
    # print(path_score, path_t)

    # raise Exception

    # goal = 202620262026 - path_score
    goal = 202620262026

    done = goal // cycle_sulfur - 2
    left = goal - done * cycle_sulfur

    # print(done, left)

    result = 0
    # result += initial
    # result += path_t



    # solve_p2(grid, (initial))

    result += done * cycle_length

    grid, start, end, needed = data

    best = inf
    for a in range(left+1):
        b = left - a
        curr = 0
        try:
            curr += solve_p2(grid, start, (initial, start[1]), needed, a, (1, 0))
            curr += solve_p2(grid, (initial, start[1]), end, needed, b, initial_direction)
        except ValueError:
            continue

        best = min(curr, best)
    result += best

    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q15_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
