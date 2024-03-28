class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(self.nimi)
# aliluokan self viittaa yliluokan attribuutteihin
class Kirja(Julkaisu):
    def __init__(self, nimi, sivut, kirjoittaja):
        self.sivut = sivut
        self.kirjoittaja = kirjoittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"{self.nimi}, {self.kirjoittaja}: {self.sivut} sivua")

# aliluokan self viittaa yliluokan attribuutteihin
class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        self.toimittaja = toimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"{self.toimittaja}, {self.nimi}")
def main():
    kirjasto = []
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")
    kirja = Kirja("Hytti nro:6", 200, "Rosa Liksom")

    kirjasto.append(lehti)
    kirjasto.append(kirja)
    kirjasto.append(Kirja("Mies joka rakasti koiria", 690, "Leonardo"))
    for kirja in kirjasto:
        kirja.tulosta_tiedot()


if __name__ == "__main__":
    main()