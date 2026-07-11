def count_vowels(text: str) -> int:
    """Count the number of vowels in a given text.

    Args:
        text (str): The input text.
    Returns:
        int: The number of vowels in the text.
    """
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1
    return count

print(" ")
text = "Hello world, welcome to the world of Python programming."
vowel_count = count_vowels(text)
print("text: " + text)
print(f"The number of vowels in the text is: {vowel_count}")