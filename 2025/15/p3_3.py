from functools import partial
from itertools import chain, cycle, islice, pairwise, combinations, product
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from math import inf
from heapq import heappop, heappush

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

def parse(s):
    walls = []
    x, y = 0, 0
    d = dx, dy = directions[0]

    # points_of_interest = set()
    important_x = set()
    important_y = set()

    for inst in s.split(","):
        important_x |= {x, x-1, x+1}
        important_y |= {y, y-1, y+1}

        d = dx, dy = directions[(directions.index(d) + [1,-1][inst[0] == "L"]) % 4]
        length = int(inst[1:])
        initial = x+dx, y+dy
        final = x+dx*length, y+dy*length

        # points_of_interest.update(product((x, x-1, x+1), (y, y-1, y+1)))

        walls.append((initial, final))

        x, y = final

    important_x |= {x, x-1, x+1}
    important_y |= {y, y-1, y+1}

    return walls, sorted(important_x), sorted(important_y)

def solve(data):
    print("starting search")

    walls, important_x, important_y = data
    last = tuple(walls)[-1][-1]

    # edges = {}
    # s = 0
    # for a, b in combinations(points_of_interest, r=2):
    #     if (a, b) in walls or (b, a) in walls:
    #         continue

    #     for start, 

    #     # print(a,b)
    #     s += 1

    # print(len(points_of_interest), s)

    return

    walls = data
    last = tuple(data)[-1][-1]

    # for a, b in walls:
    #     print(*a, *b, sep=",")

    # lx, ly = last

    # def h(pos):
    #     x, y = pos
    #     return abs(lx - x) + abs(ly - y)

    # curr_f = h(p:=(0, 0))
    # now = [(curr_f, 0, p)]
    # later = []

    # seen = defaultdict(lambda: inf)
    # while now:
    #     next_f = inf
    #     while now:
    #         s = f, t, pos = now.pop()

    #         if f > curr_f:
    #             next_f = min(next_f, f)
    #             later.append(s)
    #             continue

    #         if seen[pos] <= f:
    #             continue
    #         seen[pos] = f

    #         x, y = pos

    #         for dx, dy in directions:
    #             npos = nx, ny = x+dx, y+dy
    #             nt = t+1

    #             if npos == last:
    #                 return nt

    #             if npos in walls:
    #                 continue
    #             later.append((nt+h(npos), nt, npos))

    #     now, later = later, now
    #     curr_f = next_f


if __name__ == "__main__":
    with open("everybody_codes_e2025_q15_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
