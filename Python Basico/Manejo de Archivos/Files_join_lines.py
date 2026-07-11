
from anyio import Path

def read_file_lines(path):
    with open(path, 'r') as file:
        return file.readlines()

def join_lines(lines):
    processed_lines = []
    for line in lines:
        line = line.rstrip("\n")
        processed_lines.append(line + " ")
    return ''.join(processed_lines)
    
if __name__ == "__main__":

    current_path = Path(__file__).parent
    file_path = current_path / 'text.txt'
    lines = read_file_lines(file_path)

    joined_lines = join_lines(lines)

    print(" ")
    print(joined_lines)