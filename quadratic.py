#This is code for solving quadratic equations

print("Quadratic equations are in the form ax^2+bx+c = 0")
print("Please enter a, b and c with respect to your equation")
def quadratic():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    roots = ((b ** 2) - (4* a* c)) ** 0.5
    x1 = (((-b) + roots) / (2 * a))
    x2 = (((-b) - roots) / (2 * a))
    return x1, x2

answer = quadratic()

print(f"The answers to the quadratic equation is {answer}")

