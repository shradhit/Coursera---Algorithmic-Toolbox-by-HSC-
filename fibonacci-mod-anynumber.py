# Uses python3
"""
This is true in general: for any integer 𝑚 ≥ 2, the sequence 𝐹𝑛 mod 𝑚 is periodic. The period always
starts with 01 and is known as Pisano period.

"""

import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_improved(n, m):
    if n <= 1:
        return n
    previous = 0
    current  = 1
    remainder = list()
    remainder.append(0)
    remainder.append(1)
    for _ in range(n - 1):
        previous, current = current, previous + current
        remainder.append(current % m)
        if previous % m == 0 and current % m == 1:
            y = n % len(remainder[:-2])

    return remainder[y]



if __name__ == '__main__':
    input = sys.stdin.read();
    #input = input()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_improved(n, m))
