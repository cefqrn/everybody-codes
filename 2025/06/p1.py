from collections import Counter

with open("everybody_codes_e2025_q06_p1.txt") as f:
    data = f.read().strip()

# data = "AaAaa"
mentors = Counter()

result = 0
for a in data:
    if a not in "aA":
        continue
    if a.isupper():
        mentors[a] += 1
    else:
        result += mentors[a.upper()]

print(result)