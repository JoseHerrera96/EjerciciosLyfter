import json

def load_pokemon_data(file_path='pokemon.json'):
    # Load existing Pokémon data from JSON file, return empty list if file not found
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def print_pokemon_stats(pokemon_list):
    # Print the current Pokémon stats

    if not pokemon_list:
        print("No Pokémon in the list.")
        return

    print("Pokémon Stats:")

    for idx, pokemon in enumerate(pokemon_list, 1):
        try:
            print(" ")
            # Extract name
            name_data = pokemon.get('name', 'Unknown')
            name = name_data.get('english', 'Unknown') if isinstance(name_data, dict) else str(name_data)
            name = name[:14]

            # Extract type
            type_data = pokemon.get('type', 'Unknown')
            p_type = ", ".join(type_data) if isinstance(type_data, list) else str(type_data)
            p_type = p_type

            # Extract stats
            hp = pokemon.get('base', {}).get('HP', 'N/A')
            hp = str(hp)
            Attack = pokemon.get('base', {}).get('Attack', 'N/A')
            Attack = str(Attack)
            Defense = pokemon.get('base', {}).get('Defense', 'N/A')
            Defense = str(Defense)
            Speed = pokemon.get('base', {}).get('Speed', 'N/A')
            Speed = str(Speed)
            Special_Attack = pokemon.get('base', {}).get('Sp. Attack', 'N/A')
            Special_Attack = str(Special_Attack)
            Special_Defense = pokemon.get('base', {}).get('Sp. Defense', 'N/A')
            Special_Defense = str(Special_Defense)

            print(f"Name:{name:<15}\n  Type: {p_type:<15}\n  HP: {hp:<5}\n  Attack: {Attack:<5}\n  Defense: {Defense:<5}\n  Speed: {Speed:<5}\n  Special Attack: {Special_Attack:<5}\n  Special Defense: {Special_Defense:<5}")
        except Exception as e:
            print(f"{'Error':<15} {'Invalid entry':<15} {'N/A':<5}")

def main():
    # Load existing Pokémon data
    pokemon_list = load_pokemon_data()

    # Print the Pokémon stats
    print("\n ")
    print_pokemon_stats(pokemon_list)

if __name__ == "__main__":
    main()
