class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.03):
        super().__init__(owner, balance) 
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}.")


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, transaction_limit=5,loan_eligibility=5000):
        super().__init__(owner, balance)
        self.transaction_limit = transaction_limit
        self.loan_eligibility = loan_eligibility
        self.rewards_points = 0

    def withdraw(self, amount):
        if amount > self.transaction_limit:
            print(f"Transaction exceeds limit of {self.transaction_limit}. Withdrawal denied.")
        elif amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    

    def loan_eligibility(self):
        if self.balance >= self.loan_eligibility:
            print("Eligible for loan.")
        else:
            print("Not eligible for loan.")

    def reward_program(self):
        if self.balance > 0:
            self.rewards_points += self.balance // 100  
            print(f"Rewards points earned: {self.rewards_points}")
        else:
            print("No rewards earned. Balance is zero.")



account1 = BankAccount("Piyush")
account1.deposit(1000)
account1.withdraw(500)
print("Final balance:", account1.get_balance())



savings_account = SavingsAccount("Piyush", 1000)
savings_account.add_interest()  

checking_account = CheckingAccount("Piyush", 1500)
checking_account.withdraw(600)


checking_account.loan_eligibility()
checking_account.reward_program()  
