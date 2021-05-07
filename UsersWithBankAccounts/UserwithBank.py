class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(account_name='', int_rate=0.01, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}")
        self.account.display_account_info()
        return self

class BankAccount:
    def __init__(self, account_name, int_rate=0.01, balance=0):
        self.account_name = account_name
        self.int_rate = int_rate
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f"Account type: {self.account_name} Balance: {self.account_balance}")
        return self

    def yield_interest(self):
        self.account_balance *= (self.int_rate + 1)
        return self

sean = User("Sean", "seanruddell@yahoo.com")
guido = User("Guido", "guido@yahoo.com")
monty = User("Monty", "montymcgoo@yahoo.com")
savings = BankAccount("Savings", 0.01)
checking = BankAccount("Checking", 0.015)

sean.make_deposit(150).make_deposit(5000).make_deposit(200).make_withdrawl(250).account.yield_interest()
sean.display_user_balance()