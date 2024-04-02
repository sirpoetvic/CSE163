# fun_numbers

# https://cse163.github.io/book/module-2-data-structures-and-files/lesson-5-data-structures-tuple-set-dict/practice-build-a-list-comprehension.html


def fun_numbers(start: int, stop: int) -> list:
    """Returns all numbers divisible by 2 or 5 in a list
    using list comprehension

    Args:
        start (int): start number
        stop (int): end number

    Returns:
        list: list containing numbers divisible by 2 or 5
    """
    return [i for i in range(start, stop) if (i % 2 == 0 or i % 5 == 0)]
