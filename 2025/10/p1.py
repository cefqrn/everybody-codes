from functools import partial
from itertools import combinations, pairwise, permutations, product, starmap
from operator import contains, eq


def parse(s):
    # s.splitlines()
    board = {}

    start = None
    for i, line in enumerate(s.splitlines()):
        for j, x in enumerate(line):
            board[i,j] = x
            if x == "D":
                start = i, j

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

    left = [(4, start)]
    seen = set()

    while left:
        l, pos = state = left.pop()

        if state in seen:
            continue
        seen.add(pos)

        # if board.get(pos) == "S":
        #     result += 1

        x, y = pos

        if l == 0:
            continue

        for dx, dy in horse_moves():
            nx, ny = x+dx, y+dy
            left.append((l-1, (nx, ny)))

    result = 0
    for p in seen:
        result += board.get(p) == "S"

    print(start, seen)
    return result


if __name__ == "__main__":
    with open("everybody_codes_e2025_q10_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))

