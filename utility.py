import random as rand
import os

class Product:
    def __init__(self, name, price, quantity, product_Id):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.productID = product_Id

class Customer:
    def calculateDiscount(self, initial_amt):
        if initial_amt >= 20000:
            return initial_amt - (initial_amt * 0.3)
        elif initial_amt >= 10000:
            return initial_amt - (initial_amt * 0.2)
        elif initial_amt >= 5000:
            return initial_amt - (initial_amt * 0.1)
        elif initial_amt > 1000:
            return initial_amt - (initial_amt * 0.05)
        else:
            return initial_amt 
        
    def __init__(self, name, ph_No, purchases, initial_amt, discountedAmt):
        self.name = name
        self.phNo = ph_No
        self.purchases = purchases
        self.initialAmt = initial_amt
        discountedAmt = self.calculateDiscount(initial_amt)
        self.discountedAmt = discountedAmt

    def info(self):
        info = {
            "Customer Name": self.name,
            "Phone Number": self.phNo,
            "Purchases": self.purchases,
            "Initial Amount": self.initialAmt,
            "Amount after Discount": self.discountedAmt
        }
        return info

# Initialize the product dictionary
products = {}

# Function to add items into the inventory
def add_item(name, price, quantity, product_Id, inventory):
    inventory.write(f"{product_Id} {name} {price} {quantity}\n")
    obj = Product(name, price, quantity, product_Id)
    products[obj.name] = [obj.price, obj.quantity]

# Function to display inventory details
def inventory_details():
    print("Products in inventory: ")
    for product in products:
        print(f"Item: {product}, Price: {products[product][0]}")

# Function to initialize inventory
def initialize_inventory():
    path = r"c:\Users\USER\OneDrive\Desktop\Inventory Management System\inventory.txt"
    
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        inventory = open(path, "w")
        inventory.close()
        inventory = open(path, "a")
    else:
        inventory = open(path, "a")

    if os.stat(path).st_size == 0:
        n = int(input("Enter the number of items in the inventory to add: "))
        for i in range(n):
            name = input("Enter product name: ")
            productId = rand.randint(10000, 20000)
            price = int(input("Enter price of product: "))
            quantity = int(input("Enter quantity of product available: "))
            add_item(name, price, quantity, productId, inventory)
            print("\n")
        inventory.close()
    else:
        load_products_from_file(path)

# Function to load products from inventory file
def load_products_from_file(path):
    with open(path, "r") as inventory:
        for line in inventory:
            productId, name, price, quantity = line.strip().split()
            price = int(price)
            quantity = int(quantity)
            products[name] = price
            obj = Product(name, price, quantity, productId)
            products[obj.name] = [obj.price, obj.quantity]

# Ensure the products are loaded from the file when the module is imported
path = r"c:\Users\USER\OneDrive\Desktop\Inventory Management System\inventory.txt"
if os.path.exists(path) and os.stat(path).st_size > 0:
    load_products_from_file(path)
    
# Function to update product quantity in the inventory file
def update_product_quantity(name, purchased_quantity):
    updated_lines = []
    
    with open(path, "r") as inventory:
        for line in inventory:
            productId, prod_name, price, quantity = line.strip().split()
            if prod_name == name:
                new_quantity = int(quantity) - purchased_quantity
                if new_quantity < 0:
                    print(f"Not enough {name} in stock.")
                    return False
                quantity = str(new_quantity)
            updated_lines.append(f"{productId} {prod_name} {price} {quantity}\n")
    
    with open(path, "w") as inventory:
        inventory.writelines(updated_lines)
    return True

# Ensure initialization only happens when the script is executed directly
if __name__ == "__main__":
    initialize_inventory()
    inventory_details()
