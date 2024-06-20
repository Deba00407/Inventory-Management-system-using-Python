from utility import *

def make_string(k, v):
    key, val = k, v
    string = str(key) + " : "
    string += str(val)
    return string + '\n'

print("-" * 40)
inventory_details()
print("-" * 40, '\n')

purchases = {}
customer_details =  {'Name:' : "", 'Phone number:' : 0, 'Purchases: ' : purchases, 'Initial Amount:' : 0, 'Discounted Amount' : 0}
for i in range(len(customer_details)):
    if i == 0:
        name = input("Enter your name: ")
        customer_details["Name:"] = name
    elif i == 1:
        phNo = int(input("Enter your phone number: "))
        customer_details["Phone number:"] = phNo
    elif i == 2:
        p = 1
        while(p):
            p = int(input("\nEnter 1 for entering your purchases and 0 to stop: "))
            if p == 0:
                break
            n = input("Enter product name: ")
            q = int(input("Enter product quantity: "))
            if q > products[n][1]:
                print("Sorry! The desired quantity is not available in the inventory")
                continue
            else:
                purchases[n] = q
                products[n][1] -= q
                update_product_quantity(n, q)
        customer_details["Purchases: "] = purchases
    elif i == 3:
        sum = 0
        for product in purchases:
            sum += (products[product][0] * purchases[product])
        customer_details["Initial Amount:"] = sum

sales_cnt = rand.randint(0, 100)
filename = f"cust{sales_cnt}.txt"
cust = open(f"./Inventory Management System/Sales Executed/{filename}", "w")
cust.close()
cust = open(f"./Inventory Management System/Sales Executed/{filename}", "a")

# Making an object of the customer class
c = Customer(customer_details['Name:'], customer_details['Phone number:'],
                    customer_details['Purchases: '], customer_details["Initial Amount:"], customer_details["Discounted Amount"])
cust.writelines(make_string(k, v) for k,v in c.info().items())
            
            
    

