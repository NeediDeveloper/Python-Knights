#Simple
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(5))

#Advanced
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
         return False
    for i in range(3, int(n**0.5)+ 1, 2):
        if n % i == 0:
            return False
    return True
check_number = int(input("Enter a number: "))

if is_prime(check_number):
    print(f"{check_number} is a prime number")
else:
    print(f"{check_number} is not a prime number")

# for i in range(1, 100, 2):
#     print(i)