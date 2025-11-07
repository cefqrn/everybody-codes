with open("everybody_codes_e2025_q05_p1.txt") as f:
    data = f.read()

print(data)


# from collections import 

def make_sword(data):
    a, b = data.split(":", 1)
    a = int(a)
    b = eval(b)

    # spine = [(None, None, None)]
    spine = []
    for x in b:
        # print(spine)
        for i, curr in enumerate(spine):
            initial = curr
            match curr:
                case None, None, None:
                    curr = None, x, None
                case left, middle, right:
                    if x < middle and not left:
                        curr = x, middle, right
                    elif x > middle and not right:
                        curr = left, middle, x
            if curr is not initial:
                spine[i] = curr
                break
        else:
            spine.append((None, x, None))

    # print(spine)

    return int("".join(str(x) for _, x, _ in spine))


    # print(a,b)

print(make_sword(data))