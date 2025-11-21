from bisect import bisect_left
from itertools import islice
from math import inf

GRID_MASK = (1 << 34) - 1
PATTERN_MASK = (1 << 8) - 1

STEPS = 1000000000

def parse(s):
    grid = (0,)*34

    pattern = []
    for line in s.splitlines():
        pattern.append(sum((c=="#")<<i for i, c in enumerate(reversed(line))))

    return grid, pattern

def step(grid):
    new_grid = list(grid)
    for i, x in enumerate(grid):
        new_grid[i] ^= GRID_MASK
        bits = ((x << 1) & GRID_MASK) ^ (x >> 1)
        if i:
            new_grid[i-1] ^= bits
        if i < 33:
            new_grid[i+1] ^= bits

    return tuple(new_grid)

def iterate(f, x):
    yield x
    # yield from iterate(f, f(x))
    while True:
        yield (x := f(x))

def solve(data):
    initial_grid, pattern = data

    seen = {}
    matches = []
    for i, grid in enumerate(iterate(step, initial_grid)):
        # python int identities are wonky but fine here since we're counting up
        if seen.setdefault(grid, i) is not i:
            break

        for grid_row, pattern_row in zip(grid[13:], pattern):
            if ((grid_row >> 13) & PATTERN_MASK) ^ pattern_row:
                break
        else:
            matches.append((i, sum(map(int.bit_count, grid))))

    # dicts preserve insertion order
    # cycle_start = tuple(seen).index(grid)
    cycle_start = seen[grid]
    cycle_length = i - cycle_start

    repeats, left = divmod(STEPS, cycle_length)

    repeated_matches = islice(matches, bisect_left(matches, (cycle_start, 0)), None)
    result = repeats * sum(n for _, n in repeated_matches)

    last = bisect_left(matches, (left, inf))
    for _, n in islice(matches, last):
        result += n

    return result

if __name__ == "__main__":
    from time import perf_counter
    st = perf_counter()
    with open("everybody_codes_e2025_q14_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
    print(perf_counter() - st)
