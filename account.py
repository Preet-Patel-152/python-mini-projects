# Deposit

# Withdraw

# Check balance


class bank:
    num_bank_acc = 0

    def __init__(self, account_holder={}, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        bank.num_bank_acc += 1

    def change_acccout_password(self, new_password):
        for holder in self.account_holder:
            self.account_holder[holder] = new_password
        return f"Password changed successfully for {list(self.account_holder.keys())[0]}."

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount}. New balance: ${self.balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew: ${amount}. New balance: ${self.balance}."
            else:
                return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def check_balance(self):
        return f"Current balance: ${self.balance}."
