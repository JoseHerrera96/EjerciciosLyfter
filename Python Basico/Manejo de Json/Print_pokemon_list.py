import json

def load_pokemon_data(file_path='pokemon.json'):
    # Load existing Pokémon data from JSON file, return empty list if file not found
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def print_pokemon_list(pokemon_list):
    # Print the current Pokémon list

    if not pokemon_list:
        print("No Pokémon in the list.")
        return

    # Print the header
    print("\n ")
    print("Current Pokémon List:")
    print(f"{'#':<3} {'Name':<15} {'Type':<15} {'HP':<5}")
    print("-" * 45)

    # Print each Pokémon in the list
    for idx, pokemon in enumerate(pokemon_list, 1):
        try:
            # Extract name
            name_data = pokemon.get('name', 'Unknown')
            name = name_data.get('english', 'Unknown') if isinstance(name_data, dict) else str(name_data)
            name = name

            # Extract type
            type_data = pokemon.get('type', 'Unknown')
            p_type = ", ".join(type_data) if isinstance(type_data, list) else str(type_data)
            p_type = p_type

            # Extract HP 
            hp = pokemon.get('base', {}).get('HP', 'N/A')
            hp = str(hp)

            print(f"{idx:<3} {name:<15} {p_type:<15} {hp:<5}")
        except Exception as e:
            print(f"{idx:<3} {'Error':<15} {'Invalid entry':<15} {'N/A':<5}")



def main():
    # Load existing Pokémon data
    pokemon_list = load_pokemon_data()
    
    #print the current Pokémon list
    print_pokemon_list(pokemon_list)

if __name__ == "__main__":
    main()