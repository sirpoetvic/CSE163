"""
William Dinh
CSE 163
No pandas version of the HW2 assignment
"""

from cse163_utils import parse


# Your code here!
def species_count(data):
    """
    Takes a parsed pokemon dataset and returns the number of unique
    pokemon species in the dataset as determined by the name

    Args:
        data (csv file): pokemon dataset with attributes
    """
    poke_list = parse(data)
    unique_pokemon = set()
    for i in poke_list:
        unique_pokemon.add(i['name'])
    return len(unique_pokemon)


def max_level(data):
    """
    Find the pokemon with the highest level in the given dataset.
    Returns a tuple containing the (name, level)
    of the pokemon with the highest level.
    If there are multiple pokemon with the highest level,
    returns the first encountered.

    Args:
        data (list): A list of tuples representing parsed pokemon data.
            Each tuple contains (name, level) where name is the
            name of the pokemon and level is its corresponding level
    """
    poke_list = parse(data)
    level = 0
    species = ''
    for i in poke_list:
        if i['level'] > level:
            level = i['level']
            species = i['name']
    return (species, level)
