class Account:
  def __init__(self,owner,balance=0):
    self.owner = owner
    self.balance = balance

  def deposit(self,amount):
    if amount>0:
      self.balance += amount
      print(f"Deposited amount : {amount},bank balance: {self.balance}")
    else:
      print("no amount deposited")

  def withdraw(self,amount):
     if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def check_balance(self):
        return self.balance

account = BankAccount("Aishpreet", 100)  
account.deposit(50)  
account.withdraw(30) 
print(f"Current balance: {account.check_balance()}")
    
    
  
  

  
