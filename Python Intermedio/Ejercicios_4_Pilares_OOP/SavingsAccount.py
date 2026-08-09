class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance_init, min_balance):
        super().__init__(account_number, balance_init)
        self.__min_balance = min_balance
    
    def withdraw(self, amount):
        if amount <= self.__balance - self.__min_balance:
            self.__balance -= amount
            return self.__balance
        else:
            return "Insufficient funds"
