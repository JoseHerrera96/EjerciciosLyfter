
from pathlib import Path

def read_file_lines(path):
    with open(path, 'r') as file:
        return file.readlines()

def write_file(text, path):
    with open(path, 'w') as file:
        for line in text:
            file.write(f"{line}\n")

def make_uppercase(lines):
    upper_lines = []
    for line in lines:
        line = line.rstrip("\n")
        line=line.upper()
        upper_lines.append(line)
    return upper_lines

if __name__ == "__main__":
    
    current_path = Path(__file__).parent
    read_file_path = current_path / 'text.txt'
    write_file_path = current_path / 'text_upper.txt'

    lines = read_file_lines(read_file_path)

    upper_lines = make_uppercase(lines)

    write_file(upper_lines, write_file_path)
    
