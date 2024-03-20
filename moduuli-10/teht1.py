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


def main():
    h = Hissi(5,11)
    h.siirry_kerrokseen(3)

if __name__ == "__main__":
    main()