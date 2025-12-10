contact_book = {}

num_add_con = int(input("How many contacts would you like to add? "))
for x in range(num_add_con):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contact_book[name] = phone
    print("---------------")
print("Current Contacts:")
for name, phone in contact_book.items():
    print(f"{name}: {phone}")

action = input(
    "would you like to add or remove a contact? if add type add, if remove type remove or type quit to exit: ")

if action.lower == "quit" or action.lower == "exit":
    print("THANK YOU FOR USING CONTACT BOOK APP")

while action.lower == "add" or action.lower == "remove":
    if action.lower == "add":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contact_book[name] = phone
        print("Contact added!")
        break
    elif action.lower == "remove":
        name = input("Enter the name of the contact to remove: ")
        if name in contact_book:
            del contact_book[name]
            print("Contact removed!")
            break
        else:
            print("Contact not found.")
            action = input(
                "try again, would you like to add or remove a contact? ")
    else:
        print("invalid action. please type add or remove.")
        action = input("would you like to add or remove a contact? ")
