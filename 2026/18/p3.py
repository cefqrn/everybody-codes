directions = ()
directions += ( 0,  1), ( 1,  0), ( 0, -1), (-1,  0)
# directions += ( 1,  1), ( 1, -1), (-1, -1), (-1,  1)

directions_arrows = "^>v<"


def parse(s):

    # grid = {}
    grid = []

    from re import findall
    for y, line in enumerate(s.splitlines()):

        x, y, w = tuple(map(int, findall(r"\d+", line)))
        grid.append((x, y))
        grid.append((x+w-1, y))
        # grid.append(p)
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
    # result = sum(y for _, y in data)

    data.sort()
    print(data)

    i = 0
    j = len(data) - 1

    level = 0
    while i <= j:
        dist = data[j][0] - data[i][0]
        if data[i][1] < data[j][1]:
            new_level = max(data[i][1], level)
            i += 1
        else:
            new_level = max(data[j][1], level)
            j -= 1
        z = (new_level - level) * (dist + 1)
        print(z)
        result += z
        level = new_level

    # print(data)

    # for _ in data:



    #     ...

    return result


if __name__ == "__main__":
    with open("everybody_codes_e2026_q18_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
