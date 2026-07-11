def find_word(text: str, word: str) -> int:
    """Find all occurrences of a word in a given text and return their starting indices.

    Args:
        text (str): The text to search within.
        word (str): The word to search for.
    Returns:
        int: The count of occurrences of the word in the text.
    """

    indices = []
    index = text.find(word)
    while index != -1:
        indices.append(index)
        index = text.find(word, index + 1)
    
    counter = len(indices)
    return counter

print(" ")
text = "Hello world, welcome to the world of Python programming."
word = "world"
count = find_word(text, word)
print("text: " + text)
print(f"The word '{word}' occurs {count} times in the given text.")
