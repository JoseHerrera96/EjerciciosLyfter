from functools import wraps
from datetime import datetime

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs} at {datetime.now()}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

def validate_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise ValueError("All arguments must be numbers")
        else:
            result = func(*args, **kwargs)
            print(f"Result: {result}")
            return result
    return wrapper


@log_call
@validate_numbers
def multiply(A, B):
    return A * B