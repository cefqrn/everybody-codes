from itertools import cycle

def parse(s):
    clock = [range(1, 1+1)]
    left = []
    for i, x in enumerate(s.splitlines()):
        a, b = map(int, x.split("-"))

        if i & 1:
            left.append(range(b, a-1, -1))
        else:
            clock.append(range(a, b+1))

    clock.extend(reversed(left))

    return clock

def solve(clock):
    left = 202520252025 % sum(map(len, clock))

    for r in cycle(clock):
        if left < (length := len(r)):
            return r[left]

        left -= length

if __name__ == "__main__":
    from time import perf_counter_ns
    st = perf_counter_ns()
    with open("everybody_codes_e2025_q13_p3.txt") as f:
        data = parse(f.read().strip())

    print(solve(data))
    print(f"ran in {(perf_counter_ns() - st)/1000:.3f} μs")
