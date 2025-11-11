from collections import Counter
from itertools import chain, islice, repeat, tee

with open("everybody_codes_e2025_q06_p3.txt") as f:
    data = f.read().strip()

mentors = Counter()

WINDOW_SIZE = 1000
REPEAT_COUNT = 1000

data = chain(
    repeat(None, WINDOW_SIZE*2),
    chain.from_iterable(repeat(data, REPEAT_COUNT)),
    repeat(None, WINDOW_SIZE)
)

lows, values, highs = tee(data, 3)
values = islice(values, WINDOW_SIZE,   None)
highs  = islice(highs,  WINDOW_SIZE*2, None)

result = 0
for lo, x, hi in zip(lows, values, highs):
    if hi is not None and hi.isupper():
        mentors[hi] += 1

    if x is not None and x.islower():
        result += mentors[x.upper()]

    if lo is not None and lo.isupper():
        mentors[lo] -= 1

print(result)
