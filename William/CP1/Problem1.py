
# https://cse163.github.io/book/module-2-data-structures-and-files/lesson-4-lists-and-files/practice-build-a-list.html

def fun_numbers(num1, num2):

    """
    Args:
        num1 (int): starting number
        num2 (int): stopping numebr
    Returns:
        fun_range: all numbers divisible by 2 or 5 in range start to stop

    All numbers divisble by 2 or 5 are put in a list and retunred
    """
    fun_range = []

    if num2 <= num1:
        return fun_range

    for i in range(num1, num2):
        if (i % 2 == 0 or i % 5 == 0):
            fun_range.append(i)
    fun_range.sort()
    return fun_range
