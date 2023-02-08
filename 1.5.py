class bankaccount():
  def __init__(self, owner = '', balance = 0):
    self.owner = owner
    self.balance = balance 

  def __str__(self):
        print (f'Account owner: {self.owner}\n Account balance: ${self.balance}')
        
  def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')
        
  def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


p1 = bankaccount("Dina" , 1000000)

      
p1.deposit(50)

p1.withdraw(75)

p1.withdraw(5000000) #checking  