# TEHTÄVÄ 4
import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.nopeus = 0
        self.matka = 0
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus <= 0:
            self.nopeus = 0
        return

    def kulje(self, tunnit):
        self.matka += tunnit * self.nopeus
        return

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-15, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.autot:
            print(f"Auto {auto.rekisteritunnus}: Matka = {auto.matka} km, Nopeus = {auto.nopeus} km/h")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus_km:
                return True
        return False

def main():
    autot = []
    tunnit = 0
    for i in range(1, 11):
        autot.append(Auto(f"ABC-"+str(i), random.randint(100, 200)))
    kisa = Kilpailu("Suuri romuralli", 8000, autot)

    while not kisa.kilpailu_ohi():
        kisa.tunti_kuluu()
        tunnit += 1
        if tunnit % 10 == 0:
            print(f"\nAJETTU: {tunnit} tuntia\n")
            kisa.tulosta_tilanne()

if __name__ == "__main__":
    main()

