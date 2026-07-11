import csv

def write_csv(filepath, data, headers):
    with open(filepath, 'w', encoding = 'utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, headers)
        writer.writeheader()
        writer.writerows(data)

def get_new_game(games):
    print(" ")
    game={}
    name = input("Enter game name: ")
    genre = input("Enter game genre: ")
    developer = input("Enter game developer: ")
    classification_ESRB = input("Enter game ESRB classification: ")
    game["names"] = name
    game["genres"] = genre
    game["developers"] = developer
    game["ESRB_classification"] = classification_ESRB
    games.append(game)
    return games

if __name__ == "__main__":
    games = []
    print(" ")
    n = int(input("How many games do you want to add? "))
    headers = ["names", "genres", "developers", "ESRB_classification"]
    for i in range(n):
        games = get_new_game(games)
    write_csv('python begin/games.csv', games, headers)
        
