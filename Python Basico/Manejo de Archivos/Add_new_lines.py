
from anyio import Path

def add_lines_file(text, path):
    with open(path, 'a') as file:
        for line in text:
            file.write(f"{line}\n")

if __name__ == "__main__":

    current_path = Path(__file__).parent
    file_path = current_path / 'output_text.txt'
    
    print(" ")
    n_lines = int(input("How many lines do you want to write? "))
    
    for i in range(n_lines):
        line = input(f"Enter line {i+1}: ")
        add_lines_file([line], file_path)
    
