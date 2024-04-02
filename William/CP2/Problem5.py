def area_codes(phone_numbers):
    """
    Takes a list of str as input where each str in the list is a phone #.
    Returns the number of unique area codes found in those phone #.

    Args:
        phone_numbers (str list):
    Returns:
        Area codes (first 3 numbers of the phone #)
    """
    return len(set(phone[:3] for phone in phone_numbers))
