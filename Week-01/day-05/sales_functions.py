def calculate_revenue(price, quantity):
    return price * quantity

def calculate_total_revenue(orders):
    total = 0

    for order in orders:
        total += calculate_revenue(
            order["price"],
            order["quantity"]
        )

    return total
