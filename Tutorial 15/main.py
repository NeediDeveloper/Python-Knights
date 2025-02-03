# def greet(name="Sir/Madam"):
#     print(f"Hello, {name}!")
# greet("Naveed") # Output: Hello, Naveed!
# greet() # Output: Hello, User!

# def add_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# print(add_numbers(1, 2, 3)) # Output: 6
# print(add_numbers(10, 20, 30, 40)) # Output: 100
# print(add_numbers(1,2,8,6,4,9,3,4,85,321,87,1231,546))
# print(add_numbers(5))

def print_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")
print_info(name="Needi", age=20, city="Gujranwala")

