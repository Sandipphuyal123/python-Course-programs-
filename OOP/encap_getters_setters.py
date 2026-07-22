class BankAccount:
    def __init__(self, balance):
        self.balance = balance  

    @property
    def balance(self):
        print("Checking balance safely...")
        return self._balance

    @balance.setter
    def balance(self, new_amount):
        if new_amount < 0:
            print("Error: Starting balance cannot be negative! Setting to 0 instead.")
            self._balance = 0
        else:
            self._balance = new_amount
# watch this siMulation

# Scenario 1: Someone tries to start with -$500
account1 = BankAccount(-500) # although this doesnt happen in static code data since the coder will not write this data but if this was a dynamic data it will- 
# -handle this perfectly
# Output: Error: Starting balance cannot be negative! Setting to 0 instead.

print(account1.balance)
# Output: Checking balance safely... --> 0