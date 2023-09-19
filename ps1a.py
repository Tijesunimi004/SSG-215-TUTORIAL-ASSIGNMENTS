"""
A program to calculate the number of months to get your dream home.

Input Values:
- 
"""
#Varirable Definitions are in the pdf 
#Below is question 1


current_savings = 0


while True:
    total_cost = input("Enter the cost of your dream house: ")
    if total_cost.isdigit():
        total_cost = float(total_cost)
        break
    else:
        print("Please enter a nummber.")
        continue

while True:
    annual_salary = input("Enter your annual salary: ")
    if annual_salary.isdigit():
        annual_salary = float(annual_salary)
        break
    else:
        print("Enter valid salary")

while True:
    portion_saved = input("Enter the percentage you want to save: ")
    if portion_saved.isdigit():
        portion_saved = float(portion_saved)
        percent_portion_saved = portion_saved / 100
        break
    else: 
        print("Enter valid percent.")
        continue


# Calculate the down payment
portion_down_payment = 0.25 * total_cost

num_months = 0 

monthly_salary = annual_salary / 12


while current_savings < portion_down_payment:
    return_of_investment = (0.04 * current_savings) / 12

    current_savings += return_of_investment + (monthly_salary * percent_portion_saved)

    num_months += 1


print(f"The total number of months needed for down payments is {num_months}")






