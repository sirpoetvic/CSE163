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


def filter_range(data):
    """_summary_

    Args:
        data (csv file): data to be accessed
    """
    df = pd.read_csv(data)
    poke_range = df[(df['level'] >= 35) & (df['level'] < 72)]
    pokemon_sort = poke_range['name']
    return list(pokemon_sort)


def mean_attack_for_type(data, type):
    """_summary_

    Args:
        data (_type_): _description_
        type (_type_): _description_
    """
    df = pd.read_csv(data)
    poke_range = df[df['type'] == type]
    mean = poke_range['atk'].mean()

    if type not in poke_range:
        return None
    return mean


def count_types(data):
    poke_range = data['type'].value_counts()
    poke_dict = dict(poke_range)
    return poke_dict


def mean_attack_per_type(data):
    df = pd.read_csv(data)
    poke_range = df.groupby('type')['atk'].mean()
    return dict(poke_range)
