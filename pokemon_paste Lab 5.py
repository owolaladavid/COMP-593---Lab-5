""" 
Description: 
  Creates a new PasteBin paste that contains a list of abilities 
  for a specified Pokemon

Usage:
  python pokemon_paste.py poke_name

Parameters:
  poke_name = Pokemon name
"""
import sys
import poke_api
import pastebin_api

def main():
    poke_name = get_pokemon_name()
    poke_info = poke_api.get_pokemon_info(poke_name)
    #if pokemon_info is not None:
    paste_title, paste_body = get_paste_data(poke_info)
    paste_url = pastebin_api.post_new_paste(paste_title, paste_body, '1M')
    print(paste_url)



def get_pokemon_name():
    """Gets the name of the Pokemon specified as a command line parameter.
    Aborts script execution if no command line parameter was provided.

    Returns:
        str: Pokemon name
    """
    # TODO: Function body
    pokemon_name = sys.argv[2]
    if pokemon_name == '':
        print("Error:Parameter is missing")
        sys.exit(1)
    
    return pokemon_name

def get_paste_data(pokemon_data):
    """Builds the title and body text for a PasteBin paste that lists a Pokemon's abilities.

    Args:
        pokemon_info (dict): Dictionary of Pokemon information

    Returns: 
        (str, str): Title and body text for the PasteBin paste
    """    
    # TODO: Build the paste title
    # TODO: Build the paste body text
    poke_name = get_pokemon_name()
    formatted_poke_name = poke_name.title()
    title = f"{poke_name}\'s Abilities"
    abilities_List=[]
    for ability_info in pokemon_data["abilities"]:
       
        ability_name = ability_info["ability"]["name"].strip('\n')
        formatted_text = f"- {ability_name}"
        abilities_List.append(formatted_text)
    abilities_tuple = tuple(abilities_List)
    abilities_text = '\n'.join(abilities_tuple)
    return  (title, abilities_text)

if __name__ == '__main__':
    main()