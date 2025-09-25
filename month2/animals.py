class dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("woof woof")

animal = dog("sue", "bulldog")


class cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def meow(self):
        print("meow meow")

    def catname(self):
        print(self.name)
    
    def __str__(self):
        return f"this class requires a name and breed\nIrene"

cat1 = cat("diana", "foreign")
# cat1.catname()
# cat1.meow()
# print(animal.name)
print(cat1)
cat1.name = "Paige"
cat1.catname()

class human:
    def __init__(self,name, eyes, nose, ear,skin, tongue, limbs, skincolor, height):
        self.name = name
        self.eyes = eyes
        self.nose = nose
        self.ear = ear
        self.skin = skin
        self.tongue = tongue
        self.limbs = limbs
        self.skincolor = skincolor
        self.height = height

    def walking(self):
        print(f"{self.name} is walking")
    def talking(self):
        print(f"{self.name} is talking")

me = human("Irene", 2, 1, 2, "dry", 1, 4, "dark", 5.6)
me.walking()
me.talking()
