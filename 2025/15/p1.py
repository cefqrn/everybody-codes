from functools import partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

def parse(s):
    wall = {}
    x, y = 0, 0
    d = dx, dy = directions[0]

    for inst in s.split(","):
        d = dx, dy = directions[(directions.index(d) + [1,-1][inst[0] == "L"]) % 4]
        for _ in range(int(inst[1:])):
            x += dx
            y += dy

            wall[x, y] = "#"

    return wall

def solve(data):
    walls = data
    last = tuple(data)[-1]

    left = deque([(0, (0, 0))])
    seen = set()
    while left:
        t, pos = left.popleft()

        if pos in seen: continue
        seen.add(pos)

        x,y=pos
        for dx, dy in directions:
            npos = nx, ny = x+dx, y+dy
            if npos == last:
                return t+1

            if npos in walls:
                continue

            left.append((t+1, npos))
    result = 0
    return result

if __name__ == "__main__":
    with open("everybody_codes_e2025_q15_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
