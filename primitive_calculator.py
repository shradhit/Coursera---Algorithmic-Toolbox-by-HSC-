# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def new_sequence(n):
    sequence = []
    #print('abc')
    while n >= 1:

        sequence.append(n)
        #print(sequence)
        if n % 3 == 0:
            n = n // 3

        elif n % 2 == 0:
            n = n // 2

        elif ((n - 1) % 3 == 0):
            sequence.append(n-1)
            n = (n-1) // 3

        elif ((n - 2) % 3 == 0):
            sequence.append(n-1)
            sequence.append(n-2)
            n = (n-2) // 3

        elif ((n-1) % 2 == 0):
            sequence.append(n-1)
            n = (n-1) // 2

        #else:
        #    n = n - 1
    del sequence[-1]
    return sequence[::-1]


input = sys.stdin.read()
n = int(input)
sequence = list(new_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
