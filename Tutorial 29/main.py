# READING A FILE
file = open("file.txt", "r")
content = file.read()
print(content)
file.close()

# WRITING A FILE
file = open("file1.txt", "w")
file.write("Needi Developer is the author or Python Knights Book.\n")
# file.close()
# file = open("file1.txt", "w")
file.write("Needi Developer is a good teacher.")
file.close()

# APPENDING A FILE
file = open("file.txt", "a")
file.write("\nHello world.")
file.close()

# READ AND WRITE
file = open("file.txt","r+")
content = file.read()
print("Current content:", content)
file.write("\nAdding this line after reading!")
file.close()

# OPEN A FILE USING WITH STATEMENT
with open("file.txt", "a") as file:
    content = file.write("\nThis Line is added using with statement.")
    print(content)