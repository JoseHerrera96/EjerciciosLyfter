class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary

    def promote(self, raise_amount):
        self._salary += raise_amount*self._salary
    
    @property
    def name(self):
        return self._name
    
    @property
    def salary(self):
        return self._salary

    
    @salary.setter
    def salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("The salary must be be positive")


