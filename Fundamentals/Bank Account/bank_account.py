
import ssl
from unicodedata import name


class BankAccount:
    # amount = 0
    # interest_rate = 0.01
    def __init__(self,name, account_balance = 0,):
        self.account_balance = account_balance
        self.name = name
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
        self.account_balance += (self.account_balance * 0.01)
        return self



tyray = BankAccount(name = "Tyray")
tyray.deposit(10 + 10 + 10).withdraw(50).yield_interest().display_account_info()

jack = BankAccount(name = "Jack")
jack.deposit(100 + 50).withdraw(10 * 4).yield_interest().display_account_info()