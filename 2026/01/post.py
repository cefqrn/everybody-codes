from bisect import bisect_left

def next_after(target, space, f):
    i = bisect_left(space, True, key=lambda x: f(x) >= target)
    return f(space[i])

for part, (func, search_space) in enumerate((
    (lambda x: x*x,           range(1, 2**32)),
    (lambda x: 2*x + 2*(x-2), range(3, 2**32)),
    (lambda x: x*x - 1,       range(3, 2**32, 2)),
), 1):
    with open(f"everybody_codes_e2026_q01_p{part}.txt") as f:
        data = tuple(map(int, f.read().split(",")))

    print(sum(next_after(x, search_space, func) - x for x in data))
