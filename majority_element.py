# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here

    freq = {}
    for item in a:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for x in list(freq.values()):
        if x > (len(a) /2):
            return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
