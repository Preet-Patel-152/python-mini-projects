contact_book = {}

num_add_con = int(input("How many contacts would you like to add? "))
for x in range(num_add_con):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contact_book[name.strip()] = phone.strip()
    print("---------------")
print("Current Contacts:")
for name, phone in contact_book.items():
    print(f"{name}: {phone}")

action = input(
    "would you like to add or remove a contact? if add type add, if remove type remove or type quit to exit: ")

if action.strip().lower() == "quit" or action.strip().lower() == "exit":
    print("THANK YOU FOR USING CONTACT BOOK APP")

while action.strip().lower() == "add" or action.strip().lower() == "remove":
    if action.lower() == "add":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contact_book[name.strip()] = phone.strip()
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
    if search_action.lower().strip() == "search":
        search_name = input("Enter the name of the contact to search: ")
        if search_name.strip in contact_book:
            print(
                f"Contact found: {search_name}: {contact_book[search_name]}")
        else:
            print("Contact not found.")
    else:
        print("Continuing without search.")
    print("Current Contacts:")
    for name, phone in contact_book.items():
        print(f"{name}: {phone}")


# when you have the chance what needs to be done is rewirte this code,
# use functuons to help with the addinf and removing
#  ake a while loop for the code to be runnig till user puts in q to break out the while loop
# if and elif statments to check what the user wants to do, and use functions to do the adding removing and searching
# contacts main functions to have is to add pass number of contacts they want to add,
#   remove number of contacts they want to and same with saerch
# this will make the code more orgainized and easier to read
