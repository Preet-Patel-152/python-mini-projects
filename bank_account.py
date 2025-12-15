from account import bank

bank1 = bank({"Alice": "123456"}, 1000)

is_running = True

while is_running:

    action = input("would you like to create a new account or access existing account?"
                   " type new for new account or exi for existing account: ")

    if action.strip().lower() == "new":
        name = input("Enter account holder name: ")
        password = input("Enter account password: ")

        bank_acc = bank({name: password}, 0)
        print("Account created successfully!")
        continue

    elif action.strip().lower() == "exi":
        name = input("Enter account holder name: ")
        password = input("Enter account password: ")

        if name in bank1.account_holder and bank1.account_holder[name] == password:
            print("Access granted.")
            bank_acc = bank1

            while True:

                print(
                    "Available actions: deposit, withdraw, check balance, change password, exit")

                user_action = input("Enter action: ").strip().lower()
                match user_action:
                    case "deposit":
                        amount = float(input("Enter amount to deposit: "))
                        print(bank_acc.deposit(amount))

                    case "withdraw":
                        amount = float(input("Enter amount to withdraw: "))
                        print(bank_acc.withdraw(amount))

                    case "check balance":
                        print(bank_acc.check_balance())

                    case "change password":
                        new_password = input("Enter new password: ")
                        print(bank_acc.change_acccout_password(new_password))

                    case "exit":
                        print("Exiting account management.")
                        break

                    case _:
                        print("Invalid action. Please try again.")
        else:
            print("Access denied. Incorrect name or password.")
            continue
