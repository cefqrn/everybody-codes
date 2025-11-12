from functools import partial
from itertools import pairwise, product
from operator import contains

def pairs_in(allowed, name):
    return all(map(partial(contains, allowed), pairwise(name)))

if __name__ == "__main__":
    with open("everybody_codes_e2025_q07_p1.txt") as f:
        planets, rules = f.read().strip().split("\n\n")

    planets = planets.split(",")
    rules = rules.splitlines()

    allowed = set()
    for rule in rules:
        a, b = rule.split(" > ", 1)
        allowed.update(product(a, b.split(",")))

    print(next(filter(partial(pairs_in, allowed), planets)))
