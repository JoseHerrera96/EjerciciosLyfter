
from pathlib import Path

def read_file(path):
	with open(path) as file:
		return file.read()

if __name__ == "__main__":
	
	current_path = Path(__file__).parent
	file_path = current_path / 'text.txt'
	text = read_file(file_path)
	
	split_words = text.split()
	count = len(split_words)
	
	print(" ")
	print(f"The file contains {count} words.")