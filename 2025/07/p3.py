from collections import Counter

with open("everybody_codes_e2025_q07_p3.txt") as f:
    planets, rules = f.read().strip().split('\n\n')

planets = planets.split(",")
rules = rules.split("\n")

parsed = {}
for rule in rules:
    a, b = rule.split(" > ", 1)
    parsed[a] = b.split(",")
    # parsed.append((a, set(b.split(","))))
    # set(b.split(","))

from collections import deque
left = deque([(x, x) for x in parsed])

from functools import cache

@cache
def solve(a, l, acc):
    result = set()
    if 7 <= l <= 11:
        result.add(acc)

    if l == 11:
        return result

    for b in parsed.get(a, []):
        result.update(solve(b, l+1, acc+b))

    return result


from itertools import pairwise
@cache
def follows(planet):
    for a, b in pairwise(planet):
        for x, y in parsed.items():
            if a != x: continue

            if b not in y:
                return False
    return True

result = set()
for planet in planets:
    result.update(filter(follows, solve(planet[-1], len(planet), planet)))
    # print(planet)
    # print()

# print(result)

print(len(result))

# while left:
#     curr, a = left.popleft()
#     if curr in planets:
#         print(curr)
#         break
#     for b in parsed.get(a, []):
#         left.append((curr+b, b))



# from itertools import pairwise
# for planet in planets:
#     used = 0
#     for a, b in pairwise(planet):
#         for x, y in parsed:
#             if a != x: continue

#             if b not in y:
#                 break

#             used += 1
#         # else:
#         #     print(planet)

#         if used == len(parsed):
#             print(planet)
