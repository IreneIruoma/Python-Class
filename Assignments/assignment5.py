"""
This is a program that checks the greater number between two numbers
"""

num1 = float(input("please enter your first number; "))
num2 = float(input("please enter your second number; "))

if num1 > num2:
    print(f"The first number({num1}) is the greater number")
elif num2 > num1:
    print(f"The second number({num2}) is the greater number")
else:
    print("They are equal to each other")