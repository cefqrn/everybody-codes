from bisect import bisect_right
from functools import partial

def parse(s):
    return eval(s)

def columns_affected_by(number, length):
    return range(number-1, length, number)

def spell_required_for(wall, first_number=1):
    if not any(wall):
        return ()

    wall = list(wall)
    for column in columns_affected_by(first_number, len(wall)):
        wall[column] -= 1
        if wall[column] < 0:
            return None

    wall = tuple(wall)
    for next_number in range(first_number+1, len(wall)):
        if (rest := spell_required_for(wall, next_number)) is not None:
            return first_number, *rest

    return None

def blocks_required_for(spells, length):
    return sum(
        len(columns_affected_by(number, length))
        for number in spells)

def solve(wall):
    spell = spell_required_for(wall)
    def too_long_for(block_count, length):
        return blocks_required_for(spell, length) > block_count

    return bisect_right(
        range(999999999999999999),
        False,
        key=partial(too_long_for, 202520252025000)) - 1

if __name__ == "__main__":
    with open("everybody_codes_e2025_q16_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
