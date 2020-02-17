""" 

Inputs : 
4
5 2 3 6

Output :
30  

"""

# very base line code 
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product



# more pythonic, faster and also less space requitement 
def imporved_max_products(numbers):
    n = len(numbers)
    max_num = max(numbers)
    numbers.remove(max_num)
    sec_num = max(numbers)

    return max_num * sec_num


input_n = int(input())
input_numbers = [int(x) for x in input().split()]
#print(input_numbers)
print(imporved_max_products(input_numbers))
