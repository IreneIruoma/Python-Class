"""
Location assignment; this is about directing a user from aptech to either 
Abakpa or Emene, depending on their choice.
"""

name = input("What's your name? ")
location = input("Where are you going to? ")

if location.capitalize() == "Abakpa":
    print(f"Hello {name}, to get to {location} from Aptech, You need to enter keke in front of aptech and stop at holy ghost roundabout.You then look for {location} bus at the busstop and enter, the bus is expected to stop you at {location} junction. ")
elif location.capitalize() == "Emene":
    print(f"Hello {name}, to get to {location} from Aptech, You need to enter keke in front of aptech and stop at holy ghost roundabout.You then look for {location} bus at the busstop and enter, the bus is expected to stop you at {location} junction.")
else:
    print(f"Hello {name}, Your location isn't available now!")