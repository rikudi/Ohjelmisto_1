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

class Sähköauto(Auto):
    def __init__(self,  rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki


def main():
    autot = []
    tunnit = 0
    autot.append(Sähköauto("ABC-15", 250, 52.5))
    autot.append(Polttomoottoriauto("ACD-123", 190, 32.3))

    while tunnit < 4:
        for auto in autot:
            auto.kiihdytä(random.randint(-10, 10))
            auto.kulje(1)
            tunnit += 1
    for auto in autot:
        print(f"{auto.rekisteritunnus} Ajettu matka: ", auto.matka)

if __name__ == "__main__":
    main()