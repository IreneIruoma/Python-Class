# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()

# A CLASS is like a blueprint
class Human:
    # The __init__ method is the CONSTRUCTOR
    # It runs automatically when you create a new object
    def __init__(self, eyes, hair_color, legs, gender, height):
        # These are PROPERTIES (attributes) of the object
        self.eyes = eyes
        self.hair_color = hair_color
        self.legs = legs
        self.gender = gender
        self.height = height
    
    # These are METHODS (functions inside a class)
    def walking(self):
        print("I am walking...")

    def speaking(self):
        print("I am speaking...")

    def breathing(self):
        print("I am breathing...")

# -----------------------------
# Creating OBJECTS from the class
# -----------------------------

# person1 is an object of class Human
person1 = Human(2, "black", 2, "female", "5.6ft")

# person2 is another object, with different property values
person2 = Human(2, "brown", 2, "male", "6ft")

# -----------------------------
# Accessing PROPERTIES
# -----------------------------
print("Person 1 has", person1.eyes, "eyes and", person1.hair_color, "hair.")
print("Person 2 is", person2.height, "tall and is", person2.gender)

# -----------------------------
# Calling METHODS (actions)
# -----------------------------
person1.walking()   # Output: I am walking...
person2.speaking()  # Output: I am speaking...
person1.breathing() # Output: I am breathing...

# -----------------------------
# Showing DIFFERENCE between __init__ and normal methods
# -----------------------------

# __init__ ran AUTOMATICALLY when person1 and person2 were created.
# Normal methods (walking, speaking, breathing) only run WHEN CALLED.
class Car:
    # Constructor (__init__) = factory setup for each car
    def __init__(self, color, brand, speed, doors):
        # Properties = what the car HAS
        self.color = color
        self.brand = brand
        self.speed = speed
        self.doors = doors

    # Methods = what the car DOES
    def drive(self):
        print(f"The {self.color} {self.brand} is driving at {self.speed} km/h.")

    def brake(self):
        print(f"The {self.brand} is slowing down and stopping.")

    def honk(self):
        print(f"The {self.brand} goes 'Beep Beep!'")

# -----------------------------
# Creating OBJECTS (real cars)
# -----------------------------
car1 = Car("red", "Toyota", 120, 4)
car2 = Car("blue", "BMW", 180, 2)

# -----------------------------
# Accessing PROPERTIES
# -----------------------------
print("Car 1 is a", car1.color, car1.brand, "with", car1.doors, "doors.")
print("Car 2 is a", car2.color, car2.brand, "with", car2.doors, "doors.")

# -----------------------------
# Using METHODS (behaviors)
# -----------------------------
car1.drive()
car2.honk()
car1.brake()


# Use self. when you want the property to stay with the object.
# Without self., it’s just a temporary local variable inside the method.

# __init__ → sets up the object when it’s created (initialization).
# __str__ → gives a readable description of the object when printed.

# 1. What is __str__?
# It’s a special method (like __init__) in Python.
# It defines what gets returned when you print an object.
# Without it, printing an object just shows something like <__main__.Car object at 0x0001> (which is not helpful).

# Why use __str__?

# Think of it as giving your object a nice human-readable description.
# Just like people have an ID card description (Name, Age, Gender),
# __str__ gives your object a description when you print it.

# Structure
# def __str__(self):
#     return "Some string that describes the object"

# It must return a string.
# It runs automatically when you call print(object).

class Car:
    def __init__(self, color, brand, speed):
        self.color = color
        self.brand = brand
        self.speed = speed

    def __str__(self):
        return f"{self.color} {self.brand} running at {self.speed} km/h"

# Creating objects
car1 = Car("red", "Toyota", 120)
car2 = Car("blue", "BMW", 180)

# Printing objects
print(car1)   # Output: red Toyota running at 120 km/h
print(car2)   # Output: blue BMW running at 180 km/h

# 5. Key Difference
# __init__ → sets up the object when created.
# __str__ → gives the object a nice string representation when printed.

# ✅ Analogy:
# __init__ = filling in your birth certificate (basic details).
# __str__ = writing your bio/intro (how others see you when they “print” you).

#instance methods:this works on the object of a class, example
class Car:
    def __init__(self, color):
        self.color = color

    def drive(self):   # instance method
        print(f"The {self.color} car is driving.")

car1 = Car("red")
car1.drive()   # ✅ Works (self refers to car1)


# class methods: they act on class itself not on the object
# Instead of self, they use cls (which refers to the class).
# You mark them with @classmethod.
class Car:
    wheels = 4   # class property (shared by all cars)

    @classmethod
    def describe_class(cls):
        print(f"All cars have {cls.wheels} wheels.")

Car.describe_class()   # All cars have 4 wheels


# Static Methods
# They don’t need self or cls.
# They are just functions that live inside a class for organization.
# You mark them with @staticmethod.
class Car:
    @staticmethod
    def car_horn():
        print("Beep beep!")

Car.car_horn()    # ✅ Beep beep!


# all metthod types
class Car:
    # Class variable (shared by all cars)
    wheels = 4

    # 1️⃣ Instance Method
    def __init__(self, color, brand):
        self.color = color     # belongs to this car only
        self.brand = brand     # belongs to this car only

    def drive(self):   # instance method
        print(f"The {self.color} {self.brand} is driving!")

    # 2️⃣ Class Method
    @classmethod
    def car_facts(cls):
        print(f"All cars have {cls.wheels} wheels.")

    # 3️⃣ Static Method
    @staticmethod
    def traffic_rule():
        print("Traffic Rule: Always wear your seatbelt.")
# Create objects
car1 = Car("red", "Toyota")
car2 = Car("blue", "BMW")

# Instance Method → works on individual objects
car1.drive()   # The red Toyota is driving!
car2.drive()   # The blue BMW is driving!

# Class Method → works on the class itself
Car.car_facts()   # All cars have 4 wheels

# Static Method → general helper, not tied to object/class
Car.traffic_rule()  # Traffic Rule: Always wear your seatbelt.

