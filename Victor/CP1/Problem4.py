# fun_numbers

# https://cse163.github.io/book/module-2-data-structures-and-files/lesson-5-data-structures-tuple-set-dict/practice-build-a-list-comprehension.html


def fun_numbers(start, stop):
    return [i for i in range(start, stop) if (i % 2 == 0 and i % 5 == 0)]
