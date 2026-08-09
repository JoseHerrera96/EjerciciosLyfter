class BankAccount:
    def __init__(self, account_number, balance_init):
        self.account_number = account_number
        self.__balance = balance_init

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            return "Insufficient funds"
