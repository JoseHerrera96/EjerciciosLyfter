import json

def load_pokemon_data(file_path='pokemon.json'):
    # Load existing Pokémon data from JSON file, return empty list if file not found
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def print_pokemon_type(pokemon_list, type_input):
    # Print Pokémon with the specified type
    print(" ")
    print(f"Pokémon with type {type_input}:")
    for pokemon in pokemon_list:
        if type_input in pokemon.get('type', []):
            print(f"{pokemon['name']['english']}")
            
    print(" ")

def main():
    # Load existing Pokémon data
    pokemon_list = load_pokemon_data()

    # Prompt user for type input
    print("\n ")
    type_input = input("Enter the type of Pokémon you want to search for (water, electric, fire, etc.):")

    # Print Pokémon with the specified type
    print("\n ")
    print_pokemon_type(pokemon_list, type_input)

if __name__ == "__main__":
    main()
