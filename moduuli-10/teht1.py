# TEHTÄVÄT 1-3
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kerros):
        if kerros == self.kerros:
            print("Ollaan jo kerroksessa!!")
            return
        if kerros > self.kerros:
            while self.kerros < kerros:
                self.kerros_ylos()
                print(self.kerros)
        else:
            while self.kerros > kerros:
                self.kerros_alas()
                print(self.kerros)
    def kerros_ylos(self):
        self.kerros += 1

    def kerros_alas(self):
        self.kerros -= 1

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []

        for i in range(maara):
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros))

    def aja_hissiä(self, hissi_nro, kerros):
        if hissi_nro < len(self.hissit):
            self.hissit[hissi_nro].siirry_kerrokseen(kerros)
        else:
            print("Väärä hissin numero")

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)

def main():
    koti = Talo(0, 5, 2)
    koti.aja_hissiä(1, 5)
    koti.aja_hissiä(0, 3)
    koti.palohalytys()
    print("Hissi yksi  kerros: ", koti.hissit[0].kerros, "Hissi kaksi kerros: ", koti.hissit[1].kerros)

if __name__ == "__main__":
    main()