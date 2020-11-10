class Account:
    apr = 3.0
    
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = 'Generic Account'
        
    def calc_interest(self):
        return f'Calc interest on {self.account_type} with APR = {type(self).apr}'
        
        
class Savings(Account):
    apr = 5.0
    
    def __init__(self, account_number, balance):
        self.account_number = account_number  # We'll revisit this later - this is clumsy
        self.balance = balance
        self.account_type = 'Savings Account'

a = Account(100, 100)
s1 = Savings(101, 100)
s2 = Savings(102, 100)

s2.apr = 10