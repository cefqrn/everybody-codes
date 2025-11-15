from collections import defaultdict
from functools import partial
from itertools import combinations, pairwise, permutations, product, starmap
from operator import contains, eq
from math import inf


def parse(s):
    # s.splitlines()
    board = {}

    start = None
    for i, line in enumerate(s.splitlines()):
        for j, x in enumerate(line):
            board[j, i] = x
            if x == "D":
                start = j, i

    assert start

    return start, board


def horse_moves():
    yield  2,  1
    yield  2, -1
    yield -2,  1
    yield -2, -1
    yield  1,  2
    yield  1, -2
    yield -1,  2
    yield -1, -2


def solve(parsed_input):
    start, board = parsed_input

    k = 20

    seen = defaultdict(set)

    left = [(0, start)]
    result = 0
    while left:
        l, pos = left.pop()

        if l in seen[pos]:
            continue
        seen[pos].add(l)

        x, y = pos

        if l >= k:
            continue

        for dx, dy in horse_moves():
            nx, ny = x+dx, y+dy
            left.append((l+1, (nx, ny)))

    result = 0
    for (i, j), x in board.items():
        if x != "S":
            continue

        result += 1

        for t in range(k):
            pos = i, j+t  # dragon moves
            if board.get(pos) != "#" and t+1 in seen[pos]:
                break

            npos = i, j+t+1  # sheep moves
            if board.get(npos) != "#" and t+1 in seen[npos]:
                break
        else:
            result -= 1

    return result


if __name__ == "__main__":
    with open("everybody_codes_e2025_q10_p2.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))

