"""
this is a program that tracks the grade of students

"""

students = {}  # dictionary to store student data

def addstudent(name):
    """Add a new student with an empty grade list"""
    if name not in students:
        students[name] = []
        print(f"Student '{name}' added.")
    else:
        print(f"Student '{name}' already exists.")

def addgrade(name, grade):
    """Add a grade for an existing student"""
    if name in students:
        students[name].append(grade)
        print(f"Added grade {grade} for {name}.")
    else:
        print(f"Student '{name}' not found. Please add the student first.")

def calculateaverage(name):
    """Calculate average grade for a student"""
    if name in students and students[name]:
        return sum(students[name]) / len(students[name])
    else:
        return None  # no grades yet or student not found

def beststudent():
    """Find the student with the highest average"""
    if not students:
        return None
    best = None
    highestavg = 0
    for name, scores in students.items():
        if scores:  # only calculate if student has scores
            avg = sum(scores) / len(scores)
            if avg > highestavg:
                highestavg = avg
                best = name
    return best, highestavg

def displaystudents():
    """Display all students and their grades"""
    print("\n   Student Grades ")
    print(f"{'Name':<10} {'Grades':<20} {'Average':<10}")
    print("-" * 40)
    for name, scores in students.items():
        avg = calculateaverage(name)
        avg_display = f"{avg:.2f}" if avg is not None else "N/A"
        print(f"{name:<10} {str(scores):<20} {avg_display:<10}")
    print("-" * 40)


addstudent("Irene")
addgrade("Irene", 90)
addgrade("Irene", 80)
students["Irene"].append(65)

addstudent("Ebube")
addgrade("Ebube", 70)
addgrade("Ebube", 85)

addstudent("Stacy")
addgrade("Stacy", 100)
addgrade("Stacy", 95)

displaystudents()
print("best Student:", beststudent())
