
import ssl
from unicodedata import name


class BankAccount:
    # amount = 0
    # interest_rate = 0.01
    def __init__(self,name ="",yield_interest = 0.01, account_balance = 0):
        self.account_balance = account_balance
        self.name = name
        self.yield_interest = yield_interest

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        self.account_balance -= amount
        if self.account_balance < 0:
            self.account_balance = self.account_balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self


    def display_account_info(self):
        print(f"{self.name} bank balance is {self.account_balance}")
        
        return self

    def yield_interest(self):
        self.account_balance += (self.account_balance * 1.0)
        return self


class User:
    def __init__(self, account_balance, name):
        self.account_balance = account_balance
        self.account = BankAccount()
        self.name = name 

    def display_user_balance(self):
        print(self.account)
        return self


    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

tyray = User(0, "tyray")
tyray.make_deposit(10 + 10 + 10).make_withdrawl(10 * 4).account.display_account_info()

jack = User(0, name = "Jack")
jack.make_deposit(100 + 50).make_withdrawl(10 * 4).account.display_account_info()
