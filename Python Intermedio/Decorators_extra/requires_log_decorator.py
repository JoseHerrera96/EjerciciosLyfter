
from functools import wraps

global user_logged_in
user_logged_in : bool = False

def requires_log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise ValueError("Usuario no autenticado")
        else:
            result = func(*args, **kwargs)
            return result
    return wrapper