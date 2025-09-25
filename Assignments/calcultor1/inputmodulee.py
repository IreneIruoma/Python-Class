def getnumbers():
    while True:
        try:
           num1 = float(input("Enter the first number; "))
           num2 = float(input("Enter the second number; "))
           return num1, num2
        except ValueError:
            print("Invald input, Please enter a valid number.")

def getoperation():
    operation = input(f"what mathematical operation do yo you want to perform? (addition, subtraction, multiplication,division): ")
    if operation in ["add", "subtract", "multiply", "divide"]:
        return operation
    else:
        print("Invalid operation. Try again.")