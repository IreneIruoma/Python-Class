
"""
this is a simple calculator program that adds, subtracts,
multuplies and divides

num1 = 10
num2 = 26

"""

def addition():
   sum = num1 + num2
   print(f"this is the sum of two numbers: {sum}")

def difference():
   subtraction = num1 - num2
   print(f"this is the difference of two numbers: {subtraction}")

def product():
   multiplication = num1 * num2
   print(f"this is the product of two numbers: {multiplication}")

def quotient():
   if (num2 == 0):
     print("undefined")
   else:
      division = num1 / num2
      print(f"this is the quotient of two numbers: {division}")



while True:
      while True:
         try:
           num1 = float(input("Enter the first number; "))
           num2 = float(input("Enter the second number; "))
           break
         except ValueError:
             print("Invald input, Please enter a valid number.")
      while True:
         operation = input(f"what mathematical operation do yo you want to perform? (addition, subtraction, multiplication,division): ")
         if operation.lower() == "addition":
            addition()
            break
         elif operation.lower() == "subtraction":
            difference()
            break
         elif operation.lower() == "multiplication":
            product()
            break
         elif operation.lower() == "division":
            quotient()
            break
         else:
            print("Please enter one of the above mathematical operations")
      while True:
         another_operation = input("Do you want to perform another operation? (Yes/No): ").lower()
         if another_operation == "yes":
          break
         elif another_operation == "no":
            exit()
         else:
            print("Please input either yes or no!")

