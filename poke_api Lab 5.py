'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Pikachu")
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

        Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    cleaned_pokemon_name = pokemon_name.strip(' ')
    new_output_of_pokemon_name =cleaned_pokemon_name.lower()
    # TODO: Build a clean URL and use it to send a GET request
    resp_msg = requests.get(POKE_API_URL + new_output_of_pokemon_name)
    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
   
    if resp_msg.status_code == requests.codes.ok:
        body_dict = resp_msg.json()
        print(f"Getting information for {new_output_of_pokemon_name}....success")
        return body_dict
    # TODO: If the GET request failed, print the error reason and return None
    else:
        return None
    

if __name__ == '__main__':
    main()