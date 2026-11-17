# Create variables for your name, age, percentage and whether you are learning Python. Print their data types
name = "AASTHA"
age = 22
percentage = 85.5
is_learning_python = True

print(type(name))
print(type(age))
print(type(percentage))
print(type(is_learning_python))

#Create a list of 6 product prices. Print the first, third and last prices.
product_prices = [10.99, 25.50, 5.75, 15.25, 30.00, 20.00]
print("First price:", product_prices[0])
print("Third price:", product_prices[2])
print("Last price:", product_prices[-1])

#Add a new price to the list, remove one price and sort the list.
product_prices.append(11.1)
product_prices.remove(5.75)
product_prices.sort()
print("Updated product prices:", product_prices)

#Create a set with repeated customer IDs. Print the set and observe what happens.
customer_ids = {101, 102, 103, 102, 104, 103}
print("Customer IDs:", customer_ids) #it will print unique customer IDs only, duplicates are removed.

#Create an employee dictionary with name, department, salary and experience. Print each value and update the salary.
employee = {
    "name": "AASTHA",
    "department": "IT",
    "salary": 50000,
    "experience_years": 2
}
print("Employee Name:", employee["name"])
print("Employee Department:", employee["department"])
print("Employee Salary:", employee["salary"])
print("Employee Experience:", employee["experience_years"])

# Update the salary
employee["salary"] = 55000
print("Updated Employee Salary:", employee["salary"])



## level 2 ##
#Problem: Mini E-commerce Data Analysis

orders = [
    {"customer": "A", "amount": 1200, "status": "completed"},
    {"customer": "B", "amount": 2500, "status": "pending"},
    {"customer": "A", "amount": 1800, "status": "completed"},
    {"customer": "C", "amount": 3200, "status": "completed"},
    {"customer": "B", "amount": 1500, "status": "cancelled"}
]

#  Write a program to find: 1. Total number of orders. 2. Total revenue from completed orders only. 3. Number of completed orders. 4. Unique customers. 5. Highest order amount.

total_orders = len(orders)
print("Total no. of orders : ", total_orders)

completed_orders_revenue = 0
completed_orders_count = 0
for order in orders:
    if order["status"] == "completed":
        completed_orders_revenue  = completed_orders_revenue + order["amount"]
        completed_orders_count = completed_orders_count + 1
        
print("Total revenue from completed orders : ", completed_orders_revenue)
print("Number of completed orders : ", completed_orders_count)

set_of_customers = set(order["customer"] for order in orders)
print("Unique customers : ", set_of_customers)

highest_order_amount = max(order["amount"] for order in orders)
print("Highest order amount : ", highest_order_amount)
