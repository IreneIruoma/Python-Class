def getnumbers():
    while True:
        try:
            num1 = float(input("Enter the first number; "))
            num2 = float(input("Enter the second number; "))
            return num1, num2
        except ValueError:
            print("Invald input, Please enter a valid number.")


def getoperation():
    op = input("Enter operation (add, subtract, multiply, divide): ").lower().strip()
    return op
