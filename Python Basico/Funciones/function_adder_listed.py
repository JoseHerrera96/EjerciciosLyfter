def adder(list_of_numbers: list[int]) -> int:
    total = 0
    for number in list_of_numbers:
        total += number
    return total

print(" ")
numbers = [1, 2, 3, 4, 5]
print(f"The sum of {numbers} is {adder(numbers)}")