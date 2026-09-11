
from functools import wraps

def requires_log_decorator(func):
    @wraps(func)
    def wrapper(user_logged_in):
        if not user_logged_in:
            raise ValueError("User isn't authenticated")
        else:
            return func(user_logged_in)
    return wrapper