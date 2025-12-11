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

if action.lower() == "quit" or action.lower() == "exit":
    print("THANK YOU FOR USING CONTACT BOOK APP")

while action.lower() == "add" or action.lower() == "remove":
    if action.lower() == "add":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contact_book[name] = phone
        print("Contact added!")
        action = input(
            "would you like to add or remove a contact?, if would like to quit type quit: ")

    elif action.lower() == "remove":
        name = input("Enter the name of the contact to remove: ")
        if name in contact_book:
            del contact_book[name]
            print("Contact removed!")
            action = input(
                "would you like to add or remove a contact?, if would like to quit type quit: ")

        else:
            print("Contact not found.")
            action = input(
                "try again, would you like to add or remove a contact? ")

    elif action.lower() == "quit" or action.lower() == "exit":
        print("THANK YOU FOR USING CONTACT BOOK APP")
        break

    print("would you like  to saerch for a contact?")
    search_action = input(
        "if yes type search, if no type no to continue: ")
    if search_action.lower() == "search":
        search_name = input("Enter the name of the contact to search: ")
        if search_name in contact_book:
            print(
                f"Contact found: {search_name}: {contact_book[search_name]}")
        else:
            print("Contact not found.")
    else:
        print("Continuing without search.")
    print("Current Contacts:")
    for name, phone in contact_book.items():
        print(f"{name}: {phone}")
