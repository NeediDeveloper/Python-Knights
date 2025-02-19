fruit_tuples = ("apple", "banana", "kiwi", 54, True, 3.4)
fruit_list = ["apple", "banana", "cherry"]
print(fruit_tuples)
print(fruit_list)

empty = ()
print(type(empty))

empty = ("45", )
print(type(empty))

print(fruit_tuples[0:3:2])
print(fruit_tuples[-3])

def get_coordinates():
    return (10, 20)
x, y = get_coordinates()
print(x, y) # Output: 10 20
