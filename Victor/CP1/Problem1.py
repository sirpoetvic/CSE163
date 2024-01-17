# fun_numbers

# https://cse163.github.io/book/module-2-data-structures-and-files/lesson-4-lists-and-files/practice-build-a-list.html


def fun_numbers(start, stop):
    """Returns all numbers divisible by 2 or 5 in a list

    Args:
        start (int): start number
        stop (int): end number

    Returns:
        list: all numbers divisible by 2 or 5 in range start to stop
    """
    return_list = []
    for i in range(start, stop):
        if i % 2 == 0 or i % 5 == 0:
            return_list.append(i)
    return return_list
