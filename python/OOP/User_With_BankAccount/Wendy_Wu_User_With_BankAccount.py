
# Update the User class __init__ method

class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.account= BankAccount(int_rate=0.02, balance=0)

# Update the User class make_deposit method 

    def make_Deposit(self, amount):
        self.account.deposit(amount)
        return self

# Update the User class make_withdrawal method 

    def make_Withdraw(self, amount):
        self.account.withdraw(amount)
        return self

# Update the User class display_user_balance method

    def display_user_balance(self):
        self.account.displayAccountInfo()
        return self

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate= int_rate
        self.balance=balance
        

    
    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        if(amount<=self.balance):
            self.balance-=amount
        else:
            print("insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self

    def displayAccountInfo(self):
        print("Balance: ", self.balance)
        return self

    def yieldInterest(self):
        if(self.balance>=0):
            self.balance+= self.balance * self.int_rate
        return self

# ba1 = BankAccount(0.02, 100)
# ba2 = BankAccount(0.01, 200)
# SENSEI BONUS: Allow a user to have multiple accounts; update methods 
# so the user has to specify which account they are withdrawing or depositing to        



Adam = User("Adam", "adam@gmail.com")
Adam.ba1.make_Deposit(1000).make_Deposit(1000).make_Withdraw(1000).display_user_balance()
Adam.account.yieldInterest().displayAccountInfo()
Adam.display_user_balance()



        
    

