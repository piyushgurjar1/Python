class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if quantity <= 0:
            print("Quantity to add must be greater than zero.")
        else:
            if item_name in self.items:
                self.items[item_name] += quantity
            else:
                self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if quantity <= 0:
            print("Quantity to remove must be greater than zero.")
        elif item_name not in self.items:
            print(f"Error: {item_name} does not exist in inventory.")
        elif self.items[item_name] < quantity:
            print(f"Error: Not enough stock of {item_name}. Current stock: {self.items[item_name]}")
        else:
            self.items[item_name] -= quantity
            print(f"Removed {quantity} of {item_name}.")

    def check_stock(self, item_name):
        if item_name not in self.items:
            print(f"{item_name} is not in stock.")
        else:
            print(f"Current stock of {item_name}: {self.items[item_name]}")

inventory = Inventory()
inventory.add_item("Apple", 10)
inventory.add_item("Banana", 5)

inventory.check_stock("Apple")
inventory.check_stock("Mango")

inventory.remove_item("Apple", 3)

