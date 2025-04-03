class Car:
    def __init__(self, brand, color):
        self.brand = brand 
        self.color = color 
        
        
my_car = Car("Honda","Blue")
print(my_car.brand) 
print(my_car.color)

my_fried_car = Car("Toyota", "White")
print(my_fried_car.brand) 
print(my_fried_car.color) 

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old and my city is {self.city}.")
   
person1 = Person("Naveed", 20, "Gujranwala")
person1.greet()
