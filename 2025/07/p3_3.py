from collections import defaultdict
from itertools import product
from p1_2 import pairs_in

with open("everybody_codes_e2025_q07_p3.txt") as f:
    planets, rules = f.read().strip().split("\n\n")

planets = planets.split(",")
rules = rules.splitlines()

allowed = set()
follows = defaultdict(set)
for rule in rules:
    a, b = rule.split(" > ", 1)

    follows[a] = b = set(b.split(","))
    allowed.update(product(a, b))

seen = set()
def solve(acc):
    if acc in seen:
        return 0
    seen.add(acc)

    l = len(acc)
    result = 7 <= l <= 11
    if l >= 11:
        return result

    for b in follows[acc[-1]]:
        result += solve(acc+b)

    return result

print(sum(
    solve(planet) for planet in planets
    if pairs_in(allowed, planet)))
