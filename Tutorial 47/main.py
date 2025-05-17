def cube(n):
    return n * n * n


cube1 = lambda n: n * n * n
 
print(f"This is Lambda Function: {cube1(5)}")
print(f"This is Function: {cube(5)}")