"""
while loop
"""

start = 1
end = 10
while(start < end):
    print(start)
    start = start + 1
    # start += 1


start = 13
end = 36
while(start < end):
    print(start)
    start = start + 1

# for loop
mylist = ["basketall", "football", "tennis", "golf"]
counter = 0
for item in mylist:
    print(item)
    if item == "golf":
        print("yes, this is golf")
        print(counter)
        break
    else:
        counter += 1
        continue

num1 = int(input("enter a number: "))
multiplier = 1
while (multiplier <= 12):
    print(num1*multiplier)
    multiplier += 1

name = "Irene"
for characters in name:
    print(characters)
# range
for num in range(1, 10):
  print(num)
else:
    print("the loop is over")

# IDE - integrated development environment
# read up on virtual environment