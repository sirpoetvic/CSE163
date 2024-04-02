def shakiness_by_location(data):
    """Return a dict that stores how “shaky” each location in the dataset is

    Args:
        data (list): list of dictionaries
    Returns:
        An empty dictionary if no earthquakes in dataset

        Dictionary of the "shakiness," defined by adding the magnitude of
        earthquakes, given the location
    """
    amt_shakiness = {}
    if len(data) == 0:
        return {}
    for quake in data:
        magnitude = quake['magnitude']
        quake_name = quake['name']
        if quake_name in amt_shakiness:
            amt_shakiness[quake['name']] += magnitude
        else:
            amt_shakiness[quake['name']] = magnitude
    return amt_shakiness
