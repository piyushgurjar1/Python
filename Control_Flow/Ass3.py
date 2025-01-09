def check_balance(balance):
    print(f"Your current balance is: {balance[0]}")

def deposit(balance):
    try:
        amount = float(input("Enter the amount you want to deposit: "))
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            balance[0] += amount
            print(f"{amount} has been deposited.")
    except ValueError:
        print("Invalid input! ")

def withdraw(balance):
    try:
        amount = float(input("Enter the amount you want to withdraw: "))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > balance[0]:
            print("Insufficient funds! ")
        else:
            balance [0]-= amount
            print(f"{amount} has been withdrawn.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


print('''ATM Menu 
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit''')

balance = [0]
while True:
    choice = input("Choose an option (1-4): ")  

    if choice == "1":
        check_balance(balance) 
    elif choice == "2":
        deposit(balance)  
    elif choice == "3":
        withdraw(balance) 
    elif choice == "4":
        print("Thank you.")
        break  
    else:
        print("Invalid option!")  