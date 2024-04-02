# fibonacci

# Link: https://cse163.github.io/book/module-1-introduction-to-python/lesson-2-python-basics/practice-fibonacci.html


def fibonacci(num: int):
    """Returns the first fibonacci number that is greater than n

    Args:
        num (int): integer n

    Returns:
        int: first fibonacci number that is greater than n
    """

    num1, num2 = 0, 1
    while num2 <= num:
        num1, num2 = num2, num1 + num2
    return num2


def main():
    """Main method asserting test cases"""

    assert fibonacci(3) == 5
    assert fibonacci(6) == 8
    assert fibonacci(-2) == 1


if __name__ == "__main__":
    main()
