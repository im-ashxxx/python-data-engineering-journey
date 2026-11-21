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

def calculate_discount(price, discount_percentage):
    if discount_percentage <= 0 or discount_percentage >= 100:
        print("Discount percentage must be between 0 and 100.")
        return None
    else:
        discount_amount = price * (discount_percentage / 100)
        return price - discount_amount
