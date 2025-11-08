with open("everybody_codes_e2025_q02_p1.txt") as f:
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


exec(data)

result = Complex(0, 0)

A=[25,9]
A = Complex(*A)
for _ in range(3):
    result *= result
    # print(result)

    result /= Complex(10, 10)
    # print(result)

    result += A
    # print(result)


print(f"[{result.x},{result.y}]")

# print("[",*result,"]")

