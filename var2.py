# I'm cuurently doing my industrial

me = "I'm"
verb = "currently doing"
activity = "industrial training"
place = "Aptech"

print(me, verb, "my", activity, "at", place)

name = "Irene"  #global variable
def greet():
    # age = 22
    # print(f"hello my name is {name}")
    # print(f"I am {age} years old")
    name = "Oge"
    print(name)
greet()
name = "a" #global variable
def greet():
   name = "b"  #local variable
   print("this is for local" +name)
greet()

print("this is for global" +name)