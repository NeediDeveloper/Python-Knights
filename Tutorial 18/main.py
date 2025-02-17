# List banani
numbers = [1, 2, 3, 4, 5]
fruits = ["apple","banana","cherry"]
mixed = [1,"hello", 3.5, True]

# List ko print karna
print(numbers) # [1, 2, 3, 4, 5]
print(fruits) # ['apple','banana','cherry']
print(mixed) # [1,'hello', 3.5, True]


Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(Numbers[-5])



Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(Numbers[0:10:3])

fruits = ["apple","banana","cherry", "dates", "grapes", "kiwi", "mango"]
dry_fruits = ["Badam", "Kaju", "Kishmish", "Pista", "Akharot"]
fruits.append("orange")
fruits.insert(3, "stawberry")
fruits.remove("grapes")
fruits.pop(2)
fruits.clear()
dry_fruits.extend(fruits)

print(dry_fruits)