"""
Name: Victor Wong
CSE163
"""


def species_count(df):
    return len(df["name"].unique())


def max_level(df):
    return (df["name"][df["level"].idxmax()], df["level"].max())


def filter_range(df, lower: int, upper: int):
    return list(df[(df["level"] >= lower) & (df["level"] < upper)]["name"])


def mean_attack_for_type(df, pokemon_type):
    if pokemon_type not in df["type"].unique():
        return None
    return df[df["type"] == pokemon_type]["atk"].mean()


def count_types(df):
    return dict(df.groupby("type").size())


def mean_attack_per_type(df):
    return dict(df.groupby("type")["atk"].mean())
