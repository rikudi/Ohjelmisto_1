import random

tahkot = int(input("Kuinka monta tahkoa?"))

# nopan heitto funktio, arpoo luvun 1 ja syötetyn parametrin välillä (tahkot)
def noppa(i):
    count = random.randint(1, i)

    return count

# main funktio
def main():
    while True:
        result = noppa(tahkot)
        print(f"heiton tulos {result}")
        if result == tahkot:
            print(f"maksimiluku {result}, ohjelma sulkeutuu")
            break


if __name__ == "__main__":
    main()
