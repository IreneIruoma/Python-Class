x = 1    # int
y = 2.8  # float
z = 1j  
print(type(x))
print(x)

# converting int to float
x = float(x)
print(type(x))
print(x)

print(type(y))
print(y)

# converting float to int
y = int(y)
print(type(y))
print(y)

# random numbers
import random
start = 1
end = 19
random_number = random.randrange(start, end)
print(random_number)

# escape characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)



firstname = "irene"
middlename = "iruoma"
print(firstname+ " " +middlename)
# to put everything in uppercase
print(firstname.upper()+ " "+middlename.upper())
