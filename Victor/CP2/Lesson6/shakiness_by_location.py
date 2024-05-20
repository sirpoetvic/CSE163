"""shakiness_by_location"""

# https://cse163.github.io/book/module-2-data-structures-and-files/lesson-6-csv-data/practice-shakiness-by-location.html


def shakiness_by_location(data: list) -> dict:
    """Returns a dictionary of total magnitude per location

    Args:
        data (list): list of dictionaries showing name and
        magnitude of earthquakes

    Returns:
        dictionary: dictionary of total magnitude per location
    """

    if len(data) == 0:
        return {}
    earthquake_dictionary = {}
    earthquake_names = []
    for i in data:
        if i["name"] not in earthquake_names:
            earthquake_dictionary[i["name"]] = i["magnitude"]
            earthquake_names.append(i["name"])
        else:
            earthquake_dictionary[i["name"]] += i["magnitude"]
    return earthquake_dictionary
