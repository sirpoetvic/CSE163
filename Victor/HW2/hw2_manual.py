"""
Name: Victor Wong
CSE163
"""


def species_count(parsed_csv):
    unique_holder = set()
    for i in parsed_csv:
        unique_holder.add(i["name"])
    return len(unique_holder)


def max_level(parsed_csv):
    highest_level = ["", 0]
    for i in parsed_csv:
        if i["level"] > highest_level[1]:
            highest_level[0] = i["name"]
            highest_level[1] = i["level"]
    return tuple(highest_level)


def filter_range(parsed_csv, lower: int, upper: int):
    contained_levels = list()
    for i in parsed_csv:
        if (i["level"] >= lower) and (i["level"] < upper):
            contained_levels.append(i["name"])
    return contained_levels


def mean_attack_for_type(parsed_csv, pokemon_type):
    total = 0
    length = 0
    for i in parsed_csv:
        if pokemon_type == i["type"]:
            total += i["atk"]
            length += 1
    if length == 0:
        return None
    return total / length


def count_types(parsed_csv):
    type_dict = {}
    for i in parsed_csv:
        if i["type"] in type_dict:
            type_dict[i["type"]] = type_dict[i["type"]] + 1
        else:
            type_dict[i["type"]] = 1
    return type_dict


def mean_attack_per_type(parsed_csv):
    attack_for_type_dict = dict()
    type_set = {i["type"] for i in parsed_csv}
    for pokemon_type in type_set:
        attack_for_type_dict[pokemon_type] = mean_attack_for_type(
            parsed_csv, pokemon_type
        )
    return attack_for_type_dict
