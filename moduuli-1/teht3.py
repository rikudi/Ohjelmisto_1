#Ohjelma joka kysyy käyttäjän syötettä ja tallettaa ne float muuttujiin.
#Sen jälkeen tulostaa piirin ja pinta-alan.
kanta = float(input("Anna suorikulmion kannan pituus:"))
korkeus = float(input("Anna suorakulmion korkeus:"))

print("Suorakulmion piiri: ", kanta*2+korkeus*2)
print("Suorakulmion pinta-ala: ", kanta*korkeus)
