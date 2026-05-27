# Request a valid number from 1 to 10
while True:
    try:
        number = int(input("Enter a number from 1 to 10: "))
        if 1 <= number <= 10:
            break
        else:
            print("Out of range. Must be between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Show the table from 1 to 12
print(f"\nMultiplication table for {number} (1 to 12):")
print("-" * 34)
for i in range(1, 13):
    result = number * i
    # Aligned format
    print(f"{number} x {i:2} = {result:3}")
