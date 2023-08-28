def decimal_to_octal(decimal_number):
    if decimal_number < 8:
        return str(decimal_number)
    else:
        quotient = decimal_number // 8
        remainder = decimal_number % 8
        return decimal_to_octal(quotient) + str(remainder)


decimal_number = int(input("Enter the decimal to be converted: "))
octal_number = decimal_to_octal(decimal_number)
print("Octal equivalent:", octal_number)
