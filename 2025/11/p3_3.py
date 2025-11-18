from functools import partial
from itertools import tee
from operator import lt, sub
from statistics import mean
from sys import stdin

ducks1, ducks2 = tee(map(int, stdin))
rounds = sum(filter(partial(lt, 0), map(partial(sub, mean(ducks2)), ducks1)))
# rounds = sum(filter(0 .__lt__, map(mean(ducks2).__sub__, ducks1)))

print(rounds)
