class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"Deposited Rs{amount}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Error: Insufficient funds for this withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew Rs{amount}.")

    def check_balance(self):
        print(f"Current balance: Rs{self.balance}")

maccount = BankAccount(100)
account.check_balance()
account.deposit(50)
maccount.withdraw(30)
