# Iterators
numbers = [10, 20, 30]
iterator = iter(numbers) 
print(next(iterator)) 
print(next(iterator)) 
print(next(iterator))

# Generators
def count_up_to(n):
    count = 1
    while count <= n:
        yield count 
        count += 1
        
counter = count_up_to(8)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
