from collections import defaultdict
from functools import partial
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

trie = {}
def add_to_trie(name, curr=trie):
    for c in name:
        curr = curr.setdefault(c, {})

    return curr

def add_new_names(name, curr):
    if len(name) > 11:
        return

    for b in follows[name[-1]]:
        if b in curr:
            continue

        curr[b] = new_curr = {}
        add_new_names(name+b, new_curr)

for planet in filter(partial(pairs_in, allowed), planets):
    add_new_names(planet, add_to_trie(planet))

def count_valid(curr, length=0):
    return (7 <= length <= 11) \
         + sum(map(partial(count_valid, length=length+1), curr.values()))

print(count_valid(trie))