student1 = {"name":"Naveed", 
            "age": 20,
            "city": "Gujranwala"}

print(student1["age"])

# print(student1["address"])
# print(student1.get("address"))

student1["height"] = 5.7
student1["name"] = "Needi Developer"
print(student1)

del student1["city"]
print(student1)

print(student1.keys())
print(student1.values())
print(student1.items())

class1 = {555: {"first_name": "Needi", "last_name": "Developer", "grade": "A", "age": 20},
          556: {"first_name": "Raza", "last_name": "Ahmad", "grade": "B", "age": 18},
          557: {"first_name": "Ahmad", "last_name": "Raza", "grade": "C", "age": 22},
          558: {"first_name": "Adam", "last_name": "Usman", "grade": "D", "age": 21},
          559: {"first_name": "Ali", "last_name": "Haider", "grade": "B", "age": 19},
          560: {"first_name": "Musa", "last_name": "Suleman", "grade": "A", "age": 20},}

print(class1[559]["first_name"])