# area_codes

# https://cse163.github.io/book/module-2-data-structures-and-files/lesson-5-data-structures-tuple-set-dict/practice-area-codes.html


def area_codes(phone_list: list) -> list:
    """Returns a list containing the unique area
    codes of a list of phone numbers

    Args:
        phone_list (list): list of phone nmbers

    Returns:
        list: list of unique area codes
    """
    return list(set([phone[:3] for phone in phone_list]))
