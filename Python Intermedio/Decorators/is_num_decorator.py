
from functools import wraps

def is_num_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise ValueError("All arguments must be numbers")
        result = func(*args, **kwargs)
        return result
    return wrapper