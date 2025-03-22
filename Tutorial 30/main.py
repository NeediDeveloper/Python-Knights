with open("file.txt","r") as file:
    content = file.readlines()
    print(content[1])

with open("file.txt","w") as file:
    file.write("This is adding by main.py file")