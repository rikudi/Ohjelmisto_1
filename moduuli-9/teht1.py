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

def main():
    autot = []
    a = 0
    for i in range(10):
        a += 1
        autot.append(Auto(f"ABC-{a}", random.randint(100, 200)))

    while True:
        game_over = False
        for auto in autot:
            auto.kiihdytä(random.randint(-15, 15))
            auto.kulje(1)
            if auto.matka >= 10000:
                game_over = True
                break
        if game_over:
            break
        else:
            continue
    for auto in autot:
        print("Rekkari: ", auto.rekisteritunnus, "Huippunopeus: ", auto.huippunopeus, "km/h", "Nopeus: ", auto.nopeus, "km/h", "Kuljettu matka: ", auto.matka, "km")

main()
