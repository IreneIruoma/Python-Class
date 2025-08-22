"""
This is a program that will print numbers 1-30 
while replacing numbers divisible by 3 and 5 with fizz and buzz respectively
"""

# start = 1
# end = 30
# while(start < end):
#     print(start)
#     if start % 3 == 0 and start % 5 == 0:
#         print(f"{start}(Fizzbuzz)")
#     elif start % 3 == 0:
#         print(f"{start}(Fizz)")
#     elif start % 5 == 0:
#         print(f"{start}(buzz)")
    
     
#     start = start + 1

number = 1
while number <= 30:
    result = f"{number}"
    if number % 3 == 0:
        result += "(Fizz)"
    if number % 5 == 0:
        result += "(Buzz"

    print(result)
    number += 1