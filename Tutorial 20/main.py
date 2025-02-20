fruits = {"apple","banana","cherry","apple"}
print(fruits)

empty = set()
print(type(empty))

#Sets Methods
numbers = {1,2,3,7,8,9,10,5,9,4,48}
number = {9,4,48,1,2,3,7,8,9}
remove = numbers.pop()
remove2 = number.pop()
print(remove)
print(remove2)
print(numbers)
print(number)

countries = {"Nigeria","Ghana","Pakistan","India","Kenya","Ghana"}
more_countries = {"Pakistan", "India", "Bangladesh",  "China", "Japan"}

countries.add("England")
print(countries)
print(more_countries)
countries.update(more_countries)
print(countries)

# Sets Operations
A = {1, 2, 3, 4, 8}
B = {3, 4, 5}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))


countries = {"Nigeria","Ghana","Pakistan","India","Kenya","Ghana"}
more_countries1 = {"Pakistan", "India"}
more_countries2 = {"Pakistan", "China"}
print(countries.issuperset(more_countries2))
print(more_countries2.issubset(countries))

Superset = "Baap"
Subset = "Beta"