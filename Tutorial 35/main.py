class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

animal = Animal()
dog = Dog()
animal.speak() 
dog.speak() 


class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car is now ready to drive.")
        
car = Car()
car.start()