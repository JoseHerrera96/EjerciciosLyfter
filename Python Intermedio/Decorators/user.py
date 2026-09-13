from datetime import date
from functools import wraps

class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return ((today.year- self.date_of_birth.year) - 
            ((today.month, today.day)< (self.date_of_birth.month, self.date_of_birth.day)))

def underage_test_decorator(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError("User is underage")
        return func(user, *args, **kwargs)
    return wrapper
