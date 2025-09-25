# -----------------------------
# Bank Queue System with User Input
# -----------------------------

customers = {}     # stores customer_id -> customer_name
next_id = 1        # keeps track of the next ID to assign

def add_customer(name):
    """Add a new customer to the queue with a unique ID."""
    global next_id
    customers[next_id] = name
    print(f"Welcome {name}! Your queue number is {next_id}.")
    next_id += 1

def get_customer_by_id(customer_id):
    """Retrieve customer name by their ID."""
    return customers.get(customer_id, f"No customer found with ID {customer_id}.")

def serve_next_customer():
    """Serve (remove) the first customer in the queue."""
    if not customers:
        print("No customers in the queue.")
        return None
    first_id = min(customers.keys())
    name = customers.pop(first_id)
    print(f"Now serving Customer #{first_id}: {name}")
    return (first_id, name)

def display_queue():
    """Show all customers currently waiting in order of arrival."""
    if not customers:
        print("The queue is empty.")
    else:
        print("\n--- Current Queue ---")
        for cid, name in sorted(customers.items()):
            print(f"#{cid}: {name}")
        print("---------------------")


# -----------------------------
# Main program loop (user input)
# -----------------------------

while True:
    print("\nBank Queue System")
    print("1. Add new customer")
    print("2. Serve next customer")
    print("3. Lookup customer by ID")
    print("4. Display queue")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter customer name: ")
        add_customer(name)

    elif choice == "2":
        serve_next_customer()

    elif choice == "3":
        try:
            cid = int(input("Enter customer ID: "))
            print(get_customer_by_id(cid))
        except ValueError:
            print("Please enter a valid number for ID.")

    elif choice == "4":
        display_queue()

    elif choice == "5":
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid option, please choose 1-5.")
