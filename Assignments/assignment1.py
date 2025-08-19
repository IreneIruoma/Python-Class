
"""
this is asimple calculator program that adds, subtracts,
multuplies and divides

num1 = 10
num2 = 26

"""

num1 = int(input("Enter the first number; "))
num2 = int(input("Enter the second number; "))
operation = input(f"what mathematical operation do yo you want to perform? (addition, subtraction, multiplication,division): ")

# sum = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2

if operation.lower() == "addition":
    print(f"This is the sum of the two numbers; {num1 + num2}")
elif operation.lower() == "subtraction":
    print(f"This is the difference of the two numbers; {num1 - num2}")
elif operation.lower() == "multiplication":
   print(f"This is the product of the two numbers; {num1 * num2}")
elif operation.lower() == "division":
  if (num2 == 0):
     print("undefined")
  else:
      print(f"This is the quotient of the two numbers; {num1 / num2}")
else:
   print("Please enter one of the above mathematical operations")







