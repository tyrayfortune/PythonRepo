from mimetypes import init


class User:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def display_user_balance(self):
        print(self.account_balance)
        return self


    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

tyray = User(50 + 50 + 50 - 50)
kevin = User(50 + 50 - 50)
james = User(50 - 50 - 50 - 50)

print(tyray.account_balance)

