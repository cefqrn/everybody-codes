from collections import Counter, deque
from itertools import islice, tee

with open("everybody_codes_e2025_q06_p3.txt") as f:
    data = f.read().strip()

data *= 1000
mentors = Counter()
queue = deque()

N = 1000
data = "?"*N*10 + data + "?"*N*10

result = 0
for i, x in enumerate(data):
    if i not in range(N+1, len(data)-N-1):
        continue

    lo = data[i-N]
    hi = data[i+N+1]

    if {hi, lo} == {"?"}:
        continue

    if x.isalpha():
        if x.islower():
            result += mentors[x.upper()]
    if lo.isalpha():
        if lo.isupper():
            mentors[lo] -= 1
    if hi.isalpha():
        if hi.isupper():
            mentors[hi] += 1

print(result)
