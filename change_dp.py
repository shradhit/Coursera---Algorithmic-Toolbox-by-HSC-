# Uses python3
import sys

def get_change_slow(m):
    #write your code here
    minCoins = m
    coinValueList = [1, 3, 4]
    if m in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= m]:
            numCoins = 1 + get_change(m-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins


def get_change(V):
    coins = [1, 3, 4]
    m = len(coins)
    table = [0 for i in range(V + 1)]
    table[0] = 0

    for i in range(1, V + 1):
        table[i] = sys.maxsize

    for i in range(1, V + 1):
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
    return table[V]



if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
