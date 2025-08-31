"""
this is a program for counting down to 1 so as to detonate a bomb
"""

import time

start = 10
while start >= 0:
    print(start)
    time.sleep(2)
    start -= 1

print("POOF!!")