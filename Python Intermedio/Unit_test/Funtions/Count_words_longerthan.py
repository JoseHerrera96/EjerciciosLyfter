def count_letters(words: list[str], n: int) -> list[str]:
    """returns a list of words that have more than n letters.

    Args:
        words (list[str]): The input list of words to analyze.
        n (int): The minimum number of letters a word must have to be included.

    Returns:
        list[str]: A list of words that have more than n letters.
    """
    
    result = []
    for word in words:
        if len(word) > n:
            result.append(word)

    return result

print(" ")
words = ["Azucar", "Banana", "Cereza", "Dátil", "Elderberry", "Higo", "Uva", "Manzana", "Naranja", "Papaya", "Quince", "Frambuesa", "Fresa", "Tamarindo", "Mango", "Melocotón", "Pera", "Piña", "Ciruela", "Sandía"]
n = 4
print("words: " + str(words))
print("n: " + str(n))
result = count_letters(words, n)
print(f"Words that have more than {n} letters: \n{result}")