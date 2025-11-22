# fixes bugs from p3_4 - in_wall check, __rsub__

from functools import partial
from collections import defaultdict
from bisect import bisect_left, bisect_right
from math import inf
from heapq import heappop, heappush
from operator import itemgetter

from typing import NamedTuple
class Vec2(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Vec2(self.x + other[0], self.y + other[1])

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __sub__(self, other):
        return Vec2(self.x - other[0], self.y - other[1])

    __radd__ = __add__  # support mixing with tuples
    def __rsub__(self, other):
        return Vec2(other[0] - self.x, other[1] - self.y)

    def dot(self, other):
        return self.x * other[0] + self.y * other[1]


directions = Vec2(0, 1), Vec2(1, 0), Vec2(0, -1), Vec2(-1, 0)

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
        initial = Vec2(x+dx, y+dy)
        final = Vec2(x+dx*length, y+dy*length)

        walls.append((initial, final))

        x, y = final

    important_x |= {x, x-1, x+1}
    important_y |= {y, y-1, y+1}

    return walls, sorted(important_x), sorted(important_y)

def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def first_collision(walls, d, pos):
    x, y = pos
    if d[1]:  # vert
        candidates = []
        for start, end in walls:
            if start[0] == end[0]:  # both vertical
                if start[0] != x:   # no collision
                    continue

                if d.dot(start - pos) >= 0:  # correct direction
                    candidates.append(start)

                if d.dot(end - pos) >= 0:
                    candidates.append(end)
            else:  # horizontal
                start, end = sorted([start, end], key=itemgetter(0))
                if not (start[0] <= x <= end[0]):
                    continue

                if d.dot(start - pos) >= 0:
                    candidates.append((x, start[1]))

        return min(candidates, key=partial(dist, pos), default=(x, inf*d[1]))
    else:  # horizontal
        candidates = []
        for start, end in walls:
            if start[1] == end[1]:  # both horizontal
                if start[1] != y:   # no collision
                    continue
                if d.dot(start - pos) >= 0:  # correct direction
                    candidates.append(start)

                if d.dot(end - pos) >= 0:
                    candidates.append(end)
            else:  # horizontal
                start, end = sorted([start, end], key=itemgetter(1))
                if not (start[1] <= y <= end[1]):
                    continue

                if d.dot(start - pos) >= 0:
                    candidates.append((start[0], y))

        return min(candidates, key=partial(dist, pos), default=(inf*d[0], y))


def in_wall(walls, pos):
    x, y = pos
    for start, end in walls:
        if (start - pos).dot(e:=end - pos) in (0, -1, 1) and not all(e):
            return True
    return False


def solve(data):
    walls, important_x, important_y = data
    last = tuple(walls)[-1][-1]

    left = [(0, (0, 0))]
    seen = defaultdict(lambda: inf)
    while left:
        s = t, pos = heappop(left)

        if pos == last:
            return t

        if in_wall(walls, pos):
            continue

        if seen[pos] <= t: continue
        seen[pos] = t

        x, y = pos

        d = directions[0]  # north
        _, cy = first_collision(walls, d, pos)
        for ny in important_y[bisect_right(important_y, y):bisect_right(important_y, cy)]:
            heappush(left, (t+ny-y, (x, ny)))

        d = directions[2]  # south
        _, cy = first_collision(walls, d, pos)
        for ny in important_y[bisect_left(important_y, cy):bisect_left(important_y, y)]:
            heappush(left, (t+y-ny, (x, ny)))


        d = directions[1]  # east
        cx, _ = first_collision(walls, d, pos)
        for nx in important_x[bisect_right(important_x, x):bisect_right(important_x, cx)]:
            heappush(left, (t+nx-x, (nx, y)))

        d = directions[3]  # west
        cx, _ = first_collision(walls, d, pos)
        for nx in important_x[bisect_left(important_x, cx):bisect_left(important_x, x)]:
            heappush(left, (t+x-nx, (nx, y)))


if __name__ == "__main__":
    with open("everybody_codes_e2025_q15_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
