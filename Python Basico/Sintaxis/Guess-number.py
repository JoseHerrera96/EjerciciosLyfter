import random

secret_number = random.randint(1, 10)
number = 0
while(number != secret_number):
    
    number = int(input("Guess the secret number (between 1 and 10): "))
    if(number < secret_number):
        print("The number is higher")
    elif(number > secret_number):
        print("The number is lower")
    else:
        print("Congratulations! You guessed the secret number.")
