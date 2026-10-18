class BankAccount:
    # Keep account details private so they cannot be changed directly.
    def __init__(self, number, money):
        self.__account_number = number
        self.__balance = money

    # Replace the current account number with a new one.
    def set_account_number(self, new_number):
        self.__account_number = new_number

    # Only accept a new balance if it is zero or greater.
    def set_balance(self, new_balance):
        if new_balance < 0:
            print("The balance must be not a negative number.")
            return

        self.__balance = new_balance

    # Allow other parts of the program to read the account number.
    @property
    def account_number(self):
        return self.__account_number

    # Allow other parts of the program to read the balance.
    @property
    def balance(self):
        return self.__balance


# Make a bank account using the given sample values.
account1 = BankAccount(12345, 1000)

print("Account 1")
print("Account Number:", account1.account_number)
print("Balance: {:.2f}".format(account1.balance))

# Try setting an invalid balance to check the validation.
print()
print("Update balance to -100")
account1.set_balance(-100)

# Display the details again to check that the old balance remains.
print("Account Number:", account1.account_number)
print("Balance: {:.2f}".format(account1.balance))
