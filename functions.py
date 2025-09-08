# def greetings():
#     print("welcome to the application")
# greetings()

# # def add():
# #     num1 = int(input("enter the first number; "))
# #     num2 = int(input("enter the first number; "))
# #     print(num1 + num2)
# # add()

# # myname = input("enter your name; ")
# # def greet(name):
# #     print(f"hello {name}")

# # greet(myname)


# # num1 = int(input("enter the first number; "))
# # num2 = int(input("enter the first number; "))
# def add(a,b):
#     print(a + b)
# add("big ", "girl")


# #read up on modulation, arguements and parameters,args


# # function to add two numbers
# def add2 (num1, num2):
#     sum = num1 + num2
#     print(f"this is the sum: {sum}")

# add2(10, 5)

# # passing a list as an arguement
# bakerylist = ["bread", "cake", "cookies", "donuts", "muffins", "strawberry cake"]
# # function to check through my list for strwberry cake
# def checkstock(pastry):
#     counter = 0
#     for item in pastry:
#         if item !="strawberry cake":
#             counter += 1
#             print(counter, " loop")
#             continue
#         else:
#             print("yes, we are in stock")
# checkstock(bakerylist)


# classList = ["nenye", "actress", "despina", "kamsy", "somto", "sanctus", " chisom", "irene", "pascal", "jude", "daniel", "chiemerie", "kosi" ]
# def classattendance(attendance):
#     for item in attendance:
#         if item != "irene":
#             continue
#         else:
#             print("Yes, I'm in class")
# classattendance(classList)

# # return is used give an output
# # the continue statement jumps a line and starts fro
# # the slash / signifies positioning

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)