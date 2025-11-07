with open("everybody_codes_e2025_q05_p2.txt") as f:
    data = f.read()

# print(data)



import p1

z = tuple(map(p1.make_sword, data.split()))

print(max(z) - min(z))