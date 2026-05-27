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
    headers_tab = "\t".join(headers)
    classification_ESRB_input = input("Enter ESRB classification to filter by: ")
    print(headers_tab)
    for game in games:
        if game["ESRB_classification"] == classification_ESRB_input:
            print_game = "\t".join(list(game.values()))
            print(print_game)
            