"""count_votes"""

# https://cse163.github.io/book/module-1-introduction-to-python/lesson-3-strings-and-lists/practice-count_votes.html


def count_votes(votes: list) -> list:
    """Takes a list of numbers (1, 2, 3), and returns a list
    that shows how many each candidate got.

    Args:
        votes (list): list of numbers indicating votes for candidates
        0, 1, and 2

    Returns:
        list: list of length 3 showing how many counts each
        candidate got
    """

    return_list = [0, 0, 0]
    for i in votes:
        return_list[i] += 1
    return return_list
