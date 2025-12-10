# this mini project is a grocery list manager, you can add and remove
# items from your grocery list, and see what your grocery list looks like


print("welcome to grocery list manager")
input_list = input(
    "please enter your grocery items separated by commas, ex(apple, bannana, orange): ")
grocery_list = input_list.split(", ")

print("your current grocery list is: ")
print(grocery_list)

print("whould you like to add or remave items from your grocery list?")
action = input("type add to add items, type remove to remove items: ")

while 0 == 0:

    if action == "add":
        item_to_add = input("enter the item you whould like to add: ")
        grocery_list.append(item_to_add)
        print("item added!")
    elif action == "remove":
        item_to_remave = input("enter the item you whould like to remove: ")
        if item_to_remave in grocery_list:
            grocery_list.remove(item_to_remave)
            print("item removed!")
        else:
            print("item not found in grocery list.")
    else:
        print("invalid action. please type add or remove.")

    print("your current grocery list is: ")
    print(grocery_list)

    continue_action = input(
        "whould you like to add or remove more items? type yes to continue, no to quit: ")
    if continue_action.lower() != "yes":
        grocery_list.clear()
        print("THANK YOU FOR USING GROCERY LIST MANAGER")
        break
    action = input("type add to add items, type remove to remove items: ")
