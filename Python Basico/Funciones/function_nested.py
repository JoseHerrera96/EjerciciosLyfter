def cube(x):
    return square(x) * x

def square(x):
    return x * x

number = 3
print(" ")
print(f"The square of {number} is {square(number)}")
print(f"The cube of {number} is {cube(number)}")