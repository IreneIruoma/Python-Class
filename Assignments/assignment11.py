"""
this is a program that continues running until the user enters 'n'
"""

while True:  
    Answer = input("Do you want to continue? (y/n): ")  
    if Answer == "y":  
        print("Fine, let's continue")  

    elif Answer == "n":  
        print("You've come to the end of the program, Thank you!!")  
        break  

    else:  
        print("Please input any of the above options")