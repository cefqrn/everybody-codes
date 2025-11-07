with open("everybody_codes_e2025_q01_p2.txt") as f:
    data = f.read()

# print(data)

names, instructions = data.split()

# print(names, instructions)
names = names.split(",")
instructions = instructions.split(",")

i = 0
for instruction in instructions:
    # print(instruction)
    d, n = instruction[0], instruction[1:]
    s = 1 if d == "R" else -1
    i = (i + int(n)*s) % len(names)

    print(names[i])

# print(names, instructions)