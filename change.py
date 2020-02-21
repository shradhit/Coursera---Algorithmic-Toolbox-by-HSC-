# Uses python3
"""
You have three coins 10, 5, 1. Minimum number of coins required to make up the number 'm'.
"""

import sys

def get_change(m):
    x = y = x1 = y1 = 0
    
    x = m / 10
    y = m % 10
    x1 = y / 5
    y1 = y % 5
    ans = int(x) + int(x1) + y1
    return ans

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
