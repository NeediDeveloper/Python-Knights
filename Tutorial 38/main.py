class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name} is {self.age} years old.")
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Naveed", 20)
print(repr(person))
print(person)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Naveed", 20)
print(repr(person))
print(person)


