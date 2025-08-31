choice = input("Do you want to continue? (y/n): ")
while (choice == "y"):
    print("Fine, let's continue")
    choice = input("Do you want to continue? (y/n): ")
    if (choice == "y"):
        continue
    elif (choice == "n"):
        break
    else:  
        print("Please input any of the above options")
