import random


char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
accounts = {"preet": "kamini152"}


def generate_password(length):
    password = ''
    for i in range(length):
        password += random.choice(char)
    return password


while True:
    action = input(
        "would you like to sign up or login? type signup or login: ")

    if action.lower() == "signup":
        username = input("Enter a username: ")

        if username in accounts:
            print("Username already exists. Please try a different one.")
        else:
            while True:
                action_b = input(
                    "would you like to make ur own password or use to genrate one? type own or generate: ")
                if action_b.lower() == "own":
                    password = input("Enter a password: ")
                    accounts[username] = password
                    break
                elif action_b.lower() == "generate":
                    length = int(input("Enter desired password length: "))
                    password = generate_password(length)
                    accounts[username] = password
                    print("Generated password:", password)
                    break
                else:
                    print("Invalid option. Please type own or generate.")

        print("Signup successful! You can now login.")
        print("-----------------------------------")
        print("-----------------------------------")
        print("you have signed in to the password generator app and this is the secret message: ")
        print("The secret code is 42. Keep it safe!")
        print("-----------------------------------")
        print("-----------------------------------")
        break

    elif action.lower() == "login":
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in accounts and accounts[username] == password:
            print("Login successful! Welcome,", username)

            print("-----------------------------------")
            print("-----------------------------------")
            print(
                "you have signed in to the password generator app and this is the secret message: ")
            print("The secret code is 42. Keep it safe!")
            print("-----------------------------------")
            print("-----------------------------------")
            break
        else:
            print("Invalid username or password. Please try again.")

    else:
        print("Invalid action. Please type signup or login.")


# now
