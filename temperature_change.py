# Celsius (°C) * 9/5) + 32
def celsius_conv():
    fah = (temp * 9/5) + 32
    print(f"Your conversion from celsius to fahrenheit is {fah}")

# Fahrenheit (°F) - 32) * 5/9.
def fahrenheit_conv():
    cel = (temp - 32) * 5/9
    print(f"Your conversion from fahrenheit to celsius is {cel}")


print("Welcome to the Temperature Converter")
print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celcius\n")
user_input = input("Please pick what you want to do by entering 1 or 2: ")

if user_input == str(1):
    temp = float(input("Enter the Temperature to be converted: "))
    celsius_conv()
else:
    temp = float(input("Enter the Temperature to be converted: "))
    fahrenheit_conv()


