from functools import wraps

def print_parameters_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper
