"""
Name: Victor Wong
CSE163
"""

import pandas as pd

DATA = "Victor\\HW2\\pokemon_test.csv"
data = pd.read_csv(DATA)


def species_count(df):
    return len(df["name"].unique())


def max_level(df):
    


print(species_count(data))
