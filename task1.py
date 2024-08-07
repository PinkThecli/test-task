def main():
    print(1234, is_even(1234))
    print(4321, is_even(4321))


def is_even(n: int) -> bool:
    return not (n & 0b1)


if __name__ == "__main__":
    main()
