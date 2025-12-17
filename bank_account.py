from account import bank

accounts = {}
accounts["Alice"] = bank("Alice", "password123", 1000)


is_running = True

while is_running:

    try:
        action = input("would you like to create a new account or access existing account?\n"
                       " type new for new account, exi for existing account or done to exit out the program: ").strip().lower()
    except ValueError:
        print("Invalid input. Please try again.")
        continue

    if action == "done":
        print("THANK YOU FOR USING THE BANK ACCOUNT APP")
        is_running = False

    elif action == "new":
        name = input("Enter account holder name: ").strip()
        password = input("Enter account password: ").strip()

        if name in accounts:
            print("Username already exists. Try again.")
            continue

        else:
            accounts[name] = bank(name, password, 0)
            print("Account created successfully!")
            continue

    elif action == "exi":
        name = input("Enter account holder name: ").strip()
        password = input("Enter account password: ").strip()

        if name in accounts and accounts[name].password == password:
            bank_acc = accounts[name]
            print("Access granted.")

            while True:

                print(
                    "\nAvailable actions:\n"
                    "deposit\nwithdraw\ncheck balance\nchange password\ntransfer\n nexit")

                user_action = input("Enter action: ").strip().lower()
                match user_action:
                    case "deposit":
                        try:
                            amount = float(input("Enter amount to deposit: "))
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                            continue
                        print(bank_acc.deposit(amount))

                    case "withdraw":
                        try:
                            amount = float(input("Enter amount to withdraw: "))
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                            continue
                        print(bank_acc.withdraw(amount))

                    case "check balance":
                        print(bank_acc.check_balance())

                    case "change password":
                        new_password = input("Enter new password: ").strip()
                        print(bank_acc.change_acccout_password(new_password))

                    case "transfer":
                        try:
                            recipient_name = input(
                                "Enter recipient account holder name: ").strip()
                            accounts_recipient = accounts.get(recipient_name)
                        except ValueError:
                            print("Invalid input. Please try again.")
                            continue
                        if accounts_recipient:
                            try:
                                amount = float(
                                    input("Enter amount to transfer: "))
                            except ValueError:
                                print("Invalid input. Please enter a valid number.")
                                continue
                            if amount > 0 and amount <= bank_acc.balance:
                                bank_acc.withdraw(amount)
                                accounts_recipient.deposit(amount)
                                print(
                                    f"Transferred ${amount} to {recipient_name}.")
                            else:
                                print("Insufficient funds or invalid amount.")
                    case "developer":
                        print("Developer mode activated.")
                        print('        _   ,_,   _')
                        print('       / `\'=) (=\'` \\')
                        print('      /.-.-.\\ /.-.-.\\ ')
                        print('      `      "      `')

                        while True:
                            try:
                                dev_action = input(
                                    "what would you like to do check number of accounts or quit? ").strip().lower()
                            except ValueError:
                                print("Invalid input. Please try again.")
                                continue
                            match dev_action:
                                case "check number of accounts":
                                    print(
                                        f"Total bank accounts: {bank.num_bank_acc}")
                                case "quit":
                                    print("Exiting developer mode.")
                                    break
                                case _:
                                    print(
                                        "Invalid developer action. Please try again.")

                    case "exit":
                        print("Exiting account management.")
                        break

                    case _:
                        print("Invalid action. Please try again.")
        else:
            print("Access denied. Incorrect name or password.")
            continue


# make sure to add transfer function to the list of features users can use
# eeror handling for invalid inputs
