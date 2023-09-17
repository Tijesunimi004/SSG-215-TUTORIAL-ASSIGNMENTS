#Varirable Definitions are in the pdf 
#Below is question 1

current_savings = 0

portion_down_payment = 0.25

portion_saved = input("Enter the percentage you want to save: ")
while True:
    total_cost = input("Enter the cost of your dream house: ")
    if total_cost.isdigit():
        total_cost = int(total_cost)
        break
    else:
        print("Please enter a nummber.")
        continue

