from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial
from itertools import batched, chain, cycle, islice, pairwise, combinations, product, zip_longest
from heapq import heappop, heappush
from math import inf
from re import findall

directions = (0, 1), (1, 0), (0, -1), (-1, 0)

# def rotate_triangle(lines):
    # n %= 3
    # length = len(lines[0])

    # r1 = []
    # for line in lines:
    #     l = line.strip(".").rjust(length, ".")
    #     print(l)
    #     r1.append(l)

    # r2 = tuple(zip(*r1))
    # for line in r2:
    #     print("".join(line))

    # r2 = tuple(zip(*r1))
    # print(*map(r2)
    # for l in r2:
    #     print("".join(l))

def parse(s):
    data = {}
    for y, l in enumerate(s.splitlines()):
        for x, c in enumerate(l):
            if c == "E":
                end = x, y
                c = "T"

            elif c == "S":
                start = x, y
                c = "T"

            data[x, y] = c

    return data, s.splitlines(), start, end

def rotated(lines):
        length = len(lines[0])
        r1 = []
        for line in lines:
            l = line.strip(".").ljust(length, ".")
            r1.append(l)

        r1 = tuple("".join(l[::-1]) for l in zip(*r1))
        # print(*chain(r1, "." * length))
        result = []
        for a, b in batched(chain(r1, ["." * len(r1[-1])]), 2):
            l = "".join(map("".join, zip_longest(a, b[1:], fillvalue="")))
            l = f"{l.strip("."):.^{length}}"

            result.append(l)

        return result

def solve(data):
    # print(rotated(rotated(rotated(lines))) == lines, sep="\n")

    grid, lines, start, end = data
    w, h = len(lines[0]), len(lines)


    indices = []
    positions = []
    for y in range(h):
        row = ""
        for x in range(w):
            if grid[x, y] == ".":
                row += "\uffff"
            else:
                row += chr(len(positions))

            positions.append((x, y))

        indices.append(row)

    rotated_indices = rotated(indices)

    print(rotated_indices)

    for y in range(h):
        ...
        # for x in range(w):
            
        #     ny, nx = divmod(ord(rotated_indices[y][x]), w)
        #     print(end=str((nx, ny)))
        # print()

    print(rotated_indices)

    # connections = defaultdict(list)
    # for (x, y), c in grid1.items():
    #     if c != "T":
    #         continue

    #     if grid2.get((x+1, y)) == "T":
    #         connections[x, y].append((x+1, y))
    #         connections[x+1, y].append((x, y))

    #     if (x ^ y) & 1:
    #         if grid2.get((x, y+1)) == "T":
    #             connections[x, y].append((x, y+1))
    #             connections[x, y+1].append((x, y))

    # left = [(0, start)]
    # seen = set()
    # while left:
    #     t, p = heappop(left)

    #     if p == eval(f"end{t%3+1}"):
    #         return t

    #     if p in seen:
    #         continue
    #     seen.add(p)

    #     for o in connections[p]:
    #         heappush(left, (t+1, o))

if __name__ == "__main__":
    with open("everybody_codes_e2025_q20_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
