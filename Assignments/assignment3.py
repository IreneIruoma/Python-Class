"""
This is a program that determines whether a number is an odd or even number

"""

number = float(input("Enter your number; "))
num2 = 2
modulo = number % num2

if modulo == 0:
    print("This is an even number.")
elif modulo == 1:
    print("This is an odd number.")
else:
    print("Please enter a valid integer!")
