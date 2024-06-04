"""
Name: Victor Wong
CSE163
HW2 Manual methods
"""

from pandas import DataFrame


def species_count(data: DataFrame) -> int:
    """
    returns the number of unique pokemon species in the dataset
    as determined by the "name" attribute

    Args:
        data (DataFrame): pokemon dataset

    Returns:
        int: number of unique pokemon
    """
    return len(data["name"].unique())


def max_level(data: DataFrame) -> tuple[str, int]:
    """
    returns a 2-element tuple of the (name, level) of the pokemon with the
    highest level in the dataset

    Args:
        data (DataFrame): pokemon dataset

    Returns:
        tuple[str, int]: tuple containing max level and name
    """
    return (data["name"][data["level"].idxmax()], data["level"].max())


def filter_range(data: DataFrame, lower: int, upper: int) -> list:
    """
    returns last of names pokemon whose level fall within
    the bounds in the same order they appear in the dataset

    Args:
        data (DataFrame): pokemon dataset
        lower (int): min level
        upper (int): max level

    Returns:
        list: list of pokemon whose level falls within lower and upper
    """
    return list(
        data[(data["level"] >= lower) & (data["level"] < upper)]["name"]
    )


def mean_attack_for_type(data: DataFrame, pokemon_type: str):
    """
    returns the average atk for all the pokemon in the dataset with
    the given type. if there are no pokemon of the given type, return None.

    Args:
        data (DataFrame): pokemon dataset
        pokemon_type (str): types
    """
    if pokemon_type not in data["type"].unique():
        return None
    return data[data["type"] == pokemon_type]["atk"].mean()


def count_types(data: DataFrame) -> dict:
    """
    returns a dictionary representing each pokemon type, the number
    of pokemon of that type

    Args:
        data (DataFrame): pokemon dataset

    Returns:
        dict: representing pokemon type, and number of pokemon of each type
    """
    return dict(data.groupby("type").size())


def mean_attack_per_type(data: DataFrame) -> dict:
    """
    returns a dictionary representing each pokmeon type, the average atk
    of pokemon of that type

    Args:
        data (DataFrame): pokemon dataset

    Returns:
        dict: representing pokemon type, and the average atk of type
    """
    return dict(data.groupby("type")["atk"].mean())
