import os
import random
import time
import new

# This will print the current working directory
print("Current Directory:", os.getcwd())

# This will create a new directory named "Mera new Folder" in the current working directory
os.mkdir("Mera new Folder")

#  this will print the random choice from the list
choices = ["Apple","Banana","Cherry"]
print("Random choice:", random.choice(choices))

# this will print the current time in HH:MM:SS format
print("Current Time: " + time.strftime("%H:%M:%S"))
new.greet()