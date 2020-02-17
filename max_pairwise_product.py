# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def imporved_max_products(numbers):
    n = len(numbers)
    max_num = max(numbers)
    numbers.remove(max_num)
    sec_num = max(numbers)
        
    return max_num * sec_num
    

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
    print(imporved_max_products(input_numbers))
