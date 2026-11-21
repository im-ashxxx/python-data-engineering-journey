#string
product = "Laptop"
company = "Microsoft"
print(product)
print(type(company))

#indexing
name = "PYTHON"
print(name[0])   # P
print(name[1])   # Y
print(name[-1])  # N

#slicing
language = "PYTHON"
print(language[0:3])  # PYT
print(language[2:5])  # THO
print(language[:4])   # PYTH
print(language[2:])   # THON

#string methods
product = "  laptop COMPUTER  "

print(product.upper())
print(product.lower())
print(product.strip())
print(product.replace("laptop", "desktop"))
print(product.split())
print(product.join(["  ", "laptop", " ", "COMPUTER", " . "]))
print(product.find("lap"))
print(product.startswith("  laptop"))
print(product.endswith("COMPUTER  "))

#file handling
#write mode
file = open("sales.txt", "w")

file.write("Laptop sales: 50000\n")
file.write("Mouse sales: 5000\n")

file.close()

#read mode
file = open("sales.txt", "r")
content = file.read()
print(content)
file.close()

#append mode
file = open("sales.txt", "a") #a mode is used to append data to the file without overwriting existing content.
file.write("Keyboard sales: 3000\n")
file.close()

#with open statement -- Python automatically closes the file when the with block finishes, even if an error occurs.
with open("sales.txt", "r") as file:
    content = file.read()
    print(content)
    
#file handling with exception handling
try:
    with open("sales.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Sales file was not found.")
    
#csv file handling

#reading from a CSV file
import csv

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
        
#writing to a CSV file
import csv

data = [
    {"product": "Laptop", "price": 50000},
    {"product": "Mouse", "price": 500}
]

with open("output.csv", "w", newline="") as file:
    fieldnames = ["product", "price"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)
    
    
#practice 
#Exercise 1 – String cleaning
product = "  LAPTOP computer  "
print(product.strip().lower().replace("computer","device"))

#Exercise 2 – String slicing
company = "MICROSOFT"
print(company[:3])#First three characters.
print(company[-3:])#Last three characters.
print(company[2:6])#Characters from index 2 to 6.

#Exercise 3 – File writing and reading
with open("company.txt", "r") as file:
    content = file.read()
    print(content)
    
#Exercise 4 – CSV processing Read sales.csv using csv.DictReader.    Print: Each product name.Each product's price. ,Each product's quantity.
import csv
with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Product: {row['product']}, Price: {row['price']}, Quantity: {row['quantity']}")
        
#Exercise 5 – Calculate total revenue from CSV
def calculate_revenue_from_csv(sales_csv):
    total_revenue = 0 
    with open(sales_csv, "r") as file:
        reader=csv.DictReader(file)
        for row in reader :
            total_revenue += float(row["price"]) * int(row["quantity"])
    return total_revenue

total_revenue = calculate_revenue_from_csv("sales.csv")
print(f"Total Revenue: {total_revenue}")
    
#Exercise 6 – Exception handling for file reading
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
