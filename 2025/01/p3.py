with open("everybody_codes_e2025_q01_p3.txt") as f:
    data = f.read()

# print(data)

names, instructions = data.split()

# print(names, instructions)
names = names.split(",")
instructions = instructions.split(",")


for instruction in instructions:
    # print(instruction)
    d, n = instruction[0], instruction[1:]
    s = 1 if d == "R" else -1
    i = (int(n)*s) % len(names)

    names[0], names[i] = names[i], names[0]

    print(names)

print(names[0])

# print(names, instructions)