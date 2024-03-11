"""
Name: Victor Wong
CSE163
"""

from cse163_utils import parse


def species_count(csv):
    unique_holder = set()
    for i in parse(csv):
        unique_holder.add(i["name"])
    return len(unique_holder)


def max_level(csv):
    highest_level = ["", 0]
    for i in parse(csv):
        if i["level"] > highest_level[1]:
            highest_level[0] = i["name"]
            highest_level[1] = i["level"]
    return highest_level


def filter_range(csv, lower, upper):
    contained_levels = list()
    for i in parse(csv):
        if (i["level"] >= lower) and (i["level"] < upper):
            contained_levels.append(i["name"])
    return contained_levels


print(filter_range("pokemon_test.csv", 35, 72))
