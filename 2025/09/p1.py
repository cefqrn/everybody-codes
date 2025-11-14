from functools import partial
from itertools import pairwise, product,starmap


from operator import contains, eq

def parse(s):
    a,b,c=s.splitlines()

    return a[2:],b[2:],c[2:]



def solve(parsed_input):
    a,b,c = parsed_input

    # print

    x = sum(map(eq, a,c))
    y = sum(map(eq, b,c))

    print(x,y)
    return x*y

    return

if __name__ == "__main__":
    with open("everybody_codes_e2025_q09_p1.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))

