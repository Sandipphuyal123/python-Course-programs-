class wallet:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, depo_amt):
        self.balance += depo_amt
        print(f'{depo_amt} has been successfully Deposited.')
        print(f'your current balance: {self.balance}')
        return 'Thank you for using our service!\n\n'
    
    def withdraw(self, with_amt):
        if with_amt > self.balance: 
            return f'Insufficient Balance, your withdraw of {with_amt} has failed.\n your balance: {self.balance}'
        else:
            self.balance -= with_amt
            print(f'{with_amt} has been successfully withdrawn.')
            print(f'your current balance: {self.balance}')
            return 'Thank you for using our service!'
obj = wallet(500)
print(obj.deposit(120))
print(obj.withdraw(500))


# This can also be done 
# class Wallet:
#    def __init__(self):
#        self.__balance = 0

#    def __validate(self, amount):
#        if amount < 0:
#            raise ValueError('Amount must be positive')

#    def deposit(self, amount):
#        self.__validate(amount)
#        self.__balance += amount

#    def withdraw(self, amount):
#        self.__validate(amount)
#        if amount > self.__balance:
#            raise ValueError('Insufficient funds')
#        self.__balance -= amount

#    def get_balance(self):
#        return self.__balance

# acct_one = Wallet()
# acct_one.deposit(3)
# print(acct_one.get_balance()) # 3

# acct_one.deposit(50)
# print(acct_one.get_balance()) # 53

# acct_one.deposit(-4)  # ValueError: Amount must be positive
# acct_one.withdraw(-8) # ValueError: Amount must be positive
# acct_one.withdraw(58) # ValueError: Insufficient funds