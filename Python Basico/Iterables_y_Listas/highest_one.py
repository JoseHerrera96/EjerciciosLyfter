numbers = []

print(" ")
print("Please enter 10 numbers:")
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("\nNumbers entered:")
print(numbers)

print(f"\nHighest number: {max(numbers)}")