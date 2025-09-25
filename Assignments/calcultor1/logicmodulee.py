from inputmodulee import getnumbers, getoperation
import functionmodulee as fmod

def logicop():
    num1, num2 = getnumbers()
    operation = getoperation()

    if operation == "add":
        result = fmod.addition(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")

    elif operation == "subtract":
        result = fmod.difference(num1, num2)
        print(f"The difference of {num1} and {num2} is {result}")

    elif operation == "multiply":
        result = fmod.product(num1, num2)
        print(f"The product of {num1} and {num2} is {result}")

    elif operation == "divide":
        result = fmod.quotient(num1, num2)
        print(f"The quotient of {num1} and {num2} is {result}")

    else:
        print("Invalid operation selected.")
