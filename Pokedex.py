import requests
import json
import os

def get_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def save_pokemon_data(pokemon_data, folder='pokedex'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    pokemon_name = pokemon_data['name']
    file_path = os.path.join(folder, f'{pokemon_name}.json')
    with open(file_path, 'w') as f:
        json.dump(pokemon_data, f, indent=4)

def display_pokemon_data(pokemon_data):
    print(f"Nombre: {pokemon_data['name'].capitalize()}")
    print(f"Peso: {pokemon_data['weight']} hectogramos")
    print(f"Altura: {pokemon_data['height']} decímetros")
    print(f"Tipos: {', '.join([t['type']['name'] for t in pokemon_data['types']])}")
    print(f"Habilidades: {', '.join([a['ability']['name'] for a in pokemon_data['abilities']])}")
    print(f"Movimientos: {', '.join([m['move']['name'] for m in pokemon_data['moves'][:5]])}")
    print(f"Imagen: {pokemon_data['sprites']['front_default']}")

def main():
    pokemon_name = input("Introduce el nombre de un Pokémon: ")
    pokemon_data = get_pokemon_data(pokemon_name)
    if pokemon_data:
        display_pokemon_data(pokemon_data)
        save_pokemon_data(pokemon_data)
    else:
        print("Pokémon no encontrado. Por favor, intenta nuevamente.")

if __name__ == '__main__':
    main()
