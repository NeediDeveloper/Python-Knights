def greet():
    print("Hello, welcome to Python Knight!")
greet() # Function ko call kar rahe hain


def greet_person(name):
    print(f"Hello, {name}\nWelcome to Python Knight!")
    
User_name = input("Enter Your Good Name: ")
greet_person(User_name)

def add(a, b):
    result = a + b
    return result
    # Function ko call karke result print karte hain
sum_result = add(5, 6)
print("Sum:", sum_result)