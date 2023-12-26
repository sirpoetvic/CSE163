""" wWite a program following the "main pattern" where main() will
    output a 60 second countdown."""


def one_minute_countdown():
    print("One minute countdown")
    for i in range(60, -1, -10):
        print(i)
    print("Done!")


def main():
    one_minute_countdown()


if __name__ == "__main__":
    main()
