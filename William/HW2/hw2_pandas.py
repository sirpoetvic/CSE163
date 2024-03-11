"""
William Dinh
CSE 163
Pandas version of the HW2 assignment
"""

import pandas as pd


# Your code here!
def species_count(data):
    """
    Takes a pokemon dataset and returns the number of unique
    pokemon species in the dataset as determined by the name

    Args:
        data (csv file): pokemon dataset with attributes
    """
    df = pd.read_csv(data)
    name = df['name'].unique()
    return len(name)


def max_level(data):
    """
    Find the pokemon with the highest level in the given dataset.
    Returns a tuple containing the (name, level)
    of the pokemon with the highest level.
    If there are multiple pokemon with the highest level,
    returns the first encountered.

    Args:
        data (list): data to be accessed
    """
    df = pd.read_csv(data)
    max_lvl = df['level'].max()
    max_level_index = df['level'].idxmax()
    species = df.loc[max_level_index, 'name']
    return (species, max_lvl)


def filter_range(data, lower, upper):
    """Filters pokemon by level, based on lower/upper values

    Args:
        data (csv file): data to be accessed
    """
    df = pd.read_csv(data)
    poke_range = df[(df['level'] >= lower) & (df['level'] < upper)]
    pokemon_sort = poke_range['name']
    return list(pokemon_sort)


def mean_attack_for_type(data, type):
    """Finds the mean attack of all pokemon given a type

    Args:
        data (csv file): data to be accessed
        type (String): pokemon type to be assessed
    """
    df = pd.read_csv(data)
    poke_range = df[df['type'] == type]
    mean_attack = poke_range['atk'].mean()
    if poke_range.empty:
        return None
    return mean_attack


def count_types(data):
    """counts the number of unique types of pokemon
    returns a dict with all pokemon types

    Args:
        data (csv): data to be accessed
    """
    df = pd.read_csv(data)
    poke_range = df['type'].value_counts()
    poke_dict = dict(poke_range)
    return poke_dict


def mean_attack_per_type(data):
    """Finds the mean attack of all types, returns a dict with them

    Args:
        data (csv file): data to be accessed
    """
    df = pd.read_csv(data)
    poke_range = df.groupby('type')['atk'].mean()
    return dict(poke_range)
