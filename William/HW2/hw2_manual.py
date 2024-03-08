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
        data (csv file): A list of tuples representing parsed pokemon data.
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


def filter_range(data, lower, upper):
    """Returns a list of the names of pokemon whose level fall within the
    bounds in the same order that they appear in the dataset.

    Args:
        data (csv file): data to be accesssed
        lower (int): lower level bound (inclusive)
        upper (int): upper level bound (exclusive)
    """
    poke_list = parse(data)
    species = []
    for i in poke_list:
        if i['level'] >= lower and i['level'] < upper:
            species.append(i['name'])
    return species


def mean_attack_for_type(data, type):
    """
    Returns an int representing the average atk given a type

    Args:
        data (csv file): data to be accesssed
        type (String): type of pokemon

    """
    poke_list = parse(data)
    atk = 0
    count = 0

    for poke in poke_list:
        if poke['type'] == type:
            atk += poke['atk']
            count += 1
    if count == 0:
        return None
    else:
        return atk / count


def count_types(data):
    """
    Returns a dictionary representing for each pokemon type
    the number of pokemon of that type.
    The order of the keys in the returned dictionary does not matter
    Args:
        data (csv file): data to be accessed
    """
    poke_list = parse(data)
    type_occurrences = {}
    for i in poke_list:
        type = i['type']
        if type not in type_occurrences:
            type_occurrences[type] = 1
        else:
            type_occurrences[type] += 1
    return type_occurrences


def mean_attack_per_type(data):
    """
    Returns a dictionary representing for each pokemon
    type the average atk of pokemon of that type

    Args:
        data (csv file): data to be accesssed
    """
    poke_list = parse(data)
    type_atk = {}
    type_mean = {}
    type_occurrences = {}
    # puts the type and atk in a dict (key value pair)
    for i in poke_list:
        type = i['type']
        atk = i['atk']
        if type not in type_atk:
            type_atk[type] = atk
            type_occurrences[type] = 1
        else:
            type_atk[type] += atk
            type_occurrences[type] += 1
    # uses key value pair to find the mean of the atks
    for key, value in type_atk.items():
        mean_atk = value / type_occurrences[key]
        type_mean[key] = mean_atk
    return type_mean
