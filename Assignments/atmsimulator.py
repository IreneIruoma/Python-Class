"""
this is a program that checks, deposits and withdraws money
"""

def checkbalance(balance):
    print(f"Your current balance is ${balance}")

def deposit(balance):
    while True:
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
              balance += amount
              print(f"You deposited ${amount}. \nNew balance is ${balance}")
              break
            else:
              print("You are required to deposit an amount greater than $0")
        except ValueError:
           print("Invalid input. Please enter a valid amount")
    return balance
           
def withdraw(balance):
    while True:
       try:
          amount = float(input("Enter amount to withdraw: "))
          if amount > 0:
            if amount <= balance:
               balance -= amount
               print(f"You withdrew ${amount}. \nNew balance is ${balance}")
               break
            else:
               print("Insufficient balance!")
          else:
             print("Invalid withdrawal amount")
       except ValueError:
           print("Invalid input. Please enter a valid amount")
    return balance


balance = 1000
print("welcome to our ATM services")
while True:
    print("Our operations include: \n1. check balance \n2. deposit money \n3. withdraw money")
    while True:
         operation = input("What operation would you like to perform? ").lower()
         if operation == "check":
            checkbalance(balance)
            break
         elif operation == "deposit":
            balance = deposit(balance)
            break
         elif operation == "withdraw":
            balance = withdraw(balance)
            break
         else:
            print("Invalid operation. Please try again.")
    while True:
         another_operation = input("Do you want to perform another operation? (Yes/No): ").lower()
         if another_operation == "yes":
          break
         elif another_operation == "no":
            exit()
         else:
            print("Please input either yes or no!")
