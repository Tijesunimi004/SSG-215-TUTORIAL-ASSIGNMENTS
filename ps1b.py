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
    semi_annual_raise= input("Enter the percentage your raise is: ")
    if semi_annual_raise.isdigit():
        semi_annual_raise = float(semi_annual_raise)
        semi_annual_raise = semi_annual_raise / 100
        break
    else:
        print("Enter valid percent.")
        continue

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




while current_savings < portion_down_payment:
    return_of_investment = (0.04 * current_savings) / 12
    monthly_salary = annual_salary / 12

    if num_months % 6 == 0 and num_months > 0:
        annual_salary += (semi_annual_raise * annual_salary)
        current_savings += return_of_investment + (monthly_salary * percent_portion_saved)
    else:
        current_savings += return_of_investment + (monthly_salary * percent_portion_saved)
        (monthly_salary * percent_portion_saved)

    num_months += 1    


print(f"The total number of months needed for down payments is {num_months}")
