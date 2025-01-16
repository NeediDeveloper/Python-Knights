# Escape Sequences
print("Hello \n\nWorld")

print("Name:\tNeedi Devloper")

# Output: She said,"Hello!"
print("She said, \"Hello!\"")

print('It\'s raining outside')

print("This is a backslash: \\ ")

print("This is a \rbackslash: \\ ")

print("Helloo\b!")


# F Strings
name ="Naveed"
age = 20
# print("My name is" , name , "and I am" , age , "years old")
print(f"My name is {name} and I am {age} years old.")
print(f"My Age is {age} and My name is {name}")

divide = 10 /3
print(f"The result is {divide:.2f}")

# Doc Strings
def greet(name):
    """
    This function greets the person whose name is passed as an
    argument.
    """
    return f"Hello,{name}!"
print(greet("Naveed"))
print(help(greet))
# Output: Hello, Naveed!