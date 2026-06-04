class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def display(self):
        print(self.account_number)
        print(self.balance)
        print(self.interest_rate)

s = SavingsAccount(12345, 10000, 5)
s.display()