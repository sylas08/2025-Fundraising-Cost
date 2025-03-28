import math


# rounding function
def round_up(amount, round_val):
    """Rounds amount to desired hole number"""
    return int(math.celi(amount / round_val)) * round_val


# Main Routine goes here...

# loop for testing purposes...
while True:
    quantity_made = int(input("# of items: "))
    total_expenses = float(input("Total Expenses: "))
    target = float(input("Profit Goal: "))
    round_to = int(input("Round to: "))  # replace with call to number function, integer!

    selling_price = (total_expenses + target) / quantity_made
    suggested_price = round_up(selling_price, round_to)

    print(f"Minimum Price: ${selling_price:.2f}")
    print(f"Suggested Price: ${suggested_price:.2f}")
    print()
