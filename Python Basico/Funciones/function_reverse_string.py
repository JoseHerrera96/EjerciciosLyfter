def reverse_string(text: str) -> str:
    return text[::-1]

print(" ")
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(f"The reverse of '{input_string}' is '{reversed_string}'")