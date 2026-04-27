class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
    def balance_check(self):
        return self.balance
    
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.balance_check())