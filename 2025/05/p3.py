with open("everybody_codes_e2025_q05_p3.txt") as f:
    data = f.read()


def compare(a, b):
    (id_a, spine_a), (id_b, spine_b) = a, b

    # print(a, b)

    if not spine_a and not spine_b:
        return 1 if id_a > id_b else -1

    qa = get_quality(spine_a)
    qb = get_quality(spine_b)

    xa, *spine_a = spine_a
    xb, *spine_b = spine_b

    if qa > qb:
        return 1
    if qb > qa:
        return -1

    qa = int("".join(map(str, filter(None, xa))))
    qb = int("".join(map(str, filter(None, xb))))

    # print(qa, qb)
    if qa > qb:
        return 1
    if qb > qa:
        return -1

    return compare((id_a, spine_a), (id_b, spine_b))

def get_quality(spine):
    return int("".join(str(x) for _, x, _ in spine))

def make_sword(data):
    a, b = data.split(":", 1)
    sword_id = int(a)
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

    return sword_id, spine

from functools import cmp_to_key
swords = list(map(make_sword, data.split()))

# print(compare(*swords))

swords.sort(key=cmp_to_key(compare), reverse=True)
result = 0
for i, (id_, _) in enumerate(swords, 1):
    result += i*id_
# print(*swords, sep='\n')
print(result)
# print(make_sword(data))