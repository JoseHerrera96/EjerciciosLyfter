import csv

def read(filepath):
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        list_of_games = list(reader)
        headers = reader.fieldnames
    return list_of_games, headers

if __name__ == "__main__":
    games, headers = read('./games.csv')
    dev_query = input("Enter developer to filter by: ")
    for game in games:
        if game["developers"] == dev_query:
            print(game['names'])