class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def promote(self, raise_amount):
        self._salary += raise_amount
    
    @property
    def Employee(self):
        return self._name, self._salary
    
    @Employee.setter
    def Employee(self, new_name):
        if salary > 0:
            self._name = new_name
            self._salary = salary
        else:
            print("El salary must be be positive")


