"""largest_earthquake"""

# https://cse163.github.io/book/module-2-data-structures-and-files/lesson-6-csv-data/practice-largest-earthquake.html


def largest_earthquake(data: dict):
    """Returns largest magnitude of earthquake list of dictionaries

    Args:
        data (dict): dictionary containing earthquake data

    Returns:
        String: Name of place with largest magnitude earthquake
    """
    if len(data) == 0:
        return None
    l_mag, name = 0, ""
    for dictionary in data:
        if dictionary["name"] != name and dictionary["magnitude"] > l_mag:
            name = dictionary["name"]
            l_mag = dictionary["magnitude"]
    return name
