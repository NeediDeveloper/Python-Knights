class BankAccount():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def check_balance(self):
        return f"{self.owner}, your balance is {self.balance:.2f}."
    
    def deposit_money(self, amount):
        if amount > 0:
            self.balance += amount
            print("Transaction successful.")
            print(f"Your new balance is: {self.balance:.2f}")
        else:
            print("Please enter a valid amount.")
    def withdraw_money(self, amount):
        if amount < 0:
            print("Please enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Transaction successful.")
            print(f"Your new balance is: {self.balance:.2f}")
        
def main():
    print("Welcome to Python Knights Bank!")
    owner = input("Please enter your name: ")
    account = BankAccount(owner=owner)
    print(f"Welcome {account.owner}! Your account has been created.")
    
    while True:
        print("Menu:")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print(account.check_balance())
        elif choice == 2:
            amount = float(input("Enter the amount to deposit: "))
            account.deposit_money(amount)
        elif choice == 3:
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw_money(amount)
        elif choice == 4:
            print(f"Thanks for using Python Knights Bank,\n{account.owner} Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
main()