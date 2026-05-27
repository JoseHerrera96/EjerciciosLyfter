import json

def load_pokemon_data(file_path='pokemon.json'):
    # Load existing Pokémon data from JSON file, return empty list if file not found
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        
def collect_pokemon_input():
    # new Pokémon information from user input
    print("\n ")
    english_name = input("Enter the Pokémon's English name: ")
    level = int(input("Enter the Pokémon's level: "))
    type_input = input("Enter the Pokémon's type (comma-separated for multiple types): ")

    # Split input into type list and strip whitespace
    type_list = [t.strip() for t in type_input.split(',')]
    hp = int(input("Enter the Pokémon's base HP: "))
    attack = int(input("Enter the Pokémon's base Attack value: "))
    defense = int(input("Enter the Pokémon's base Defense value: "))
    sp_attack = int(input("Enter the Pokémon's base Special Attack value: "))
    sp_defense = int(input("Enter the Pokémon's base Special Defense value: "))
    speed = int(input("Enter the Pokémon's base Speed value: "))
    
    # new Pokémon
    return {
        "name": {
            "english": english_name
        },
        "level": level,
        "type": type_list,
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }

def save_pokemon_data(pokemon_list, file_path='pokemon.json'):
    #Save updated Pokémon list back to the JSON file
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(pokemon_list, file, indent=4, ensure_ascii=False)

def main():
    # Load existing Pokémon data
    pokemon_list = load_pokemon_data()
    
    # Collect and add new Pokémon
    new_pokemon = collect_pokemon_input()
    pokemon_list.append(new_pokemon)
    
    # Save updated data
    save_pokemon_data(pokemon_list)

if __name__ == "__main__":
    main()
