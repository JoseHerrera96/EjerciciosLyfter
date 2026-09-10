from functools import wraps

def print_parameters_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper
