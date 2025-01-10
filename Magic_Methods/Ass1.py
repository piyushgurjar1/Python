class Transaction:
    def __init__(self, amount, description):
        self.amount = amount  
        self.description = description  

    def __repr__(self):
        return f"Transaction(amount={self.amount}, description='{self.description}')"

   
    def __eq__(self, other):
        if isinstance(other, Transaction):
            return self.amount == other.amount and self.description == other.description
        return False  

    def __add__(self, other):
        if isinstance(other, Transaction):
           
            new_amount = self.amount + other.amount
            new_description = f"{self.description} + {other.description}"
            return Transaction(new_amount, new_description)
        return NotImplemented
    
  
trans1 = Transaction(100, "Tea")
trans2 = Transaction(50, "Coffee")

print(trans1)
print(trans2)  

print(trans1 == trans2)  

trans = trans1 + trans1
print(trans)  
