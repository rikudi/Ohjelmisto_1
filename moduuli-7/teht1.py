def hae_vuodenaika(kuukausi):
    vuodenajat = ("Talvi", "Talvi",
             "Kevät", "Kevät", "Kevät",
             "Kesä", "Kesä", "Kesä",
             "Syksy", "Syksy", "Syksy", "Talvi")

    if 1 <= kuukausi <= len(vuodenajat):
        return vuodenajat[kuukausi - 1]  # -1 jotta saadaan syötettä vastaava vuodenaika oikeasta indeksistä
    else:
        print("virheellinen kuukauden numero")


def main():
    kuukausi = int(input("Kuukauden numero: "))
    vuodenaika = hae_vuodenaika(kuukausi)
    print(f"Kuukausi {kuukausi} on vuodenaikaa: {vuodenaika}")


if __name__ == "__main__":
    main()

