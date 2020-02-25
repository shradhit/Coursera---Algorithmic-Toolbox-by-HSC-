# Uses python3
import sys


def binary_search(a, x):
    left = 0;
    right = len(a) - 1
    while left < right:
        mid = (left + right) / 2
        mid = int(mid)
        if (a[left] <= x) and (x <= a[mid]):
            right = mid
        elif (a[mid + 1] <= x) and (x <= a[right]):
            left = mid + 1
        elif a[left] > a[mid]:
            right = mid
        else:
            left = mid + 1
    if a[left] == x:
        return left
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')
