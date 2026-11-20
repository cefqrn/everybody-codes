from collections import defaultdict
from string import digits


directions = ()
directions += ( 0,  1), ( 1,  0), ( 0, -1), (-1,  0)
# directions += ( 1,  1), ( 1, -1), (-1, -1), (-1,  1)

directions_arrows = "^>v<"


def parse(s):

    # grid = {}
    grid = []

    for y, line in enumerate(s.splitlines()):
        grid.append(line)

        # digits = tuple(map(int, findall(r"\d+", line)))
        # grid.append(digits)
        # grid.append(line)

        # for x, c in enumerate(line):
        #     if c == ".":
        #         continue

        #     grid[x, y] = c

        ...

    return grid


# def within(a):


digit_bits = {
    "0": int("1111110", 2),
    "1": int("0110000", 2),
    "2": int("1101101", 2),
    "3": int("1111001", 2),
    "4": int("0110011", 2),
    "5": int("1011011", 2),
    "6": int("1011111", 2),
    "7": int("1110000", 2),
    "8": int("1111111", 2),
    "9": int("1111011", 2),
    "A": int("1110111", 2),
}

from itertools import combinations, permutations
remove_1 = defaultdict(list)
remove_1["+"].append("-")
for (d1, bits1), (d2, bits2) in permutations(digit_bits.items(), r=2):
    diff = (bits1 ^ bits2).bit_count()
    if diff != 1: continue
    if bits1.bit_count() > bits2.bit_count():
        remove_1[d1].append(d2)

add_1 = defaultdict(list)
add_1["-"].append("+")
for (d1, bits1), (d2, bits2) in permutations(digit_bits.items(), r=2):
    diff = (bits1 ^ bits2).bit_count()
    if diff != 1: continue
    if bits1.bit_count() < bits2.bit_count():
        add_1[d1].append(d2)

no_change = defaultdict(list)
for (d1, bits1), (d2, bits2) in permutations(digit_bits.items(), r=2):
    diff = (bits1 ^ bits2).bit_count()
    if diff != 2: continue
    no_change[d1].append(d2)

# print(remove_1)
# print(add_1)
# print(no_change)


def possible_with(side):
    result = []
    for i, c in enumerate(side):
        for x in no_change[c]:
            curr = side[:i] + x + side[i+1:]
            result.append(curr)
        for j, d in enumerate(side[i+1:], i+1):
            for x in add_1[c]:
                for y in remove_1[d]:
                    curr = side[:i] + x + side[i+1:j] + y + side[j+1:]
                    result.append(curr)
            for x in remove_1[c]:
                for y in add_1[d]:
                    curr = side[:i] + x + side[i+1:j] + y + side[j+1:]
                    result.append(curr)
    return result

def works(side):
    if works_single(side):
        return side
    for p in possible_with(side):
        if works_single(p):
            return side
    return None

def works_single(side):
    stack = []
    for s in side.split():
        if s in "-=+":
            stack.append(s)
            continue
        stack.append(str(int(s, 11)))
    stack = "".join(stack)
    return eval(stack.replace("=", "=="))



# def remove_one(a):
#     return [a]

# def possible_with()



# change left
# change right
# -1 left +1 right
# +1 left -1 right, same as reverse then do prev so just sort


print(add_1)
print(remove_1)
print(no_change)


def solve(data):

    result = 0

    print(data)

    for line in data:
        if not (new_line := works(line)):
            print("not work", line)
            continue
        print("works", line, "->", new_line)

        mapping = dict(zip(
            "0123456789+-=A",
            [6, 2, 5, 5, 4, 5, # (last is 5)
            6,3,7,6,2,1,2,
            6
            ]
        ))

        curr = sum(mapping.get(c, 0) for c in line)
        print(curr)
        result += curr



        ...

    x = result
    stack = []
    while x:
        x, r = divmod(x, 11)
        stack.append(r)
    print(stack)

    result = "".join((digits + "A")[c] for c in stack[::-1])
    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q20_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
