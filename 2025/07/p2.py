from collections import Counter

with open("everybody_codes_e2025_q07_p2.txt") as f:
    planets, rules = f.read().strip().split('\n\n')

planets = planets.split(",")
rules = rules.split("\n")

# parsed = {}
parsed = []
for rule in rules:
    a, b = rule.split(" > ", 1)
    # parsed[a] = b
    parsed.append((a, set(b.split(","))))
    # set(b.split(","))

# from collections import deque
# left = deque([(x, x) for x in parsed])

# while left:
#     curr, a = left.popleft()
#     if curr in planets:
#         print(curr)
#         break
#     for b in parsed.get(a, []):
#         left.append((curr+b, b))



from itertools import pairwise
result = 0
for i, planet in enumerate(planets, 1):
    # used = 0
    for a, b in pairwise(planet):
        for x, y in parsed:
            if a != x: continue

            if b not in y:
                break

            # used += 1
        else:
            continue

        break
    else:
        result += i
        print(i, planet)

print(result)
