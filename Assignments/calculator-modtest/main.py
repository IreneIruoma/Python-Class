import inputmodule
import logicmodule
# print(logicmodule.__file__)

def main():
    while True:
        num1, num2 = inputmodule.getnumbers()
        op = inputmodule.getoperation()
        logicmodule.checkop(op, num1, num2)

        another_operation = input("Do you want to perform another operation? (Yes/No): ").lower()
        if another_operation == "yes":
          continue
        elif another_operation == "no":
            break
        else:
            print("Please input either yes or no!")

if __name__ == "__main__":
    main()
