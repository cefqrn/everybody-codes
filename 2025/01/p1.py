with open("everybody_codes_e2025_q01_p1.txt") as f:
    data = f.read()

# print(data)

names, instructions = data.split()
names = names.split(",")
instructions = instructions.split(",")

i = 0
for instruction in instructions:
    d, n = instruction
    s = 1 if d == "R" else -1
    i = max(min(i + int(n)*s, len(names)-1), 0)

    print(names[i])

# print(names, instructions)