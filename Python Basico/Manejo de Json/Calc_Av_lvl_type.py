import json

def load_pokemon_data(file_path='pokemon.json'):
    # Load existing Pokémon data from JSON file, return empty list if file not found
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def group_per_type(pokemon_list):
    # Group Pokémon by type
    grouped_pokemon = {}
    for pokemon in pokemon_list:
        type_data = pokemon.get('type', 'Unknown')
        if isinstance(type_data, list):
            for p_type in type_data:
                truncated_type = str(p_type)
                grouped_pokemon.setdefault(truncated_type, []).append(pokemon)
        else:
            p_type = str(type_data)
            grouped_pokemon.setdefault(p_type, []).append(pokemon)
    return grouped_pokemon

def calc_av_lvl(pokemon_list):
    # Calculate average level of Pokémon in the list
    total_level = 0
    for pokemon in pokemon_list:
        level = pokemon.get('level', 0)
        total_level += level
    if total_level:
        return total_level / len(pokemon_list)
    else:
        return 0

def main():
    # Load existing Pokémon data
    pokemons = load_pokemon_data()

    #Group Pokémon by type
    grouped_pokemon = group_per_type(pokemons)

    #Calculate and print average level per type
    print("\n ")
    print("Average Level per Type")
    for p_type, pokemon_list in grouped_pokemon.items():
        av_lvl = calc_av_lvl(pokemon_list)
        print(f"Type: {p_type:<15} Average Level: {av_lvl:<5.2f}")

if __name__ == "__main__":
    main()
