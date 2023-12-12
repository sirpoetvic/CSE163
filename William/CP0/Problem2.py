def countdown(number):
    if number < 0:
        print("Start must be non-negative!")
    else:
        print(f"{number} second countdown!")
        for i in range(number, -1, -10):
            print(i)

        print("Done!")


def sample_run():
    countdown(60)
    print()
    countdown(15)
    print()
    countdown(-4)
    print()
    countdown(0)


def main():
    sample_run()


if __name__ == "__main__":
    main()
