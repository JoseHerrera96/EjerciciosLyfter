def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):  # Trial Division method
        if num % i == 0:
            return False
    return True


def find_prime(numbers: list[int]) -> list[int]:
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes

print(" ")
input_numbers = [10, 15, 3, 7, 19, 22, 29, 4]
prime_numbers = find_prime(input_numbers)
print(f"Original numbers: {input_numbers}")
print(f"Prime numbers: {prime_numbers}")