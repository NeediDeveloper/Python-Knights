balance = 10000
while True:
    print("1. Check Balance")
    print("2. Withraw Money")
    print("3. Exit")
    choices = int(input("Enter here: "))
    if choices == 1:
        print(f"Your balance is: ${balance}")
    elif choices == 2:
        amount = int(input("Enter amount: "))
        # balance -= amount if amount <= balance else 0
        if amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print(f"Successfully withdrawn ${amount}")
            print(f"Your remaining balance is: ${balance}")
    elif choices == 3:
        print("Thank you for using our service")
        break
    else:
        print("Invalid choice")