#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
#Withdrawals may not exceed the available balance. Instantiate your class, 
#make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
        else:
            print("Insufficient funds.")
account = Account(input("Owner is: "), abs(float(input("The balance is:"))))

account.deposit(float(input("Write the amount you want to deposit: ")))

account.withdraw(float(input("Write the amount you want to withdraw: ")))