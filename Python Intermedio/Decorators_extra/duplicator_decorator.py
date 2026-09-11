from functools import wraps

def say_hi(name):
    print(f"Hi, {name}!")

def duplicator_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper
