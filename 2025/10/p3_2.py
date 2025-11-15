from collections import defaultdict, deque
from functools import partial
from itertools import combinations, pairwise, permutations, product, starmap
from operator import contains, eq
from math import inf

def parse(s):
    hiding_spots = set()
    sheep_positions = set()

    start = None

    y = 0
    for y, line in enumerate(b:=s.splitlines()):
        for x, c in enumerate(line):
            if c == "S":
                sheep_positions.add((x,y))
            elif c == "#":
                hiding_spots.add((x,y))
            elif c == "D":
                start = x, y

    assert start

    return (len(line), len(b)), start, frozenset(sheep_positions), frozenset(hiding_spots)


def horse_moves():
    yield  2,  1
    yield  2, -1
    yield -2,  1
    yield -2, -1
    yield  1,  2
    yield  1, -2
    yield -1,  2
    yield -1, -2


from functools import cache



def solve(parsed_input):
    (w, h), dragon_position, sheep_positions, hiding_spots = parsed_input

    W = range(w)
    H = range(h)

    k = h * len(sheep_positions) * 2
    dragon_positions = defaultdict(lambda: defaultdict(int))

    dragon_positions[dragon_position][0] = 1

    left = deque([(0, dragon_position)])
    while left:
        t, pos = left.popleft()
        amount = dragon_positions[pos][t]

        if t == k:
            break

        x, y = pos
        for dx, dy in horse_moves():
            npos = nx, ny = x+dx, y+dy

            if nx not in W or ny not in H:
                continue

            dragon_positions[npos][t+1] += amount
            if dragon_positions[npos][t+1] == amount:
                left.append((t+1, npos))


    @cache
    def sheep(sheep_positions):
        # either move, don't move, or wait
        # you can only wait if you're the only one left
        for pos in sheep_positions:
            x, y = pos
            npos = x, y+1
            

        return result


    return sheep(sheep_positions)




    # return parsed_input


if __name__ == "__main__":
    with open("everybody_codes_e2025_q10_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))

