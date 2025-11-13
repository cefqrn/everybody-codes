from itertools import pairwise

if __name__ == "__main__":
    with open("everybody_codes_e2025_q08_p1.txt") as f:
        order = f.read().strip()

    order = tuple(map(int, order.split(",")))

    k = 32

    print(sum((b-a)%k == k//2 for a, b in pairwise(order)))
