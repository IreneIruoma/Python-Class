"""
this is a number that tries to match a secret number set by me
"""

import random
start = 1
end = 100
secret_number = random.randrange(start, end)
# print(secret_number)
guessno = int(input("Guess a number; "))
while guessno != secret_number:
    if guessno > secret_number:
        guessno = int(input("You went higher than expected, Reduce it! "))
    else:
        guessno = int(input("You went lower than expected, increase it! "))

print("Got it right! Way to go")