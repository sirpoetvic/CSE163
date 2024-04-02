"""minute_countdown"""

# https://cse163.github.io/book/module-1-introduction-to-python/lesson-2-python-basics/practice-minute-countdown.html


def one_minute_countdown():
    """Counts down in the terminal 1 minute, in 10 second increments"""

    print("One minute countdown")
    for i in range(60, -1, -10):
        print(i)
    print("Done!")


def main():
    """Main method"""

    one_minute_countdown()


if __name__ == "__main__":
    main()
