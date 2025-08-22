"""
this is a program that runs until a user enters a negative number
"""

number = 0  
while number >= 0:
    number = int(input("Enter your number; "))
    if number >= 0:
        print(f"You entered {number}")

print("You've come to the end of your program!")