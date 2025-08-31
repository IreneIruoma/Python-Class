"""
this is asimple calculator program that adds, subtracts,
multuplies and divides

num1 = 10
num2 = 26

"""

# num1 = int(input("Enter the first number; "))
# num2 = int(input("Enter the second number; "))

# print(f"This is the sum of the two numbers; {num1 + num2}")
# print(f"This is the difference of the two numbers; {num1 - num2}")
# print(f"This is the product of the two numbers; {num1 * num2}")
# print(f"This is the quotient of the two numbers; {num1 / num2}")


def sum():
    num1 = int(input("Enter the first number; "))
    num2 = int(input("Enter the second number; "))
    print(num1 + num2)
sum()

def difference():
    num1 = int(input("Enter the first number; "))
    num2 = int(input("Enter the second number; "))
    print(num1 - num2)
difference()

def product():
    num1 = int(input("Enter the first number; "))
    num2 = int(input("Enter the second number; "))
    print(num1 * num2)
product()

def quotient():
    num1 = int(input("Enter the first number; "))
    num2 = int(input("Enter the second number; "))
    print(num1 / num2)
quotient()