import random

SECRET_NUMBER = random.randint(1, 10)

print("Guess the secret number (1 to 10):")

attempt = int(input("Your guess: "))

while attempt != SECRET_NUMBER:
    print("Incorrect. Try again.")
    attempt = int(input("Your guess: "))

print("Congratulations! You guessed the number.")
