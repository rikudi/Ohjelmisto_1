# Ohjelma joka kysyy lukuja kunnes syötetään tyhjä merkkijono ""

num = input("Syötä luku tai paina enter lopettaaksesi: ")
myNums = []

# kysytään lukuja kunnes käyttäjä syöttää tyhjän (enter)
while num != "":
    myNums.append(int(num))
    print(myNums)
    num = input("Syötä luku tai paina enter lopettaaksesi: ")

# järjestetään luvut laskevaan järjestykseen
sortedNums = sorted(myNums, reverse=True)
print(f"sortedNums: {sortedNums}")

# splice metodilla leikataan ensimmäiset 5 lukua sortedNum indeksissä (0, 1, 2, 3, 4) ja sijoitetaan ne uuteen taulukko-muuttujaan highestNums[]
highestNums = sortedNums[:5]
print(f"highestNums: {highestNums}")