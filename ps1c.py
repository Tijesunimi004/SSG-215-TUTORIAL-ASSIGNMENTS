
while True:
    annual_salary = input("Enter the starting salary: ")
    if annual_salary.isdigit():
        annual_salary = float(annual_salary)
        break
    else:
        print("Please enter a nummber.")
        continue


low = 0
high = 10000
goal_month = 36
num_month = 0
current_savings = 0
semi_annual_raise = 0.07
num_tries = 0
down_payment = 250000

while num_month < goal_month:
    return_of_investment = (0.04 * current_savings) / 12
    monthly_salary = annual_salary / 12
    mid = low + high // 2
    percent = mid / 100

    if num_month % 6 == 0 and num_month > 0:
        annual_salary += (semi_annual_raise * annual_salary)
        current_savings += return_of_investment + (monthly_salary * percent)
    else:
        current_savings += return_of_investment + (monthly_salary * percent)

    print(current_savings)
    num_tries += 1
    num_month += 1

    if num_month > 36:
        high = mid - 1
        continue
    elif num_month < 36:
        low = mid + 1
        continue
    elif num_month == 36 and current_savings >= down_payment and percent < 100:
        print(f"{percent}% should be saved.")
        print(num_tries)
        break
    else:
        print("You can't save enough for down payment")
    

