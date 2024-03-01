# from abc import ABC, abstractmethod
class Account():
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    # @abstractmethod
    def show_balance(self):
        print(f'Balance: {self.balance}')

class SavingsAccount(Account):
    def __init__(self, name, balance=0, interest_rate=0):
        super().__init__(name, balance)
        self.interest_rate = interest_rate
    def deposit_money(self, amount):
        self.balance += amount
    def make_profit(self):
        self.balance += self.balance* self.interest_rate

ac1 = SavingsAccount("Zodu", 500, 0.3)
ac1.make_profit()
ac1.show_balance()