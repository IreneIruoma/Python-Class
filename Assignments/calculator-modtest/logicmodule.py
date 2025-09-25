import functionmodule as fm

def checkop(operation, num1, num2):
    if operation == "addition":
        result = fm.addition(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")

    elif operation == "subtraction":
        result = fm.difference(num1, num2)
        print(f"The difference of {num1} and {num2} is {result}")

    elif operation == "multiplication":
        result = fm.product(num1, num2)
        print(f"The product of {num1} and {num2} is {result}")

    elif operation == "division":
        result = fm.quotient(num1, num2)
        print(f"The quotient of {num1} and {num2} is {result}")

    else:
        print("Invalid operation selected.")
