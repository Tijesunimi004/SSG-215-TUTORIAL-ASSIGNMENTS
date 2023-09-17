num_years = int(input("For how many years have you been working for this company: "))

if num_years > 5:
    salary = float(input("How much is your current salary: "))
    bonus = salary * (5/100)
    new_salary = bonus + salary
    print(f"Your new salary is {new_salary}")
else:
    print("You're not eligible for a bonus")

