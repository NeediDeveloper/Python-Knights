fruits = ["apple","banana","cherry"]
for index, fruit in enumerate(fruits, start=15):
    print(f"Index: {index}, Fruit: {fruit}")
    
    
names = ["Naveed","Sara","Fatima", "Maheen"]
scores = [90, 85, 88, 59, 45]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

keys = ["name", "age", "city", "country", "grade"]
value = ["Needi Developer", 20, "Gujranwala", "Pakistan", "A"]
dictionary = dict(zip(keys, value))
print(dictionary)
