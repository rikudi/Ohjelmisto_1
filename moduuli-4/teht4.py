#Peli joka arpoo random luvun ja kysyy käyttäjältä lukua
import random
a = random.randint(1, 10) #random-luku
i = int(input("Arvaa luku 1-10 väliltä: ")) #syöte

while i != a:
    if i < a:
        print("Luku on suurempi")
        i = int(input("Syötä numero: "))
    elif i > a:
        print("Luku on pienempi")
        i = int(input("Syötä numero: "))
print("Luku oikein, peli loppui")