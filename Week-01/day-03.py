#FUNCTION - 
def greet():
    print("Welcome to Python!")

greet()

#PARAMETER & ARGUMENTS -
def greet_user(name): #name is a parameter
    print(f"Welcome, {name}!")
    
greet_user("AASTHA") # "AASTHA" is an argument

#types of arguments
#1. Positional arguments
def calculate_total(price, quantity):
    total = price * quantity
    print(total)

calculate_total(100, 5) # 100 is the price argument, 5 is the quantity argument

#2. Keyword arguments
def calculate_total(price, quantity):
    total = price * quantity
    print(total)

calculate_total(price=100, quantity=5) # 100 is the price argument, 5 is the quantity argument

#3. Default arguments
def calculate_total(price, quantity=1): # quantity has a default value of 1
    total = price * quantity
    print(total)

calculate_total(100) # 100 is the price argument, quantity defaults to 1    

# return & print 
def add(a, b):
    print(a + b)

result = add(10, 20)
print(result) # none is printed because the function does not return any value, it only prints the sum.

def add(a, b):
    return a + b

result = add(10, 20)
print(result) # 30 is printed because the function returns the sum.

#lambda function
square = lambda x: x ** 2
print(square(5)) # 25 is printed because the lambda function returns the square of the input.







#sample data
orders = [
    {"product": "Laptop", "price": 50000, "quantity": 2},
    {"product": "Mouse", "price": 500, "quantity": 5},
    {"product": "Keyboard", "price": 1500, "quantity": 3},
    {"product": "Monitor", "price": 12000, "quantity": 2},
    {"product": "Headphones", "price": 2000, "quantity": 4}
]
#Exercise 1 – Calculate individual order totals
def calculate_order_total(order):
    return order["price"] * order["quantity"]

for order in orders:
    total = calculate_order_total(order)
    print("Total for", order['product'], ":", total) 
    
#Exercise 2 – Calculate total revenue
def calculate_total_revenue(orders):
    total_revenue = 0
    for order in orders:
        total_revenue += calculate_order_total(order)
    return total_revenue

total_revenue = calculate_total_revenue(orders)
print("Total revenue:", total_revenue)

#Exercise 3 – Find expensive products
def find_expensive_products(orders, minimum_price=2000):
    expensive_products = []
    for order in orders:
        if order["price"]> minimum_price:
            expensive_products.append(order["product"])
    return expensive_products

products = find_expensive_products(orders)
print("EXPENSIVE PRODUCT LIST -", products)

#Exercise 4 – Calculate total units sold
def calculate_total_unit_sold(orders):
    total_units =0 
    for order in orders:
        total_units += order["quantity"]
    return total_units

total_units_sold = calculate_total_unit_sold(orders)
print("Total units sold:", total_units_sold)

#Exercise 5 – Use keyword arguments
#Call your find_expensive_products() function using keyword arguments and set the minimum price to 10000.
products = find_expensive_products(orders, minimum_price = 10000)
print("EXPENSIVE PRODUCT LIST -", products)
