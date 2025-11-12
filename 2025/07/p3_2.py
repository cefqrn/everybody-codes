from itertools import pairwise

with open("everybody_codes_e2025_q07_p3.txt") as f:
    planets, rules = f.read().strip().split("\n\n")

planets = planets.split(",")
rules = rules.splitlines()

parsed = {}
for rule in rules:
    a, b = rule.split(" > ", 1)
    parsed[a] = b.split(",")


def follows_rules(planet):
    for a, b in pairwise(planet):
        for x, y in parsed.items():
            if a != x: continue

            if b not in y:
                return False

    return True


seen = set()
def solve(a, l, acc):
    if acc in seen:
        return 0
    seen.add(acc)

    result = 7 <= l <= 11
    if l >= 11:
        return result

    for b in parsed.get(a, []):
        result += solve(b, l+1, acc+b)

    return result


result = 0
for planet in filter(follows_rules, planets):
    result += solve(planet[-1], len(planet), planet)

print(result)
