# Uses python3
# knapsack problem

import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    value_perunit_weight = [x/y for x, y in zip(values, weights)]

    #print(value_perunit_weight)

    while capacity and len(value_perunit_weight) != 0:
        #print(max(value_perunit_weight))
        max_value_rn = max(value_perunit_weight)
        max_value_index = value_perunit_weight.index(max_value_rn)
        value_perunit_weight.remove(max_value_rn)

        check = capacity - weights[max_value_index]
        #print(check)
        if check > 0 :
            value += values[max_value_index]
            capacity = capacity - weights[max_value_index]

        else :
            value += max_value_rn * capacity
            capacity = 0
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    #print(values)
    weights = data[3:(2 * n + 2):2]
    #print(weights)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

