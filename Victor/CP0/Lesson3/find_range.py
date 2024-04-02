"""Write a function named find_range() that takes a list of integers
   and returns the range of values found in the list."""

# Link: https://cse163.github.io/book/module-1-introduction-to-python/lesson-3-strings-and-lists/practice-find_range.html


def find_range(input_list: list) -> int:
    """Given a list, returns the range of values found in the list

    Args:
        input (int): list of integers

    Returns:
        int: range of values in the list
    """
    return max(input_list) - min(input_list) + 1
