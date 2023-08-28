#This is code for solving quadratic equations

print("Quadratic equations are in the form ax^2+bx+c = 0")
print("Please enter a, b and c with respect to your equation")
def quadratic():
    
    while True:
        try:
            a = float(input("Enter a: "))

            if a.is_integer() or not float.is_integer(a):
                break
            else:
                print("Please enter an integer or a float.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            b = float(input("Enter b: "))

            if b.is_integer() or not float.is_integer(b):
                break
            else:
                print("Please enter an integer or a float.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            c = float(input("Enter c: "))

            if c.is_integer() or not float.is_integer(c):
                break
            else:
                print("Please enter an integer or a float.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    root = ((b ** 2) - (4* a* c))
    square_root = ((b ** 2) - (4 * a * c)) ** 0.5
    if root < 1:
        print("It's a complex root please try again")
        quadratic()
    else:
        x1 = (((-b) + square_root) / (2 * a))
        x2 = (((-b) - square_root) / (2 * a))
        return x1, x2

answer = quadratic()

print(f"The answers to the quadratic equation is {answer}")

