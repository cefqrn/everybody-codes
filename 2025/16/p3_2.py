from bisect import bisect_right

def parse(s):
    return eval(s)

def solve2(data, start_from=1):
    if not any(data):
        return ()

    wall = list(data)
    for i in range(start_from-1, len(data), start_from):
        wall[i] -= 1
        if wall[i] < 0:
            return None

    wall = tuple(wall)
    for x in range(start_from+1, len(data)):
        if (result := solve2(wall, x)) is not None:
            return start_from, *result

    return None

def solve1(data, length):
    return sum(len(range(x-1, length, x)) for x in data)

N = 202520252025000
def solve(data):
    spells = solve2(data)
    def cant_solve(length):
        return solve1(spells, length) > N

    return bisect_right(range(1, 999999999999999999), False, key=cant_solve)

if __name__ == "__main__":
    with open("everybody_codes_e2025_q16_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
