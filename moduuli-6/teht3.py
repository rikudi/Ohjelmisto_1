def gallonat(g):
    litrat = g * 3.785
    return litrat


def main():
    i = int(input("Syötä gallonamäärä: "))
    while True:
        litrat = gallonat(i)
        print(litrat)
        i = int(input("Syötä gallonamäärä: "))
        if i < 0:
            print("Syötetty negatiivinen luku, suljetaan ohjelma")
            break


if __name__ == "__main__":
    main()
