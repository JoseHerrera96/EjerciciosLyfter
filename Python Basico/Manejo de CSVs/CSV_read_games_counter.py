import csv

def read(filepath):
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        list_of_games = list(reader)
        headers = reader.fieldnames
    return list_of_games, headers

if __name__ == "__main__":
    games, headers = read('./games.csv')
    print(" ")
    count_genre = {}
    for game in games:
        genre = game["genres"]
        if genre in count_genre:
            count_genre[genre] += 1
        else:
            count_genre[genre] = 1
    for genre, count in count_genre.items():
        print(f"{genre}: {count}")
    
