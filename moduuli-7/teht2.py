nimet = set()
def hae_nimet(nimi):
    while nimi != "":
        if nimi in nimet:
            print("Aiemmin syötetty nimi")
            nimi = input("Anna nimi: ")
        else:
            nimet.add(nimi)
            print("Uusi nimi")
            nimi = input("Anna nimi: ")

def main():
    print(f"nimet: {nimet}")
    nimi = input("Anna nimi: ")
    hae_nimet(nimi)

    for i in nimet:
        print(i)


if __name__ == "__main__":
    main()