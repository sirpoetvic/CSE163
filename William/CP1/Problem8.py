def largest_magnitude(data):
    """
    Returns largest magnitude of earthquake within a list of dicts
    If length = 0, return None

    Args:
        data (list): list of dicts earthquake data

    Returns:
        String: name/location with the largest magnitude
    """
    magnitude, quake_name = 0, ""
    for quake in data:
        if quake['magnitude'] > magnitude and quake_name != quake['name']:
            magnitude = quake['magnitude']
            quake_name = quake['name']
    return quake_name
