import math


def laskuri(halkaisija, hinta):
    # ensiksi lasketaan pinta-ala
    sade = halkaisija / 2  # säde
    p_ala = math.pi * (math.pow(sade, 2) / 100)  # pinta-ala pi*säde^2. Jaetaan sadalla ja muunnetaan neliömetreiksi

    hinta_per_neliometri = hinta / p_ala
    return hinta_per_neliometri


def main():
    halkaisija_yksi = float(input("1. Pizzan halkaisija senttimetreinä: "))
    hinta_yksi = float(input("1. Pizzan Hinta: "))

    halkaisija_kaksi = float(input("2. Pizzan halkaisija senttimetreinä"))
    hinta_kaksi = float(input("2. Pizzan Hinta: "))

    eka_pizza = laskuri(halkaisija_yksi, hinta_yksi)
    toka_pizza = laskuri(halkaisija_kaksi, hinta_kaksi)

    print(f"Hinta per neliömetri 1. pizzalle: {eka_pizza:.2f} euroa")
    print(f"Hinta per neliömetri 2. pizzalle: {toka_pizza:.2f} euroa")


if __name__ == "__main__":
    main()