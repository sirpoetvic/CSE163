# fun_numbers

# https://cse163.github.io/book/module-2-data-structures-and-files/lesson-4-lists-and-files/practice-build-a-list.html


"""Returns all number divisible by 2 OR 5 in a list"""


def fun_numbers(start, stop):
    """_summary_

    Args:
        start (int): _description_
        stop (int): _description_

    Returns:
        _type_: _description_
    """
    list = []
    for i in range(start, stop):
        if i % 2 == 0 or i % 5 == 0:
            list.append(i)
    return list
