#This is code for solving quadratic equations

print("Quadratic equations are in the form ax^2+bx+c = 0")
print("Please enter a, b and c with respect to your equation")
def quadratic():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
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

