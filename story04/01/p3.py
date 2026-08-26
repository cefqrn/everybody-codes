from bisect import bisect_left, bisect_right
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import cache, partial, reduce
from itertools import chain, cycle, islice, pairwise, combinations, product
from heapq import heappop, heappush
from math import inf
from re import findall

directions = (0, -1), (1, 0), (0, 1), (-1, 0)

def parse(s):
    data = s

    data = []
    for line in s.splitlines():
        data.append(eval(line))

    return data

def solve(data):
    result = 0

    for seq in data:
        print(seq)

        blocked_above = []
        blocked_under = []
        seen = {curr := 0}

        blocked = blocked_under
        other_blocked = blocked_above
        for x, _ in zip(seq, cycle([blocked_under, blocked_above])):
            new = curr - x
            # print("want to try", new)
            if new >= 0 and new not in seen:
                for r in chain([[]], blocked):
                    if (new in r) ^ (curr in r):
                        break
                else:
                    # print(curr, new, "hi", x)
                    blocked.append(range(new+1, curr))
                    curr = new
                    seen.add(new)

                    blocked, other_blocked = other_blocked, blocked
                    continue

            for x in range(x, 300):
                new = curr + x
                if new in seen:
                    continue

                for r in chain([[]], blocked):
                    if (new in r) ^ (curr in r):
                        # if x < 20: print("BLOCKED", curr, new, (new in r) , (curr in r))
                        break
                else:
                    # print(curr, new, "old", x, blocked)
                    blocked.append(range(curr+1, new))
                    curr = new
                    seen.add(new)

                    blocked, other_blocked = other_blocked, blocked
                    break
        # print(blocked_above)
        # print(blocked_under)

        result += curr

    return result

if __name__ == "__main__":
    with open("everybody_codes_e4_q01_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
