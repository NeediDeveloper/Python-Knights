numbers = [10, 20, 30, 40]
iterator = iter(numbers)
print(next(iterator)) 
print(next(iterator)) 
print(next(iterator)) 
print("This is another line of code")
print(next(iterator)) 

def count_up_to(n):
    count = 1
    while count <= n:
        yield count 
        count += 1

counter = count_up_to(100)
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 
