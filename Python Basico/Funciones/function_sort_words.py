def sort_words_by_hyphen(text: str) -> str:
    words = text.split("-")
    words.sort()
    return "-".join(words)


print(" ")
input_text = "banana-apple-cherry-date"
sorted_text = sort_words_by_hyphen(input_text)
print(f"Original text: {input_text}")
print(f"Sorted text: {sorted_text}")