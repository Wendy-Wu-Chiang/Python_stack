# Create a BankAccount class with the attributes interest rate and balance

class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate=int_rate
        self.balance=balance

# Add a deposit method to the BankAccount class

    def deposit(self, amount):
        self.balance+=amount
        return self
# Add a withdraw method to the BankAccount class
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            self.balance-=5
            print("Insufficient Funds: Charging a $5 fee")
        return self
# Add a display_account_info method to the BankAccount class
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
# Add a yield_interest method to the BankAccount class
    def yield_interest(self):
        if self.balance>0:
            self.balance=self.balance + self.balance * self.int_rate
        return self
# Create 2 accounts
ba1 = BankAccount(balance = 100)
ba2 = BankAccount(0.01, 200)
# To the first account, make 3 deposits and 1 withdrawal,
# then calculate interest and display the account's info all in one line of code (i.e. chaining)
ba1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, 
# then calculate interest and display the account's info all in one line of code (i.e. chaining)
ba2.deposit(1000).deposit(1000).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()