class User:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        return self.account_balance 

User()
print(kevin)


