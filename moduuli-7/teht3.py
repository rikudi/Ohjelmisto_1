#kysyy haluaako syöttää uuden lentoaseman, hakea lentoaseman tiedot vai lopettaa.
lentoasemat = {

}

def hae_lentokentat(i):
    if i == "":
        print("Lopetetaan...")
    elif i == "uusi" :
        print("Uusi lentoasema...")
        icao = input("Lentoaseman ICAO koodi: ")
        nimi = input("Lentoaseman nimi:")
    elif i == "hae":
        print("Haetaan lentoaseman tiedot...")

    return

def main():

    i = input("Syötä 'uusi', jos haluat lisätä lentoaseman. "
              "Syötä 'hae', jos haluat hakea lentoaseman tiedot. "
              "Paina enter jos haluat lopettaa.")
    hae_lentokentat(i)


if __name__ == "__main__":
    main()