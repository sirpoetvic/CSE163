def minute_countdown():
    print("One minute countdown")
    for i in range(60, -1, -10):
        print(i)

    print("Done!")


def main():
    minute_countdown()


if __name__ == "__main__":
    main()
