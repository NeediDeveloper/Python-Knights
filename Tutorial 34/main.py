# SINGLE INHERITANCE
class Animal:
    def speak(self):
        print("Animals make sounds.")

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")
        
dog = Dog()
dog.speak()
dog.bark() 

# MULTIPLE INHERITANCE
class Mother:
    def care(self):
        print("Mother takes care.")

class Father:
    def protect(self):
        print("Father provides protection.")

class Child(Mother, Father):
    def play(self):
        print("Child loves to play!")
child = Child()
child.care() 
child.protect() 
child.play() 

# MULTILEVEL INHERITANCE
class Vehicle:
    def info(self):
        print("Vehicles are used for transportation.")

class Car(Vehicle):
    def car_type(self):
        print("Car is a personal vehicle.")

class SportsCar(Car):
    def speed(self):
        print("SportsCar is very fast!")

sports_car = SportsCar()
sports_car.info()
sports_car.car_type() 
sports_car.speed() 