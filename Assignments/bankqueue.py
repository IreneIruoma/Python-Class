"""
this is a program that grants users an id in the bank and prints out their name
when they are called on
"""

customers = {}
nextid = 1    # keeps track of the next ID to assign

def addcustomer(name):
    global nextid
    customers[nextid] = name
    print(f"Customer added: {name} (ID {nextid})")
    nextid += 1

def getcustomerbyid(customerid):
    return customers.get(customerid, f"No customer found with ID {customerid}.")

def servenextcustomer():
    if not customers:
        print("No customers in the queue.")
        return None
    firstid = min(customers.keys())  # find the earliest ID (smallest number)
    name = customers.pop(firstid)    # remove and return them
    print(f"Serving Customer #{firstid}: {name}")
    return (firstid, name)

def display_queue():
    if not customers:
        print("The queue is empty.")
    else:
        print("\n Current Queue ")
        for cid, name in sorted(customers.items()):
            print(f"#{cid}: {name}")

addcustomer("Irene")
addcustomer("Stacy")
addcustomer("Ebube")

display_queue()

print(getcustomerbyid(2))  
print(getcustomerbyid(5))   

servenextcustomer()   # serve Irene
servenextcustomer()   # serve Stacy

display_queue()
