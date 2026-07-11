def counter_lowercase_uppercase(text: str) -> tuple[int, int]:
    lower_count = 0
    upper_count = 0
    for char in text:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    return lower_count, upper_count

print(" ")
sample_text = "Hello World!"
lower, upper = counter_lowercase_uppercase(sample_text)
print(f"In the text: '{sample_text}'")
print(f"Lowercase letters: {lower}, Uppercase letters: {upper}")