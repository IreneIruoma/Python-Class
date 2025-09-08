"""
this is a program that checks whether a password is strong
"""

while True:
    password = input("Enter a password: ")
    uppercasecount = 0
    lowercasecount = 0
    numbercount = 0

    for character in password:
        if character.isupper():
            uppercasecount += 1
        elif character.islower():
            lowercasecount += 1
        elif character.isdigit():
            numbercount += 1

    if len(password) >= 8 and uppercasecount > 0 and lowercasecount > 0 and numbercount > 0:
        print("Strong password!")
        print(f"The uppercase letters are {uppercasecount} in number")
        print(f"The lowercase letters are {lowercasecount} in number")
        print(f"The numbers are {numbercount} in number")
        break
    else:
        print("Weak password! Your password should contain at least 8 characters, including uppercase, lowercase and numbers")
