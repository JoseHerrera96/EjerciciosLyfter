def read_file_lines(path):
    with open(path, 'r') as file:
        return file.readlines()
    
def write_file(text, path):
    with open(path, 'w') as file:
        for line in text:
            file.write(f"{line}\n")

def main():
    songs = []
    lines = read_file_lines(r'C:\Users\joseh\Downloads\Lyfter\python begin\songs.txt')
    
    for line in lines:
        song = line.strip()
        songs.append(song)
    
    sorted_songs = sorted(songs)
    write_file(sorted_songs, r'C:\Users\joseh\Downloads\Lyfter\python begin\sorted_songs.txt')


if __name__ == "__main__":
    main()

    