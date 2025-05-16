numbers = [4, 9, 7, 2, 4, 8, 20, 12, 3]

# MAP
def square(n):
    return n * n 

squared_numbers = list(map(square, numbers))
print(squared_numbers)

# FILTER
def odd(n):
    return n % 2 != 0
odd_numbers = list(filter(odd, numbers))
print(odd_numbers)

# REDUCE
from functools import reduce

def sum(x, y):
    return x + y

sum_of_numbers = reduce(sum, numbers)
print(sum_of_numbers)