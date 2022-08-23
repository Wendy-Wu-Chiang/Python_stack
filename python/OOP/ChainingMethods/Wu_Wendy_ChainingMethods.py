# If you've been following along, you're going to utilize the User class we've been discussing for this assignment.
# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150

# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.account_balance=0
    
    def make_Deposit(self, amount):
        self.account_balance+=amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance-=amount
        return self

    def display_user_balance(self):
        print(f"user:{self.name},Balance:${self.account_balance}")

    def transfer_money(self,other_user,amount):
        self.account_balance-=amount
        print(self.name, self.account_balance)
        print(other_user.name)

        # other_user.account_balance+=amount
        # other_user.make_Deposit(amount)
        # self.make_withdrawal(amount) 
        # return self
    

Guido=User("Guido", "guido@gmail.com")
Adom=User("Adom", "adom@gmail.com")
Will=User("Will", "will@gmail.com")

Guido.make_Deposit(10).make_Deposit(100).make_Deposit(100).make_withdrawal(100).display_user_balance()

Adom.make_Deposit(100).make_Deposit(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

Will.make_Deposit(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

Will.transfer_money(Adom,100)  

   







    

