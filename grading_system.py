while True:
    grade = input("Enter your scroe to know your grade: ")
    if grade.isdigit():
        grade = int(grade)
        if grade > 100 or grade < 0:
            print("This grade is not within range. ")
            continue
        elif grade <= 100:
            break
    else:
        print("This is not a number")
        continue
#a. Below 25 - F
#b. 25 to 45 - E
#c. 45 to 50 - D
#d. 50 to 60 - C
#e. 60 to 80 - B
#f. Above 80 - A

if grade >= 80:
    print("You got an A")
elif grade >= 60 and grade <= 80:
    print("You got a B")
elif grade >= 50 and grade <= 60:
    print("You got a C")
elif grade >= 45 and grade <= 50:
    print("You go a D")
elif grade >= 25 and grade <= 45:
    print("You got an E")
else:
    print("You got an F")
