from cse163_utils import parse


def species_count(csv):
    unique_holder = set()
    for i in parse(csv):
        unique_holder.add(i["name"])
    return len(unique_holder)
