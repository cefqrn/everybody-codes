from itertools import product
from p1_2 import pairs_in

with open("everybody_codes_e2025_q07_p2.txt") as f:
    planets, rules = f.read().strip().split("\n\n")

planets = planets.split(",")
rules = rules.splitlines()

allowed = set()
for rule in rules:
    a, b = rule.split(" > ", 1)
    allowed.update(product(a, b))

print(sum(
    i for i, planet
    in enumerate(planets, 1)
    if pairs_in(allowed, planet)))