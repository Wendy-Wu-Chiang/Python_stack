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

    def make_withdrawal(self, amount):
        self.account_balance-=amount

    def display_user_balance(self):
        print(f"user:{self.name},Balance:${self.account_balance}")

    def transfer_money(self,other_user,amount):
        # self.account_balance-=amount
        self.other_user = other_user
        print(self.name, self.account_balance)
        print(self.other_user)
        # print(self.other_user.account_balance)
        self.other_user.make_Deposit(amount)
        self.make_withdrawal(amount)  
        # not working)


Guido=User("Guido", "guido@gmail.com")
Adom=User("Adom", "adom@gmail.com")
Will=User("Will", "will@gmail.com")

Guido.make_Deposit(10)
Guido.make_Deposit(100)
Guido.make_Deposit(100)
Guido.make_withdrawal(100)
Guido.display_user_balance()

Adom.make_Deposit(100)
Adom.make_Deposit(100)
Adom.make_withdrawal(100)
Adom.make_withdrawal(100)
Adom.display_user_balance()

Will.make_Deposit(1000)
Will.make_withdrawal(100)
Will.make_withdrawal(100)
Will.make_withdrawal(100)
Will.display_user_balance()

Will.transfer_money("Adom",100)  


   







    

