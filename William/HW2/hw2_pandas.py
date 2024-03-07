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
        data (list): A list of tuples representing parsed pokemon data.
            Each tuple contains (name, level) where name is the
            name of the pokemon and level is its corresponding level
    """
    df = pd.read_csv(data)
    max_lvl = df['level'].max()
    max_level_index = df['level'].idxmax()
    species = df.loc[max_level_index, 'name']
    return (species, max_lvl)


def filter_range(data):
    pass