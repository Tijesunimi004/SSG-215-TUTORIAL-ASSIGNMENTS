quantity = int(input("Enter the quantity of items bought: "))

unit_cost = 100
amount_needed = quantity * unit_cost

if amount_needed > 1000:
    discount = (10 / 100) * amount_needed
    amount_to_be_paid = amount_needed - discount
    print(f"After your 10% discount you'll be paying {amount_to_be_paid:.2f}")
else:
    print("You're not eligible for this discount.")

