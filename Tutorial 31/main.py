with open("example.txt","r") as file:
    file.seek(4) 
    print(file.tell())
    content = file.read() 
    print(content)
    
with open("example.txt","rb") as file:
    file.seek(-5, 2)
    content = file.read()
    print(file.tell())
    print(content.decode('utf-8'))
