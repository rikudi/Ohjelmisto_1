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
    game_over = False
    autot = []
    for i in range(1, 11):
        autot.append(Auto(f"ABC-" + str(i), random.randint(100, 200)))
    while not game_over:
        for auto in autot:
            auto.kiihdytä(random.randint(-15, 15))
            auto.kulje(1)
            if auto.matka >= 10000:
                game_over = True
                break
    for auto in autot:
        print("Rekkari: ", auto.rekisteritunnus, "Huippunopeus: ", auto.huippunopeus, "km/h", "Nopeus: ", auto.nopeus, "km/h", "Kuljettu matka: ", auto.matka, "km")

main()
