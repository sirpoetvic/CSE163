# countdown

# Link: https://cse163.github.io/book/module-1-introduction-to-python/lesson-2-python-basics/practice-countdown.html


def countdown(n: int) -> None:
    """Outputs a countdown starting at n

    Args:
        num (int): integer num
    """

    if n < 0:
        print("Start must be non-negative!")
    else:
        print(n, "second countdown")
        for i in range(n, -1, -10):
            print(i)
        print("Done!")


def sample_run():
    """Method testing countdown with various test cases"""

    countdown(60)
    print()
    countdown(15)
    print()
    countdown(-4)
    print()
    countdown(0)


def main():
    """Main method runs sample function"""
    sample_run()


if __name__ == "__main__":
    main()
