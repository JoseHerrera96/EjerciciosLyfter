def addition_list(numbers):
    total = 0
    for num in numbers:
        try:
            total += float(num)
            print(f"Added {num} to total. Current total: {total}")
        except ValueError as e:
            print(f"Cannot convert '{num}' to a number.")
    
    print(" ")
    print(f"The sum of the numbers is: {total}")

if __name__ == "__main__":
    numbers = ["10", "20", "abc", "30.5", "xyz"]
    print(" ")
    print(f"Original list: {numbers}")
    print(" ")
    addition_list(numbers)