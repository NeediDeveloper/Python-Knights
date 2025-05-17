data = input("Enter your name:")
if len(data) > 5:
    print(f"Your name, {data}, is long!")
    
if (data := input("Enter your name:")) and len(data) > 5:
    print(f"Your name, {data}, is long!")
