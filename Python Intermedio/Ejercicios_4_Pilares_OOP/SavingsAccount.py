from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance_init, min_balance):
        super().__init__(account_number, balance_init)
        self._min_balance = min_balance
    
    def withdraw(self, amount):
        if amount <= self.get_balance() - self._min_balance:
            withdraw = super().withdraw(amount)
            return  withdraw
        else:
            return "Insufficient funds"
