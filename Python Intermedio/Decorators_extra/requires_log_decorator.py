
from functools import wraps

global user_logged_in
user_logged_in : bool 

def requires_log_decorator(func):
    @wraps(func)
    def wrapper():
        if not user_logged_in:
            raise ValueError("User isn't authenticated")
        else:
            return func(user_logged_in)
    return wrapper