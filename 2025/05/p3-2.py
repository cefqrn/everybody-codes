with open("everybody_codes_e2025_q05_p3.txt") as f:
    data = f.read()

def key(sword):
    id_, bone = sword
    return (
        quality_of(bone),
        tuple(map(score_of, bone)),
        id_
    )

def concat(nums):
    return int("".join(map(str, nums)))

def score_of(level):
    return concat(filter(None, level))

def quality_of(bone):
    _, spine, _ = zip(*bone)
    return concat(spine)

def sword_from(line):
    sword_id, nums = line.split(":", 1)

    spine = []
    for x in map(int, nums.split(",")):
        for i, (left, middle, right) in enumerate(spine):
            if x < middle and left is None:
                spine[i] = x, middle, right
                break
            if x > middle and right is None:
                spine[i] = left, middle, x
                break
        else:
            spine.append((None, x, None))

    return int(sword_id), spine

swords = list(map(sword_from, data.splitlines()))
swords.sort(key=key, reverse=True)

print(sum(i*id_ for i, (id_, _) in enumerate(swords, 1)))
