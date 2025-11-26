from functools import partial
from heapq import heappop, heappush
from itertools import count
from math import asin, dist, isclose, pi

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

TWO_PI = 2*pi

def parse(s):
    grid = {}
    for y, line in enumerate(s.splitlines()):
        for x, c in enumerate(line):
            if c == "@":
                vpos = x, y
            elif c == "S":
                pos = x, y
                grid[x, y] = 0
            else:
                grid[x, y] = int(c)

    return grid, pos, vpos

def explode(grid, pos, radius):
    vx, vy = pos
    for (x, y), c in grid.items():
        if (x-vx)**2 + (y-vy)**2 <= radius**2:
            grid[x, y] = None

o = 0, 0
length_of = partial(dist, o)

def solve(data):
    grid, spos, vpos = data
    vx, vy = vpos

    def angle_between(p, q):
        # cross product with z = 0
        px, py = p
        qx, qy = q

        s = sx, sy = px - vx, py - vy
        t = tx, ty = qx - vx, qy - vy

        m = (sx * ty - sy * tx) / (length_of(s) * length_of(t))

        return asin(m)

    for radius in count():
        limit = (radius+1)*30
        explode(grid, vpos, radius)

        seen = {}
        left = [(0, spos, 0)]
        best = None
        while left:
            t, pos, angle = heappop(left)

            if t >= limit:
                break

            if (r := seen.get(pos)) is not None:
                if isclose(TWO_PI, abs(angle - r[1])):
                    total_cost = t + r[0] - grid[pos]  # don't double count end
                    if total_cost < limit:
                        score = radius * total_cost
                        best = score if best is None else min(best, score)

                if r[0] <= t:
                    continue

            seen[pos] = t, angle

            x, y = pos

            for dx, dy in directions:
                npos = nx, ny = x+dx, y+dy
                if (cost := grid.get(npos)) is None:
                    continue

                nangle = angle + angle_between(pos, npos)

                heappush(left, (t+cost, npos, nangle))

        if best is not None:
            return best

if __name__ == "__main__":
    with open("everybody_codes_e2025_q17_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
