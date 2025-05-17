import os 
import math
import random

dir_name = "RandomFiles"
os.mkdir(dir_name)

file_names = []
for i in range(5):
    random_number = random.randint(1000, 9999)
    file_name = f"{random_number}.txt"
    file_names.append(file_name)
    
for file_name in file_names:
    number =  random.uniform(1, 500)
    sqaure_root = math.sqrt(number)
    file_path = os.path.join(dir_name, file_name)
    with open(file_path, "w") as file:
        file.write(f"Random number: {number:.2f}\n")
        file.write(f"Sqaure root: {sqaure_root:.2f}\n")
print("Files created successfully!")

for file_name in file_names:
    print(f"File name: {file_name}")

    