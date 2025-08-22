"""
this is a program that keeps running until the user enters an age above 18
"""



age = 0  
while age <= 18:
    age = int(input("Enter your age; "))
    if age < 0:
        print("You are not even born yet!!")
    elif age < 18:
        print(f"You're not of age yet,you have {19 - age} more years to go")
    elif age == 18:
        print("sorry, few more months to go!")

print("I bet it feels good to be an adult!!")