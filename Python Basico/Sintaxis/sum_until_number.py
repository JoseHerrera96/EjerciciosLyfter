limit = int(input("Enter a positive integer: "))

counter = 1
running_sum = 0

while counter <= limit:
    running_sum += counter
    counter += 1

print("\n---")
print(f"The sum of the numbers from 1 to {limit} is: {running_sum}")
