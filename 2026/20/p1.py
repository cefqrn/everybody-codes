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


def solve(data):

    result = 0

    print(data)

    for line in data:
        is_true = eval(line.replace("=", "=="))
        if not is_true:
            continue

        mapping = dict(zip(
            "0123456789+-=",
            [6, 2, 5, 5, 4, 5, # (last is 5)
            6,3,7,6,2,1,2
            ]
        ))

        curr = sum(mapping.get(c, 0) for c in line)
        print(curr)
        result += curr



        ...

    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q20_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
