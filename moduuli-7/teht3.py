lentoasemat = {}  # Tässä tallennetaan lentoasematiedot

while True:
    print("\n1 - Syötä uusi lentoasema")
    print("2 - Hae lentoaseman tiedot")
    print("3 - Lopeta")

    valinta = input("Valitse toiminto (1, 2 tai 3): ")

    if valinta == "1":
        icao_koodi = input("Syötä lentoaseman ICAO-koodi: ").upper()
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao_koodi] = nimi
        print(f"Lentoasema {nimi} ({icao_koodi}) tallennettu onnistuneesti.")

    elif valinta == "2":
        icao_koodi = input("Syötä haettavan lentoaseman ICAO-koodi: ").upper()
        if icao_koodi in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[icao_koodi]}")
        else:
            print(f"Lentoasemaa {icao_koodi} ei löytynyt.")

    elif valinta == "3":
        print("Lopetetaan..")
        break

    else:
        print("Virheellinen valinta. Valitse 1, 2 tai 3.")
