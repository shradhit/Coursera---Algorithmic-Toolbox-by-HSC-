# Uses python3
import sys


def get_optimal_new(capacity, weights, values):
    value = 0.
    j = 0
    # write your code here
    value_perunit_weight = [x/y for x, y in zip(values, weights)]
    value_perunit_weight_dict = {k: v for v, k in enumerate(value_perunit_weight)}
    value_perunit_weight_dict_sorted = {}
    for i in sorted(value_perunit_weight_dict, reverse=True):
        value_perunit_weight_dict_sorted.update({i:value_perunit_weight_dict[i]})
    while capacity and j < len(value_perunit_weight_dict_sorted):
        #print('abc')
        #print(list(value_perunit_weight_dict_sorted.keys())[j])
        max_value_rn = list(value_perunit_weight_dict_sorted.keys())[j]
        max_value_index = value_perunit_weight_dict_sorted.get(max_value_rn)
        check = capacity - weights[max_value_index]
        #print(j)
        j += 1
        #print(j)
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
    opt_value = get_optimal_new(capacity, weights, values)
    print("{:.10f}".format(opt_value))

