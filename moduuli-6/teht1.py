import random


def throw():
    return random.randint(1, 6)


def main():
    while True:
        result = throw()
        print(f"heiton tulos {result}")
        if result == 6:
            break


if __name__ == "__main__":
    main()
