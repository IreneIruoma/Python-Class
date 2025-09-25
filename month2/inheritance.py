class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)



me = Person("Irene", "Iruoma")
me.printname()

class Student(Person):
  def printlastname(self):
    print(self.lastname)

mee = Student("Irene", "Iruoma")
mee.printname()
mee.printlastname(o0iu8)