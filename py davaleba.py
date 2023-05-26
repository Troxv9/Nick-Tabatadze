import requests
import json
import sqlite3

def fetch_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    response.raise_for_status()
    pokemon_data = response.json()
    return pokemon_data

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def print_pokemon_info(pokemon_data):
    print("Pokemon Info:")
    print(f"Name: {pokemon_data['name']}")
    print(f"Height: {pokemon_data['height']}")
    print(f"Weight: {pokemon_data['weight']}")
    print("Abilities:")
    for ability in pokemon_data['abilities']:
        print(f"- {ability['ability']['name']}")

def create_database_table():
    conn = sqlite3.connect('pokemon.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pokemon
                    (id INTEGER PRIMARY KEY, name TEXT, height INTEGER, weight INTEGER)''')
    conn.commit()
    conn.close()

def insert_into_database(pokemon_data):
      conn = sqlite3.connect('pokemon.db')
      cursor = conn.cursor()
      cursor.execute("INSERT INTO pokemon (id, name, height, weight) VALUES (?, ?, ?, ?)",
                     (pokemon_data['id'], pokemon_data['name'], pokemon_data['height'], pokemon_data['weight']))
      conn.commit()
      conn.close()

# Fetch data for Pokemon with ID 1
pokemon_data = fetch_pokemon_data(1)

# Save the data in a JSON file
save_to_json(pokemon_data, 'pokemon.json')

# Print information from the JSON object
print_pokemon_info(pokemon_data)

# Create the database table
create_database_table()

# Insert the Pokemon data into the database
insert_into_database(pokemon_data)



