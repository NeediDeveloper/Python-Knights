def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!") # Custom error
    elif age > 150:
        raise ValueError("Age cannot be more than 150!")
    # Custom error
    else:
        print(f"Your age is valid: {age}")
        
try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError as e:
    print(f"Error: {e}")

class rat_ky_time_Mobile_use_mat_karo(Exception):
    pass

try:
    time = int(input("Enter the time of your mobile: "))
    if time > 10:
        raise rat_ky_time_Mobile_use_mat_karo("Raat ke 10 baje ke baad mobile use mat karo")
    else:
        print("Mobile use kar sakte ho")
except rat_ky_time_Mobile_use_mat_karo as e:
    print(f"Error: {e}")