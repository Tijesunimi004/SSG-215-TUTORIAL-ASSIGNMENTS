# Constants
total_cost = 1000000  # Cost of the house
down_payment = 0.25 * total_cost  # Down payment is 25% of the cost of the house
annual_return_rate = 0.04  # Annual investment return rate
months = 36  # Number of months for saving
semi_annual_raise = 0.07  # Semi-annual raise is 7%
current_savings = 0
# Input: Starting annual salary
annual_salary = float(input("Enter the starting annual salary: "))

# Initialize variables for binary search
low = 0.0
high = 1.0
epsilon = 0.01  # Tolerance for the difference between savings and down payment
num_guesses = 0

while abs(current_savings - down_payment) > epsilon and num_guesses < 10000:
    current_savings = 0
    annual_salary_copy = annual_salary  # Make a copy of the initial annual salary
    savings_rate = (low + high) / 2  # Calculate savings rate as a decimal

    for month in range(months):
        current_savings += current_savings * (annual_return_rate / 12)  # Investment return
        current_savings += (annual_salary_copy / 12) * savings_rate  # Monthly savings
        if month % 6 == 0:
            annual_salary_copy += annual_salary_copy * semi_annual_raise  # Apply semi-annual raise

    if current_savings < down_payment:
        low = savings_rate
    else:
        high = savings_rate
    num_guesses += 1

# Print the result
if num_guesses < 10000:
    print(f"Best savings rate: {savings_rate:.4f}")
    print("Steps in binary search:", num_guesses)
else:
    print("It is not possible to pay the down payment in three years with this salary.")
