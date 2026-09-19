from functools import wraps

def duplicator_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@duplicator_decorator
def say_hi(name):
    print(f"Hi, {name}!")