"""
Name: Victor Wong
CSE163
HW2 Manual methods
"""


def species_count(parsed_csv: list) -> int:
    """
    returns the number of unique pokemon species in the dataset
    as determined by the "name" attribute

    Args:
        parsed_csv (list): parsed pokemon csv

    Returns:
        int: number of unique pokemon
    """
    unique_holder = set()
    for i in parsed_csv:
        unique_holder.add(i["name"])
    return len(unique_holder)


def max_level(parsed_csv: list) -> tuple[str, int]:
    """
    returns a 2-element tuple of the (name, level) of the pokemon with the
    highest level in the dataset

    Args:
        parsed_csv (list): parsed pokemon csv

    Returns:
        tuple[str, int]: tuple containing max level and name
    """

    highest_level = ["", 0]
    for i in parsed_csv:
        if i["level"] > highest_level[1]:
            highest_level[0] = i["name"]
            highest_level[1] = i["level"]
    return tuple(highest_level)


def filter_range(parsed_csv: list, lower: int, upper: int) -> list:
    """
    returns last of names pokemon whose level fall within
    the bounds in the same order they appear in the dataset

    Args:
        parsed_csv (list): parsed pokemon csv
        lower (int): min level
        upper (int): max level

    Returns:
        list: list of pokemon whose level falls within lower and upper
    """
    contained_levels = list()
    for i in parsed_csv:
        if (i["level"] >= lower) and (i["level"] < upper):
            contained_levels.append(i["name"])
    return contained_levels


def mean_attack_for_type(parsed_csv: list, pokemon_type: str):
    """
    returns the average atk for all the pokemon in the dataset with
    the given type. if there are no pokemon of the given type, return None.

    Args:
        parsed_csv (list): parsed pokemon dataset
        pokemon_type (str): type
    """
    total = 0
    length = 0
    for i in parsed_csv:
        if pokemon_type == i["type"]:
            total += i["atk"]
            length += 1
    if length == 0:
        return None
    else:
        return total / length


def count_types(parsed_csv: list) -> dict:
    """
    returns a dictionary representing each pokemon type, the number
    of pokemon of that type

    Args:
        parsed_csv (list): parsed pokemon csv

    Returns:
        dict: representing pokemon type, and number of pokemon of each type
    """
    type_dict = {}
    for i in parsed_csv:
        if i["type"] in type_dict:
            type_dict[i["type"]] = type_dict[i["type"]] + 1
        else:
            type_dict[i["type"]] = 1
    return type_dict


def mean_attack_per_type(parsed_csv: list) -> dict:
    """
    returns a dictionary representing each pokmeon type, the average atk
    of pokemon of that type

    Args:
        parsed_csv (list): parsed pokemon csv

    Returns:
        dict: representing pokemon type, and the average atk of type
    """
    attack_for_type_dict = dict()
    type_set = {i["type"] for i in parsed_csv}
    for pokemon_type in type_set:
        attack_for_type_dict[pokemon_type] = mean_attack_for_type(
            parsed_csv, pokemon_type
        )
    return attack_for_type_dict
