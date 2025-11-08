with open("everybody_codes_e2025_q02_p3.txt") as f:
    data = f.read()

from typing import NamedTuple

class Complex(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Complex(self.x+other.x, self.y+other.y)

    def __mul__(self, other):
        X1, Y1 = self
        X2, Y2 = other
        return Complex(*[X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2])

        # return Complex(self.x*other.x - self.y-other.y, self.x*other.y + self.y*other.x)

    def __truediv__(self, other):
        # truncate, not floor
        return Complex(int(self.x / other.x), int(self.y / other.y))



def check(p):
    result = Complex(0, 0)
    for _ in range(100):
        result *= result
        result /= Complex(100000,100000)
        result += p

        if not (-1000000 <= result.x <= 1000000) or not (-1000000 <= result.y <= 1000000):
            return False

    return True


exec(data)
# A=[35300,-64910]

A = Complex(*A)

from itertools import product
r = 0
k=0

from collections import defaultdict
results = defaultdict(list)
for i, j in product(range(1000+1), repeat=2):
    p = Complex(A.x+1*j, A.y+1*i)
    c = check(p)
    r += c

    results[i].append(c)

print(r)
# print(*results, sep='\n')

# for l in results.values():
#     print(*map("·x".__getitem__, l), sep="")


# for i in range(101):


# print(f"[{result.x},{result.y}]")

# print("[",*result,"]")

