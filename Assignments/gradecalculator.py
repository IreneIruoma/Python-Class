"""
this is a program that gets the user input(score) and assigns a grade to them while providing
encouraging messages along with the grade
"""

def gradecalculator(score):
    # statement to validate the score
    if score < 0 or score > 100:
        return "Invalid score! Please enter a score betweeen 0-100"
    # statement to  assign grades
    if score >= 90:
        return "Grade A \nYou did an excellent job."
    elif score >= 80:
        return "Grade B \nGood job!!"
    elif score >= 70:
        return "Grade C \nNice job, there's always room for improvement"
    elif score >= 60:
        return "Grade D \nYou passed, but you can always do better"
    else:
        return "Grade F \nIt's not the end of the world, you can always try again"
    
 
while True:
    while True:
        try:
            userscore = float(input("Please enter your score: "))
            result = gradecalculator(userscore)
            print(result)
            if 0 <= userscore <= 100:
                break
        except ValueError:
            print("Please enter a valid number")
    while True:
        another_operation = input("Do you want to perform another operation? (Yes/No): ").lower()
        if another_operation == "yes":
            break
        elif another_operation == "no":
            exit()
        else:
            print("Please input either yes or no!")