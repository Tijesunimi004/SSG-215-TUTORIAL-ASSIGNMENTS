import cmath
from time import sleep

print("Enter your first complex number below")

sleep(1)

a = float(input("Enter the real part of the first complex number: "))
b = float(input("Enter the imaginary part of the first complex number: "))

print("Enter your second complex number below")
x = float(input("Enter the real part of the second complex number: "))
y = float(input("Enter the imaginary part of the second complex number: "))

z1 = complex(a,b)
z2 = complex(x,y)

result_sum = z1 + z2
result_sub = z1 - z2
result_mul = z1 * z2
result_div = z1 / z2


print(f"The sum of the complex numbers = {result_sum}")
print(f"Subtraction of the two complex numbers = {result_sub}")
print(f"The multiplication of the two complex numbers = {result_mul}")
print(f"The division of the two complex numbers = {result_div}")
