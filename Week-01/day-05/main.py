import csv
from sales_functions import calculate_total_revenue

orders = []

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        orders.append({
            "product": row["product"],
            "price": float(row["price"]),
            "quantity": int(row["quantity"])
        })

total = calculate_total_revenue(orders)

print(f"Total Revenue: {total}")
