from re import findall
from itertools import batched, pairwise
from operator import mul
from time import perf_counter

with open("everybody_codes_e2026_q03_p3.txt") as f:
    data = f.read().strip()

st = perf_counter()

result = 0
for _, a, b in batched(findall(r"\d+", data), 3):
    a = (a * len(b))[-len(b):]
    a = [int(a)**i for i, a in zip(range(len(b))[::-1], a)]
    b = tuple(map(int, b))

    target = sum(map(mul, a, b))

    possible = {0}
    for (decreased_base, updated_base), (decreased, updated) in [*zip(pairwise(a), pairwise(b))][::-1]:
        can_remove = set()
        for new_digit in range(10):
            difference = (new_digit - updated) * updated_base
            can_remove.update(x + difference for x in possible)

        if can_remove.intersection(x * decreased_base for x in range(1, decreased+1)):
            break

        possible.update(can_remove)
    else:
        result += target

elapsed = perf_counter() - st

print(f"{result} found in {elapsed * 1_000:.3f} ms")
