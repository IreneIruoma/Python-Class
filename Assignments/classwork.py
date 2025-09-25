names = {}

def addnames(name):
    if name not in names:
        names[name] = []
        print(f"Student '{name}' added.")
    else:
        print(f"Student '{name}' already exists.")
#wite a code to manage a bank queue system, users are required to input their names an d they are given a serial noh
t