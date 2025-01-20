age = 16

if age < 18:
    print("You are a minor.")
# elif age == 18:
#     print("Congratulations! You are an adult now.")
else:
    print("You are an adult.")
    
    
marks = 1

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: C")


balance = 5000
withdrawal = 5000
if withdrawal > balance:
    print("Insufficient balance.")
elif withdrawal == balance:
    print("Your account will be empty after this transaction.")
else:
    print(f"Transaction successful! Remaining balance: {balance - withdrawal}")